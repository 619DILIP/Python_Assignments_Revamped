# Inventory Dashboard: Optimize

## Overview

This is the same inventory dashboard from the refactor assignment, now running at scale. It's a separately-built, already-correct copy, not your own fixed version from that assignment, so it doesn't matter how that one turned out. It's seeded with roughly 300,000 items instead of a couple dozen, and one endpoint is deliberately slow. Use GitHub Copilot in the IDE to understand why it's slow before you fix it, not just to make it faster.

## Setup

Install dependencies once:

```
pip install -r requirements.txt
```

You'll run two processes at a time and keep both terminals open while you work.

**Backend:**

```
cd backend
uvicorn main:app --reload --port 8000
```

**Frontend, in a second terminal:**

```
cd frontend
python -m http.server 5500
```

Then open `http://127.0.0.1:5500` in your browser. The database seeds itself on first run and may take a moment the first time.

## Using GitHub Copilot without paying for it

Copilot's free plan (2,000 completions and 50 chat requests a month, no card needed) is enough for this assignment if you're targeted about what you ask rather than burning requests on trial and error.

- During setup, GitHub sometimes offers a 30-day free trial of Copilot Pro. Skip it. Stay on the plain Free plan unless you already know you want Pro afterward, since the trial converts to a paid subscription automatically.
- If you're a verified student, GitHub's Student Developer Pack includes Copilot Pro at no cost, which removes the 50-request cap. Worth checking if you're eligible, but not required.

## Instructions

1. Time the `/api/summary` endpoint as it currently stands. This is your baseline. A simple way:

   ```
   curl -w "\nTime: %{time_total}s\n" -o /dev/null -s http://127.0.0.1:8000/api/summary
   ```

2. Ask Copilot to explain why the endpoint is slow, not just to make it faster. You should be able to describe the actual reason in your own words before you touch the code.
3. Apply the fix. Don't change what the endpoint returns, only how it gets there.
4. Re-time it and compare to your baseline. You should see a clear, repeatable improvement.
5. Construct one edge case yourself, such as a category with zero items, and confirm the optimized version handles it the same way the original did.
6. If you get stuck anywhere in this process, using AI is fine, expected even. Just do it properly: understand what it's telling you instead of taking it on faith. You're meant to do this job with AI's help, not hand the job to AI. Lean on it too hard and the only thing you're shortchanging is your own learning.

## Submission

Write up:

- Your baseline and optimized timings, and the slowdown's cause in your own words.
- What Copilot suggested, what you accepted, and what you changed or rejected.

Take a screenshot of your before/after timings, add it to this folder along with your write-up, and compress the whole folder into a zip. If you created a virtual environment (`.venv`) while working, remove it before zipping.