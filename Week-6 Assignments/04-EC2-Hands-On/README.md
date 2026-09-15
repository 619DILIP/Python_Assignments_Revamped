# 04 - Setting Up and Using EC2

## Goal

Launch, inspect, and tear down an EC2 instance on Floci. Floci's EC2 emulation is backed by real Docker containers, so `run-instances` genuinely starts a container on your machine - this isn't a fake response.

## Steps

1. **Create a key pair:**
   ```
   aws --endpoint-url=http://localhost:4566 ec2 create-key-pair \
     --key-name floci-key --query 'KeyMaterial' --output text > floci-key.pem
   ```

2. **Launch an instance:**
   ```
   INSTANCE_ID=$(aws --endpoint-url=http://localhost:4566 ec2 run-instances \
     --image-id ami-000000000001 \
     --instance-type t3.micro \
     --key-name floci-key \
     --query 'Instances[0].InstanceId' --output text)
   echo "Launched: $INSTANCE_ID"
   ```

3. **Describe it** to see its current state and details:
   ```
   aws --endpoint-url=http://localhost:4566 ec2 describe-instances --instance-ids $INSTANCE_ID
   ```

4. **Confirm it's a real container**, not just an API response:
   ```
   docker ps | grep floci
   ```
   You should see a container corresponding to your instance.

5. **Stop, then start it again:**
   ```
   aws --endpoint-url=http://localhost:4566 ec2 stop-instances --instance-ids $INSTANCE_ID
   aws --endpoint-url=http://localhost:4566 ec2 start-instances --instance-ids $INSTANCE_ID
   ```

6. **Terminate it:**
   ```
   aws --endpoint-url=http://localhost:4566 ec2 terminate-instances --instance-ids $INSTANCE_ID
   ```

## On Your Own

Launch a second instance, this time passing `--user-data` with a short shell script (for example, one that echoes a message to a file). After it's running, check `docker logs` for that instance's container and confirm your user-data script actually ran.

## Submit

Capture screenshot(s) of the instance launching, the `docker ps` confirmation, and the user-data task showing your script's output in the container logs, These screenshots will be included in your final submission ZIP.
