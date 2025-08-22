#!/usr/bin/env python3
import os, re, pathlib, json

ROOT = pathlib.Path(__file__).resolve().parents[2]
PUBLISHED_FILE = ROOT / "AWS_Interview_QA_2025_details.md"
STATE_FILE = ROOT / ".data" / "published_index.json"

BATCH = int(os.getenv("BATCH_SIZE", "3"))
SOURCE_LOCAL_FILE = os.getenv("SOURCE_LOCAL_FILE")  # e.g., "source/all_questions.md"

def parse_items(text: str):
    """Parse Q&A lines:
       Q123) Question text...
       Answer: Answer body..."""
    items = []
    q_pat = re.compile(r'^\s*(Q\d+\))\s*(.+)$')
    lines = text.splitlines()
    current_q, buf = None, []
    for line in lines:
        m = q_pat.match(line)
        if m:
            if current_q:
                items.append((current_q, " ".join(buf).strip()))
                buf = []
            current_q = f"{m.group(1)} {m.group(2).strip()}"
        elif line.strip().lower().startswith("answer:"):
            buf.append(line.split(":",1)[1].strip())
        else:
            if current_q:
                buf.append(line.strip())
    if current_q:
        items.append((current_q, " ".join(buf).strip()))
    return [(q,a) for q,a in items if q and a]

def load_state() -> int:
    if STATE_FILE.exists():
        try:
            return int(json.loads(STATE_FILE.read_text()).get("published_count", 0))
        except Exception:
            return 0
    return 0

def save_state(count: int):
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(json.dumps({"published_count": count}), encoding="utf-8")

def ensure_header():
    if not PUBLISHED_FILE.exists():
        PUBLISHED_FILE.write_text("# AWS Interview Q&A (Daily Updates)\n\n", encoding="utf-8")

def append_blocks(pairs, start, batch=BATCH):
    ensure_header()
    content = PUBLISHED_FILE.read_text(encoding="utf-8")
    appended = 0
    for i in range(batch):
        idx = start + i
        if idx >= len(pairs): break
        q, a = pairs[idx]
        block = f"<details>\n  <summary><strong>{q.strip()}</strong></summary>\n  <p>{a.strip()}</p>\n</details>\n\n"
        content += block
        appended += 1
    if appended:
        PUBLISHED_FILE.write_text(content, encoding="utf-8")
    return appended

def main():
    if not SOURCE_LOCAL_FILE:
        print("ERROR: SOURCE_LOCAL_FILE env var not set."); return 2
    src = ROOT / SOURCE_LOCAL_FILE
    if not src.exists():
        print(f"ERROR: Source file not found: {src}"); return 2

    items = parse_items(src.read_text(encoding="utf-8"))
    if not items:
        print("ERROR: No Q&A items parsed."); return 3

    published = load_state()
    added = append_blocks(items, published, BATCH)
    if added:
        save_state(published + added)
        print(f"Appended {added} items. Total published: {published + added}/{len(items)}")
    else:
        print("No more items to append.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
