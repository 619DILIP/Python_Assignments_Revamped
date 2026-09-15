# 02 - How Floci Works

## Goal

Before creating anything, get a clear picture of what Floci actually is and what it isn't - this will make the next three exercises make a lot more sense.

## The Mental Model

Floci is not a fake or scripted version of AWS. It's a real implementation of AWS's own APIs, running entirely on your machine. When you point the AWS CLI at `http://localhost:4566` instead of the real AWS endpoints, the exact same commands, flags, and responses apply - the CLI genuinely can't tell the difference. Some services (like S3) are emulated in-process, and others (like EC2 and RDS) are backed by real Docker containers under the hood, so what you're talking to is closer to "the real thing, running locally" than "a mock."

This matters for two reasons:
- Anything you learn doing this exercise transfers directly to using real AWS later - same commands, same behavior.
- Because nothing here touches a real AWS account, there's no cost risk and no cleanup required on a billing dashboard - just `docker compose down` when you're done.

## Steps

1. **List what's currently running against a completely fresh Floci instance.** With nothing created yet, run:
   ```
   aws --endpoint-url=http://localhost:4566 s3 ls
   aws --endpoint-url=http://localhost:4566 ec2 describe-instances
   aws --endpoint-url=http://localhost:4566 rds describe-db-instances
   ```
   Each of these should return empty responses or no instances or no databases.

2. **Check the health endpoint again**, and this time actually read the response:
   ```
   curl http://localhost:4566/health
   ```
   Note which services show as available. You'll be using `s3`, `ec2`, and `rds` in the next three exercises.

## On Your Own

In a few sentences, answer: what would you expect to be different if you pointed these same three commands at a real AWS account for the first time (instead of Floci)? What would you expect to be the same?

## Submit

Capture screenshot(s) of the three empty-state commands from Step 1, plus your written answer, These screenshots will be included in your final submission ZIP.
