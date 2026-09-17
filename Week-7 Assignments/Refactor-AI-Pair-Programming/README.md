# Inventory Dashboard: Fix and Refactor

## Overview

This app is a small inventory dashboard: a FastAPI backend and a plain HTML/JS frontend, talking to each other over two separate local processes. It's broken in six places, spread across the backend, the frontend, and the contract between them. You have not built anything with this stack before, which is the point. Use GitHub Copilot in the IDE to find and understand each problem, not just to apply a fix you already knew.

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

Then open `http://127.0.0.1:5500` in your browser. The database seeds itself on first run.

## Using GitHub Copilot without paying for it

Copilot's free plan (2,000 completions and 50 chat requests a month, no card needed) is enough for this assignment if you're targeted about what you ask rather than burning requests on trial and error.

- During setup, GitHub sometimes offers a 30-day free trial of Copilot Pro. Skip it. Stay on the plain Free plan unless you already know you want Pro afterward, since the trial converts to a paid subscription automatically.
- If you're a verified student, GitHub's Student Developer Pack includes Copilot Pro at no cost, which removes the 50-request cap. Worth checking if you're eligible, but not required.

## Instructions

1. Read through `backend/main.py` and `frontend/app.js` yourself first. Note down what you notice before you bring in Copilot.
2. Open the project folder in VS Code with Copilot enabled. Start the app (see Setup above), splitting your terminal into two panes, one for the backend, one for the frontend and see what actually breaks in the browser.
3. Use Copilot to find and fix each issue. Apply changes one at a time and re-test in the browser after each, rather than making every change at once and hoping.
4. At least one of the issues only shows up when you check the browser's console or network tab, not from reading the code alone. Make sure you've found and fixed that kind before considering this done.
5. Push back on at least one Copilot suggestion, either rejecting it or asking it to explain before you accept it.
6. If you get stuck anywhere in this process, using AI is fine, expected even. Just do it properly: understand what it's telling you instead of taking it on faith. You're meant to do this job with AI's help, not hand the job to AI. Lean on it too hard and the only thing you're shortchanging is your own learning.

You'll know you're done when the dashboard loads in the browser with a correct category summary table and a low-stock list that's actually filtered by quantity, not by price.

## Submission

Write up:

- What you noticed yourself before using Copilot.
- What Copilot suggested, what you accepted, and what you changed or rejected.
- Any suggestions you pushed back on or questioned, and why? OR if you did not push back on any suggestions, why not?

Take a screenshot of the working dashboard, add it to this folder along with your write-up, and compress the whole folder into a zip. If you created a virtual environment (`.venv`) while working, remove it before zipping.
