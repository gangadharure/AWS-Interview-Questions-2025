#!/usr/bin/env python3
"""
Normalize a messy all_questions.md into a clean, machine-parseable source.

Input (env):
  SOURCE_LOCAL_FILE  - e.g., "source/all_questions.md"
  OUTPUT_FILE        - e.g., "source/cleaned_all_questions.md"
  RENUMBER           - "true" (default) to renumber Q1..Qn sequentially, "false" to keep original

What it fixes:
- Strips marketing preface; starts at the first Q-line
- Unifies “Answer:” label (handles “Answer :”, “Ans:”, “A n s w e r :”, etc.)
- Collapses broken “W h a t  i s  A W S ?” into “What is AWS?”
- Removes stray control chars, smart quotes, double spaces, OCR garbage
- Reflows wrapped lines so each Q and Answer becomes a single paragraph
- Ensures consistent format:

  Q42) Your question text...
  Answer: Your answer text...

Output:
- Writes a clean file the publisher script can parse reliably.
"""
import os, re, pathlib, unicodedata

ROOT = pathlib.Path(__file__).resolve().parents[2]
SRC  = ROOT / os.getenv("SOURCE_LOCAL_FILE", "")
OUT  = ROOT / os.getenv("OUTPUT_FILE", "source/cleaned_all_questions.md")
RENUMBER = os.getenv("RENUMBER", "true").lower() in ("1","true","yes","y")

def strip_weird(s: str) -> str:
    # normalize unicode & remove control chars except \n
    s = unicodedata.normalize("NFKC", s)
    s = s.replace("\uFFFD", "")
    s = re.sub(r"[\x00-\x08\x0b-\x1f\x7f]", "", s)
    # normalize quotes/dashes
    s = s.replace("’","'").replace("‘","'").replace("“",'"').replace("”",'"').replace("–","-").replace("—","-")
    return s

def collapse_spaced_words(line: str) -> str:
    """
    Convert 'W h a t  i s  A W S ?' -> 'What is AWS?'
    Heuristic: many single letters separated by single spaces.
    """
    # Only attempt if looks like inter-letter spacing
    if re.search(r"(?:\b\w\s){4,}\w\b", line):
        # Remove single spaces between letters but keep normal word spaces
        # First, compress multiple spaces to single
        line = re.sub(r"[ \t]+", " ", line)
        # Replace letter-space-letter (within a word) with joined letters iteratively
        line = re.sub(r"(?<=\b\w)\s(?=\w\b)", "", line)  # join A _ B patterns
        # Fix over-joining by restoring spaces around normal words if missing (best-effort)
    return line

def normalize_answer_label(line: str) -> str:
    # Unify any variant like "Answer :", "Ans:", "A n s w e r :", "Answer-"
    clean = collapse_spaced_words(line)
    clean = re.sub(r"^\s*(ans(?:wer)?)[\s:-]*", "Answer: ", clean, flags=re.I)
    return clean

def is_q_line(line: str) -> re.Match:
    # Accept Q12), Q 12), q12), Q12 ) etc.
    return re.match(r"^\s*[Qq]\s*(\d+)\)\s*(.+)$", line)

def main():
    if not SRC.exists():
        print(f"ERROR: source not found: {SRC}")
        return 2

    raw = SRC.read_text(encoding="utf-8", errors="ignore")
    raw = strip_weird(raw)

    # Split lines, clean per-line
    lines = [collapse_spaced_words(l.rstrip()) for l in raw.splitlines()]
    # find first Q line; drop any marketing preface above it
    start_idx = 0
    for i,l in enumerate(lines):
        if is_q_line(l):
            start_idx = i
            break
    lines = lines[start_idx:]

    # Pass 1: normalize "Answer" spelling on all lines
    lines = [normalize_answer_label(l) for l in lines]

    # Pass 2: stitch Q/Answer blocks into records
    items = []  # list of (orig_num, question_text, answer_text)
    cur_q_num = None
    cur_q_text = []
    cur_ans_text = []
    mode = None  # "Q" or "A"

    for l in lines:
        m = is_q_line(l)
        if m:
            # flush previous
            if cur_q_num is not None:
                q = " ".join(cur_q_text).strip()
                a = " ".join(cur_ans_text).strip()
                if q and a:
                    items.append((cur_q_num, q, a))
            # start new
            cur_q_num = int(m.group(1))
            cur_q_text = [m.group(2).strip()]
            cur_ans_text = []
            mode = "Q"
            continue
        if re.match(r"^\s*Answer:\s*(.*)", l, flags=re.I):
            mode = "A"
            cur_ans_text.append(re.sub(r"^\s*Answer:\s*", "", l, flags=re.I).strip())
            continue
        # continue current section
        if mode == "Q":
            if l.strip():
                cur_q_text.append(l.strip())
        elif mode == "A":
            if l.strip():
                cur_ans_text.append(l.strip())
        else:
            # ignore lines before first Q/Answer
            pass

    # flush last
    if cur_q_num is not None:
        q = " ".join(cur_q_text).strip()
        a = " ".join(cur_ans_text).strip()
        if q and a:
            items.append((cur_q_num, q, a))

    if not items:
        print("ERROR: No Q&A items parsed after normalization.")
        return 3

    # Optional renumber
    if RENUMBER:
        items = [(i+1, q, a) for i,(_,q,a) in enumerate(items)]

    # Write clean file
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", encoding="utf-8") as f:
        for num, q, a in items:
            f.write(f"Q{num}) {q}\n")
            f.write(f"Answer: {a}\n\n")

    print(f"Normalized {len(items)} Q&A items -> {OUT}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
