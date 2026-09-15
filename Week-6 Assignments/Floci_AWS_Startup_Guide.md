# Floci AWS Emulator - Startup Guide

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

## Troubleshooting

### Error: "Unable to locate credentials"
Make sure you ran `floci env | Invoke-Expression` (PowerShell) or `eval "$(floci env)"` (Git Bash) in your current terminal session.

### Error: "aws: command not found"
AWS CLI is not installed or not in PATH. Run `pip install --upgrade awscli` and restart your terminal.