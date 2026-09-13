# 01 - Basic Setup

## Goal

Get Floci running locally and confirm the AWS CLI can actually talk to it before you touch any individual service.

## Steps

1. **Pull the Floci image.**
   ```
   docker pull floci/floci:latest
   ```

2. **Start Floci** using the provided `docker-compose.yml`:
   ```
   docker compose up -d
   ```
   This runs Floci on `http://localhost:4566` - the single endpoint every AWS-shaped service in Floci is reachable through.

3. **Verify it's actually running:**
   ```
   curl http://localhost:4566/_localstack/health
   ```
   You should get back a JSON response listing available services.

4. **Give the AWS CLI dummy credentials.** Floci doesn't check these for validity, but the CLI still requires something to be set:
   ```
   export AWS_ACCESS_KEY_ID=test
   export AWS_SECRET_ACCESS_KEY=test
   export AWS_DEFAULT_REGION=us-east-1
   ```

5. **Confirm the CLI can reach Floci:**
   ```
   aws --endpoint-url=http://localhost:4566 sts get-caller-identity
   ```
   You should get back a fake but valid-looking account identity, not an error.

## On Your Own

Stop Floci (`docker compose down`), then start it again. Run the health check and `get-caller-identity` commands a second time to confirm it comes back up cleanly.

## Submit

A screenshot showing the health check response and the `get-caller-identity` output.
