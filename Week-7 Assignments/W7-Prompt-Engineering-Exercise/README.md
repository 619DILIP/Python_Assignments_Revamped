# 🏆 Prompt Engineering Exercise

## Overview

This assignment is designed to help you practice zero-shot vs. multi-shot prompting by extracting structured information from unstructured customer support messages.

## Instructions

1. Open it in VS Code.

2. Write your three prompt versions inside `src/main/lab.py` - see the TO DO blocks for what each needs to cover.

3. For each prompt version, paste the prompt plus a sample message into your AI assistant's chat, then paste the response back into the matching `RESULTS` block in `lab.py`. Do this for at least 2 of the 5 sample messages per version (6 model calls total).

4. Run `lab.py` - it prints your saved results side by side so you can compare the three versions.

5. Take a screenshot of your output, add it to the assignment folder along with your written comparison (see below), and compress the whole folder into a zip file for submission.

## Notes

- The 5 sample customer messages are provided inside `src/data/support_messages.json`.
- You're writing three prompt versions (zero-shot, multi-shot, constrained) - see the TO DO blocks in `lab.py` for what each needs to cover.
- If you have your own API access and would rather call a model programmatically instead of pasting into a chat window, that's fine too - `call_model()` in `lab.py` is there for that path. It's optional, not required.
- Along with your code, submit a short written comparison covering which version performed most consistently and why, plus one thing you'd change if you did this again.


