# 🏆 Optimize a Script Using AI Tooling

## Overview

This assignment is designed to help you practice the baseline → analyze → apply → test → re-benchmark workflow for using an AI tool to optimize slow code.

## Instructions

1. Open it in VS Code with your AI pair-programming tool enabled.

2. Run `src/main/lab.py` as-is first and record how long it takes - this is your baseline, before you change anything.

3. Ask your AI tool to analyze the script and explain why it's slow, not just "make it faster." Apply the suggested change inside `lab.py`, then re-run and confirm it still finds the exact same duplicates as the original.

4. Time the optimized version and compare it to your baseline. Then construct one edge case yourself (e.g. an empty file, or a file with one ID) and confirm both versions handle it identically.

5. Take a screenshot of your baseline and optimized timings side by side, write up the AI tool's explanation in your own words, add both to the assignment folder, and compress the whole folder into a zip file for submission.

## Notes

- The sample dataset is provided inside `src/data/customer_ids.csv` - 5,000 customer IDs with roughly 1,000 duplicates deliberately mixed in.
- `lab.py` contains a working but deliberately inefficient (O(n²)) duplicate-detection function. Don't change what it returns, just how it gets there.


