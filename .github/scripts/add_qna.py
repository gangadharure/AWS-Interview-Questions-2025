#!/usr/bin/env python3
import os, re, pathlib, subprocess, sys, shutil, json

ROOT = pathlib.Path(__file__).resolve().parents[2]
PUBLISHED_FILE = ROOT / "AWS_Interview_QA_2025_details.md"
STATE_FILE = ROOT / ".data" / "published_index.json"

DEFAULT_BATCH = int(os.getenv("BATCH_SIZE", "2"))

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
    url = f"https://{SOURCE_TOKEN}:x-oauth-basic@github.com/{SOURCE_REPO}.git"
    dest = tmpdir / "src"
    run(["git", "clone", "--depth=1", "--branch", SOURCE_BRANCH, url, str(dest)])
    return dest

def parse_items(text: str):
    items = []
    q_pat = re.compile(r'^\s*Q\d+\)\s*(.+)$', re.IGNORECASE)
    lines = text.splitlines()
    current_q, buf = None, []
    for line in lines:
        m = q_pat.match(line)
        if m:
            if current_q:
                items.append((current_q, " ".join(buf).strip()))
                buf = []
            current_q = f"Q) {m.group(1).strip()}"
        elif line.strip().lower().startswith("answer:"):
            buf.append(line.split(":",1)[1].strip())
        else:
            if current_q:
                buf.append(line.strip())
    if current_q:
        items.append((current_q, " ".join(buf).strip()))
    return items

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

def append_details_blocks(pairs, start_index, batch=DEFAULT_BATCH):
    if not PUBLISHED_FILE.exists():
        PUBLISHED_FILE.write_text("# AWS Interview Q&A (Daily Updates)\n\n", encoding="utf-8")

    content = PUBLISHED_FILE.read_text(encoding="utf-8")
    n0, appended = start_index, 0

    for i in range(batch):
        idx = n0 + i
        if idx >= len(pairs): break
        q_raw, a_raw = pairs[idx]
        qline = q_raw.strip()
        if not re.match(r'Q\d+\)', qline):
            qline = f"Q{idx+1}) {qline}"
        abody = a_raw.strip()
        block = f"""<details>
  <summary><strong>{qline}</strong></summary>
  <p>{abody}</p>
</details>

"""
        content += block
        appended += 1

    if appended > 0:
        PUBLISHED_FILE.write_text(content, encoding="utf-8")
    return appended

def main():
    if not (SOURCE_REPO and SOURCE_TOKEN):
        print("Missing SOURCE_REPO or SOURCE_TOKEN", file=sys.stderr)
        return 1

    tmpdir = pathlib.Path("tmp_src")
    if tmpdir.exists(): shutil.rmtree(tmpdir)
    tmpdir.mkdir(parents=True, exist_ok=True)

    src = clone_private_source(tmpdir)
    src_file = src / SOURCE_FILE
    if not src_file.exists():
        print(f"Source file not found: {src_file}", file=sys.stderr)
        return 2

    items = parse_items(src_file.read_text(encoding="utf-8"))
    if not items:
        print("No Q&A items parsed.", file=sys.stderr)
        return 3

    published_count = load_state()
    appended = append_details_blocks(items, start_index=published_count, batch=DEFAULT_BATCH)

    if appended > 0:
        published_count += appended
        save_state(published_count)
        print(f"Appended {appended} items. Published total: {published_count}/{len(items)}")
    else:
        print("No more items to append.")

if __name__ == "__main__":
    sys.exit(main())
