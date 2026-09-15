# Full-Stack Inventory Dashboard: Debug and Optimize

## Overview

This is one assignment in two phases, using AI coding assistance in the IDE (GitHub Copilot) rather than a chat window. The app is a small inventory dashboard: a FastAPI backend and a plain HTML/JS frontend, talking to each other over two separate local processes. You have not built anything with this stack before, which is the point. You'll need to lean on Copilot to understand what's going wrong and why, not just apply a fix you already knew.

Submit one write-up covering both phases (see the end of this file for what to include), along with your patched code from both folders.

## Setup

From this folder, install dependencies once:

```
pip install -r requirements.txt
```

Each phase has its own backend and frontend. You'll run two processes at a time: the API on port 8000 and the static frontend on port 5500. Keep both terminals open while you work.

Backend:

```
cd phase-1-broken-app/backend
uvicorn main:app --reload --port 8000
```

Frontend, in a second terminal:

```
cd phase-1-broken-app/frontend
python -m http.server 5500
```

Then open http://127.0.0.1:5500 in your browser. The database seeds itself on first run.

## Using GitHub Copilot without paying for it

Copilot's free plan (2,000 completions and 50 chat requests a month, no card needed) is enough for this assignment if you use it with some intent rather than burning requests on trial and error. A few things to know going in:

- During setup, GitHub sometimes offers a 30-day free trial of Copilot Pro. Skip it. Stay on the plain Free plan unless you already know you want to pay for Pro afterward, since the trial converts to a paid subscription automatically.
- If you're a verified student, GitHub's Student Developer Pack includes Copilot Pro at no cost, which removes the 50-request cap. Worth checking if you're eligible, but not required for this assignment.
- Budget your chat requests. You should be able to get through both phases well within the free limit if you're targeted about what you ask.

## Phase 1: Fix the broken app (phase-1-broken-app/)

The app has six intentional problems spread across the backend, the frontend, and the contract between them. Some of them won't show up until both processes are running and you're actually looking at the browser console and network tab, not just reading the code.

1. Read through backend/main.py and frontend/app.js yourself first. Note down what you notice before you bring in Copilot.
2. Open both folders in VS Code with Copilot enabled. Start the app (see Setup above) and see what actually breaks in the browser.
3. Use Copilot to find and fix each issue. Apply changes one at a time and re-test in the browser after each, rather than making every change at once and hoping.
4. At least one of the issues only shows up when you check the browser's console or network tab, not from reading the code alone. Make sure you've found and fixed that kind before considering this phase done.
5. Push back on at least one Copilot suggestion, either rejecting it or asking it to explain before you accept it.

You'll know Phase 1 is done when the dashboard loads in the browser with a correct category summary table and a low-stock list that's actually filtered by quantity, not by price.

## Phase 2: Optimize a slow endpoint (phase-2-optimize/)

This is a separate, already-correct copy of the same app, not your Phase 1 output. It's seeded with roughly 300,000 items instead of a couple dozen, and one endpoint is deliberately slow.

1. Start this version the same way (see Setup above, same ports are fine since Phase 1 should no longer be running).
2. Time the /api/summary endpoint as it currently stands. This is your baseline. A simple way:

```
curl -w "\nTime: %{time_total}s\n" -o /dev/null -s http://127.0.0.1:8000/api/summary
```

3. Ask Copilot to explain why the endpoint is slow, not just to make it faster. You should be able to describe the actual reason in your own words before you touch the code.
4. Apply the fix. Don't change what the endpoint returns, only how it gets there.
5. Re-time it and compare to your baseline. You should see a clear, repeatable improvement.
6. Construct one edge case yourself, such as a category with zero items, and confirm the optimized version handles it the same way the original did.

## Write-up (submit with both phases)

- What you noticed yourself before using Copilot, in both phases.
- What Copilot suggested, what you accepted, and what you changed or rejected.
- The one suggestion you pushed back on or questioned, and why.
- Your baseline and optimized timings for Phase 2, plus the slowdown's cause in your own words.

Take screenshots of the working dashboard (Phase 1) and your before/after timings (Phase 2), add them to this folder, and compress the whole assignment folder into a zip for submission. If you created a virtual environment (.venv) while working, remove it before zipping.