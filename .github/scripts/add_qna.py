name: Add Daily Q&A

on:
  schedule:
    - cron: "30 3 * * *"   # daily ~09:00 IST
  workflow_dispatch: {}

permissions:
  contents: write

env:
  BATCH_SIZE: "3"          # publish 3/day (set "2" if you prefer 2/day)

jobs:
  update:
    runs-on: ubuntu-latest
    steps:
      # 1) Checkout THIS public repo
      - uses: actions/checkout@v4

      # 2) Checkout your PRIVATE repo into ./source using your PAT
      - name: Checkout private source repo
        uses: actions/checkout@v4
        with:
          repository: ${{ secrets.SOURCE_REPO }}      # e.g., gangadharure/AWS-Interview-Questions
          ref: ${{ secrets.SOURCE_BRANCH }}           # e.g., main
          token: ${{ secrets.SOURCE_TOKEN }}          # PAT with Contents:read for the private repo
          path: source

      # 3) Sanity check (helps debug paths quickly)
      - name: List source dir
        run: |
          echo "Listing ./source ..."
          ls -la source
          echo "Looking for file: source/${{ secrets.SOURCE_FILE }}"
          test -f "source/${{ secrets.SOURCE_FILE }}" && echo "Found." || (echo "NOT FOUND"; exit 2)

      # 4) Append next Q&As into the public file
      - name: Append new Q&As
        run: |
          python3 .github/scripts/add_qna.py
        env:
          SOURCE_LOCAL_FILE: source/${{ secrets.SOURCE_FILE }}  # <- read from checked-out private repo
          BATCH_SIZE: ${{ env.BATCH_SIZE }}

      # 5) Commit/push if changed
      - name: Commit changes (if any)
        run: |
          if [[ -n "$(git status --porcelain)" ]]; then
            git config user.name "github-actions[bot]"
            git config user.email "github-actions[bot]@users.noreply.github.com"
            git add -A
            git commit -m "chore: add daily Q&As"
            git push
          else
            echo "Nothing to publish."
          fi
