
# Currency Converter

![alt text](https://github.com/Bryan-Campuzano/Currency-Converter/blob/main/Green%20Simple%20Money%20Investment%20Tips%20YouTube%20Thumbnail.png)

This project provides a simple implementation of a currency converter deployed using AWS Lambda and Terraform. It is designed for practicing DevOps workflows.

## Features

- Currency conversion using real-time exchange rates.
- AWS Lambda function triggered by API Gateway.
- Terraform scripts to deploy the infrastructure.

## Prerequisites

- AWS account.
- Terraform installed.
- AWS CLI configured.

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Bryan-Campuzano/Currency-Converter.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Currency-Converter
   ```
3. Initialize Terraform:
   ```bash
   terraform init
   ```
4. Deploy the infrastructure:
   ```bash
   terraform apply
   ```

## Usage

After deployment, the Lambda function can be accessed via the generated API Gateway URL. You can send currency conversion requests using the following format:

```bash
curl -X GET "https://your-api-gateway-url/convert?from=USD&to=EUR&amount=100"
```

## Cleanup

To remove the infrastructure, run:
```bash
terraform destroy
```

## Purpose 

this is an academic proyect of my devops engineer's practics at Globant.