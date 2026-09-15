# 07 - Setting Up and Using IAM

## Goal

Practice creating and attaching IAM users, roles, and policies through the CLI on Floci.

## A Heads-Up Before You Start

Floci's IAM support is real but marked "partial," and policy *enforcement* is opt-in and off by default. That means creating a narrow, correctly-scoped policy versus an overly broad one won't actually behave differently here - both would work the same way. So this exercise is about practicing the correct real-world pattern for creating and attaching IAM resources, the same commands and JSON shape you'd use against real AWS, not about watching access actually get denied.

## Steps

1. **Create an IAM user:**
   ```
   aws --endpoint-url=http://localhost:4566 iam create-user --user-name candidate-user
   ```

2. **Create a policy** using the least-privilege example provided (`src/setup/read-only-s3-policy.json`), which grants read-only access to a single bucket rather than broad S3 access:
   ```
   aws --endpoint-url=http://localhost:4566 iam create-policy \
     --policy-name CandidateReadOnlyS3 \
     --policy-document file://src/setup/read-only-s3-policy.json
   ```
   Note the `Arn` returned in the output - you'll need it in the next step.

3. **Attach the policy to your user:**
   ```
   aws --endpoint-url=http://localhost:4566 iam attach-user-policy \
     --user-name candidate-user \
     --policy-arn <arn-from-step-2>
   ```

4. **Confirm the attachment:**
   ```
   aws --endpoint-url=http://localhost:4566 iam list-attached-user-policies --user-name candidate-user
   ```

5. **Create a role** (the kind a service like Lambda would assume, rather than a person):
   ```
   aws --endpoint-url=http://localhost:4566 iam create-role \
     --role-name candidate-service-role \
     --assume-role-policy-document '{"Version":"2012-10-17","Statement":[{"Effect":"Allow","Principal":{"Service":"lambda.amazonaws.com"},"Action":"sts:AssumeRole"}]}'
   ```

6. **Describe the role** to confirm it was created correctly:
   ```
   aws --endpoint-url=http://localhost:4566 iam get-role --role-name candidate-service-role
   ```

## On Your Own

Write your own second policy - this time granting write access (`s3:PutObject`) to the same bucket, scoped only to objects under a `uploads/` prefix (hint: the resource ARN can include a wildcard, e.g. `arn:aws:s3:::candidate-practice-bucket/uploads/*`). Create it and attach it to `candidate-user` alongside the read-only policy, then list the user's attached policies again to confirm both are there.

## Submit

Capture screenshot(s) of Steps 1–6, plus a screenshot of your own write-access policy JSON and the final `list-attached-user-policies` output showing both policies attached, These screenshots will be included in your final submission ZIP.
