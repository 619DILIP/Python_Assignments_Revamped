import subprocess

ENDPOINT = "http://localhost:4566"
BUCKET_NAME = "candidate-automation-bucket"
FILE_PATH = "sample-file.txt"


def run_command(command):
    """Runs a command (given as a list of strings) and prints its output."""
    result = subprocess.run(command, capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print("Error:", result.stderr)
    return result


def main():
    # TO DO: Create the bucket
    # Your task: build the same "aws s3 mb" command you ran by hand in
    # Exercise 03, as a list of strings, and pass it to run_command().
    # Example shape: ["aws", "--endpoint-url=" + ENDPOINT, "s3", "mb", ...]

    # TO DO: Upload the sample file
    # Your task: same idea, using "aws s3 cp" to upload FILE_PATH into the
    # bucket you just created.

    # TO DO: List the bucket's contents
    # Your task: use "aws s3 ls" to confirm the upload worked, and print
    # the result.

    print("\n✅ Automation Run Completed!")


if __name__ == "__main__":
    main()
