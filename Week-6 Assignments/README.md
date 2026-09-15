# Hands-On with Floci

## Overview

This is a series of small, sequential exercises to get real hands-on time with [Floci](https://floci.io), the free, open-source local AWS emulator - done through the CLI directly, no Python required until the very end. Work through them in order.

## What's Inside

1. **01-Basic-Setup** - get Floci running and confirm the AWS CLI can talk to it
2. **02-How-Floci-Works** - understand the mental model before touching any real service
3. **03-S3-Hands-On** - create a bucket, upload/download/list/delete objects, try versioning
4. **04-EC2-Hands-On** - launch, inspect, and stop/terminate an emulated EC2 instance
5. **05-RDS-Hands-On** - stand up a database, connect with `psql`, run SQL directly (includes a short primer, since psql hasn't come up before this)
6. **06-Bonus-Python-Automation** - script parts of what you just did by hand, using only Python's built-in `subprocess` module to call the same AWS CLI commands - no new libraries needed
7. **07-IAM-Hands-On** - create and attach IAM users, roles, and policies through the CLI

## Prerequisites

- Docker installed and running
- AWS CLI installed
- Completion of the Local AWS Environment module

## Final Submission

Complete all seven exercises in order and collect the required screenshot(s) from each exercise.

At the end, organize your screenshots and compress them into **one ZIP file** for submission.

Your ZIP file should contain the evidence for all seven exercises:

```text
Floci-Hands-On-Submission.zip
│
├── 01-Basic-Setup/
│   └── screenshot(s)
│
├── 02-How-Floci-Works/
│   └── screenshot(s)
│
├── 03-S3-Hands-On/
│   └── screenshot(s)
│
├── 04-EC2-Hands-On/
│   └── screenshot(s)
│
├── 05-RDS-Hands-On/
│   └── screenshot(s)
│
├── 06-Bonus-Python-Automation/
│   └── automate.py
    └── screenshot(s)
│
└── 07-IAM-Hands-On/
    └── screenshot(s)
```