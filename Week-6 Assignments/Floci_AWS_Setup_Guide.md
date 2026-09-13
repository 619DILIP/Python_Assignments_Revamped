# Floci AWS Emulator Quick Start Guide

## Prerequisites
- Docker installed and running
- Python 3 installed (for AWS CLI)

---

## Step 1: Install Floci CLI

Floci is a local AWS emulator that runs in Docker. It simulates AWS services so you can test code locally without hitting real AWS.

### PowerShell
```powershell
irm https://floci.io/install.ps1 | iex
```

### Git Bash / WSL
```bash
curl https://floci.io/install.sh | bash
```

---

## Step 2: Install AWS CLI

The AWS CLI is a command-line tool that lets you interact with AWS services. When pointed at Floci, it talks to your local emulator instead of the real cloud.

### PowerShell or Git Bash
```bash
pip install --upgrade awscli
```

Verify installation:
```bash
aws --version
```

---

## Step 3: Start Floci & Set Environment Variables

`floci start` launches the AWS emulator in a Docker container. The `floci env` command outputs environment variables that tell the AWS CLI where to connect (localhost:4566 instead of AWS's real servers).

### PowerShell
```powershell
floci start
floci env | Invoke-Expression
```

### Git Bash / WSL
```bash
floci start
eval "$(floci env)"
```

Verify setup:
```bash
echo $env:AWS_ENDPOINT_URL    # PowerShell
echo $AWS_ENDPOINT_URL         # Git Bash
```

---

## Step 4: Create an S3 Bucket

S3 is AWS's object storage service. A bucket is like a container for storing files. `mb` stands for "make bucket".

```bash
aws s3 mb s3://my-bucket
```

List buckets to verify:
```bash
aws s3 ls
```

---

## Step 5: Upload a File

This demonstrates uploading a file (called an "object" in S3) to your bucket.

### Create a test file

**PowerShell:**
```powershell
"Why pay for S3 when floci is free? 🎉" | Out-File hello-floci.txt
```

**Git Bash:**
```bash
echo "Why pay for S3 when floci is free? 🎉" > hello-floci.txt
```

### Upload to S3
```bash
aws s3 cp hello-floci.txt s3://my-bucket/hello-floci.txt
```

---

## Step 6: List Objects in Bucket

View all files stored in your bucket.

```bash
aws s3 ls s3://my-bucket/
```

---

## Step 7: Download a File

Retrieve a file from S3 to your local machine. `cp` means "copy" - you're copying from cloud to local.

```bash
aws s3 cp s3://my-bucket/hello-floci.txt ./hello-floci-download.txt
```

---

## Step 8: Modify & Re-Upload a File

S3 doesn't allow direct editing. You download, edit locally, then re-upload to replace the original.

### Download the file
```bash
aws s3 cp s3://my-bucket/hello-floci.txt ./hello-floci.txt
```

### Edit the file
**PowerShell:**
```powershell
notepad ./hello-floci.txt
```

**Git Bash:**
```bash
nano hello-floci.txt
```

### Re-upload (overwrites the original)

Re-uploading with the same filename replaces the old version (assuming versioning is off).

```bash
aws s3 cp ./hello-floci.txt s3://my-bucket/hello-floci.txt
```

---

## Step 9: Delete a File

Permanently remove a file from the bucket. `rm` means "remove".

```bash
aws s3 rm s3://my-bucket/hello-floci.txt
```

---

## Step 10: Delete a Bucket

Delete the entire bucket. `rb` means "remove bucket". A bucket must be empty before deletion (unless you use `--force`).

```bash
aws s3 rb s3://my-bucket
```

To force delete a non-empty bucket:
```bash
aws s3 rb s3://my-bucket --force
```

---

## Common Commands Reference

| Task | Command |
|------|---------|
| List buckets | `aws s3 ls` |
| List bucket contents | `aws s3 ls s3://my-bucket/` |
| Upload file | `aws s3 cp ./file s3://my-bucket/file` |
| Download file | `aws s3 cp s3://my-bucket/file ./file` |
| Upload directory (recursive) | `aws s3 cp ./dir s3://my-bucket/ --recursive` |
| Sync local to S3 | `aws s3 sync ./dir s3://my-bucket/` |
| Delete file | `aws s3 rm s3://my-bucket/file` |
| Delete bucket (empty) | `aws s3 rb s3://my-bucket` |
| Delete bucket (force) | `aws s3 rb s3://my-bucket --force` |

---

## Troubleshooting

### Error: "Unable to locate credentials"
Make sure you ran `floci env | Invoke-Expression` (PowerShell) or `eval "$(floci env)"` (Git Bash) in your current terminal session.

### Error: "aws: command not found"
AWS CLI is not installed or not in PATH. Run `pip install --upgrade awscli` and restart your terminal.

### File created multiple versions instead of overwriting
Your bucket has versioning enabled. To suspend versioning:
```bash
aws s3api put-bucket-versioning --bucket my-bucket --versioning-configuration Status=Suspended
```

---

## Next Steps

- Explore other AWS services: DynamoDB, Lambda, SQS, SNS, etc.
- Use Floci for local development and testing
- Integrate with your CI/CD pipeline
