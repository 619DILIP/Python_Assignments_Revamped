# 06 - Bonus: Automating It With Python (Optional)

## Goal

Take a few of the CLI commands you ran by hand in Exercise 03 and wrap them in a small Python script instead. This is meant to be a light touch, not a new topic: it only uses Python's built-in `subprocess` module to run the exact same `aws` CLI commands you already typed manually - **no boto3, no psycopg2, no new libraries** beyond what you already know.

The point isn't to learn a new AWS SDK - it's to see how something you did by hand can be scripted using Python you already know.

## Starter Code

`src/main/automate.py` has TODO blocks that call the same S3 commands from Exercise 03, just from Python instead of your terminal.

## Instructions

1. Open `src/main/automate.py`.
2. Fill in each TODO using `subprocess.run([...])`, passing the same `aws` command and arguments you typed manually in Exercise 03 as a list of strings.
3. Run the script and confirm it produces the same result as doing it by hand - bucket created, file uploaded, contents listed.

## On Your Own

Add one more step to the script: after listing the bucket contents, have it delete the object and the bucket, printing a confirmation message after each step (similar to what you did manually at the end of Exercise 03).

## Submit

Your completed `automate.py` and a screenshot of it running end to end.
