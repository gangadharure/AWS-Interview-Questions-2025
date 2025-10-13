
<details>
  <summary><strong>Q246) How would you store and retrieve a database password using AWS Secrets Manager in an EC2 instance?</strong></summary>
  <p>Store the credentials in AWS Secrets Manager using the AWS Console, CLI, or SDK. Attach an IAM role to the EC2 instance with `secretsmanager:GetSecretValue` permission. Use the AWS SDK to retrieve the secret in your application. *(code sample and best practices as provided)*</p>
</details>

