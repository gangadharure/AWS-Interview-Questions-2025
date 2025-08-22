#!/usr/bin/env python3
import os, re, pathlib, subprocess, sys, shutil, json

ROOT = pathlib.Path(__file__).resolve().parents[2]
PUBLISHED_FILE = ROOT / "AWS_Interview_QA_2025_details.md"
STATE_FILE = ROOT / ".data" / "published_index.json"

DEFAULT_BATCH = int(os.getenv("BATCH_SIZE", "3"))

SOURCE_REPO   = os.getenv("SOURCE_REPO")
SOURCE_BRANCH = os.getenv("SOURCE_BRANCH", "main")
SOURCE_FILE   = os.getenv("SOURCE_FILE", "all_questions.md")
SOURCE_TOKEN  = os.getenv("SOURCE_TOKEN")

def run(cmd, cwd=None, check=True):
    res = subprocess.run(cmd, cwd=cwd, text=True, capture_output=True)
    if check and res.returncode != 0:
        print(res.stdout)
        print(res.stderr, file=sys.stderr)
        raise SystemExit(res.returncode)
    return res

def clone_private_source(tmpdir: pathlib.Path) -> pathlib.Path:
    url = f"https://x-access-token:{SOURCE_TOKEN}@github.com/{SOURCE_REPO}.git"
    dest = tmpdir / "src"
    run(["git", "clone", "--depth=1", "--branch", SOURCE_BRANCH, url, str(dest)])
    return dest

def parse_items(text: str):
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
        elif line.lower().startswith("answer:"):
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
        except:
            return 0
    return 0

def save_state(count: int):
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(json.dumps({"published_count": count}), encoding="utf-8")

def ensure_header():
    if not PUBLISHED_FILE.exists():
        PUBLISHED_FILE.write_text("# AWS Interview Q&A (Daily Updates)\n\n", encoding="utf-8")

def append_blocks(pairs, start, batch=DEFAULT_BATCH):
    ensure_header()
    content = PUBLISHED_FILE.read_text(encoding="utf-8")
    appended = 0

    for i in range(batch):
        idx = start + i
        if idx >= len(pairs): break
        q, a = pairs[idx]
        block = f"<details>\n  <summary><strong>{q}</strong></summary>\n  <p>{a}</p>\n</details>\n\n"
        content += block
        appended += 1

    if appended > 0:
        PUBLISHED_FILE.write_text(content, encoding="utf-8")
    return appended

def main():
    tmp = pathlib.Path("tmp_src")
    if tmp.exists(): shutil.rmtree(tmp)
    tmp.mkdir()

    src = clone_private_source(tmp)
    src_file = src / SOURCE_FILE
    if not src_file.exists():
        print("Source file missing.", file=sys.stderr); sys.exit(2)

    items = parse_items(src_file.read_text(encoding="utf-8"))
    if not items:
        print("No items parsed.", file=sys.stderr); sys.exit(3)

    start = load_state()
    added = append_blocks(items, start)
    if added:
        save_state(start + added)
        print(f"Appended {added} items. Now at {start + added}/{len(items)}")
    else:
        print("All items already published.")

if __name__ == "__main__":
    sys.exit(main())
