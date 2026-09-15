# 03 - Setting Up and Using S3

## Goal

Create a real S3 bucket on Floci and practice the core operations: upload, list, download, delete.

## Steps

1. **Create a bucket:**
   ```
   aws --endpoint-url=http://localhost:4566 s3 mb s3://candidate-practice-bucket
   ```

2. **Upload the sample file** (provided at `src/data/sample-file.txt`):
   ```
   aws --endpoint-url=http://localhost:4566 s3 cp src/data/sample-file.txt s3://candidate-practice-bucket/
   ```

3. **List the bucket's contents** to confirm the upload:
   ```
   aws --endpoint-url=http://localhost:4566 s3 ls s3://candidate-practice-bucket/
   ```

4. **Download it back** under a different name, and open it to confirm the content matches:
   ```
   aws --endpoint-url=http://localhost:4566 s3 cp s3://candidate-practice-bucket/sample-file.txt downloaded-copy.txt
   ```

5. **Delete the object, then the bucket:**
   ```
   aws --endpoint-url=http://localhost:4566 s3 rm s3://candidate-practice-bucket/sample-file.txt
   aws --endpoint-url=http://localhost:4566 s3 rb s3://candidate-practice-bucket
   ```

## On Your Own

Create a second bucket, this time with **versioning enabled**:
```
aws --endpoint-url=http://localhost:4566 s3 mb s3://candidate-versioning-bucket
aws --endpoint-url=http://localhost:4566 s3api put-bucket-versioning \
  --bucket candidate-versioning-bucket --versioning-configuration Status=Enabled
```
Upload the same file twice with different content each time (edit `sample-file.txt` between uploads), then list all versions:
```
aws --endpoint-url=http://localhost:4566 s3api list-object-versions --bucket candidate-versioning-bucket
```

## Submit

Capture screenshot(s) of the full Steps 1–5 sequence, plus a screenshot of the versioning task showing two versions of the same file listed, These screenshots will be included in your final submission ZIP.
