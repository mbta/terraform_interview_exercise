# Terraform Interview Exercise

## Objective

Use Terraform and LocalStack to configure a Lambda function and function URL. LocalStack acts as a stand-in for AWS, there's no need an AWS account or access keys. The initial configuration in main.tf configures Terraform to make calls to the LocalStack container.

## Prerequisites

All can be installed via [Homebrew](https://brew.sh/) on macOS or Linux

- [Python](https://www.python.org/downloads/): `brew install python@3.11`
- Docker CLI: `brew install docker`
- [Colima](https://github.com/abiosoft/colima): `brew install colima` (likely only needed on macOS)
- [Localstack](https://docs.localstack.cloud/getting-started/installation/): `brew install localstack`
- [Terraform](https://developer.hashicorp.com/terraform/downloads): `brew install terraform`

Note that the LocalStack Python package must be installed on your host machine &ndash; running only the LocalStack Docker container is not sufficient to complete this exercise. 

## Steps

### 1. Initialization

1. Make sure Docker (or Colima) is running
1. Start LocalStack:

   ```bash
   $ localstack start
   ```

1. Clone this repo to a local working directory
1. Initialize a Terraform root module within the repo directory

### 2. Add Lambda Function

1. Write Terraform configuration for a [Lambda function](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/lambda_function) that runs the Python code contained in the `lambda/` directory
1. Validate, plan, and apply your changes

### 3. Add Lambda Function URL

1. Write Terraform configuration for a [Lambda function URL](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/lambda_function_url) for the function you created
1. Validate, plan, and apply your changes

### 4. Testing &amp; Teardown

1. Get the URL of the Lambda function you created
1. Call the Lambda function using `curl` and observe its output
1. Destroy the running infrastructure

## Sources/Inspiration

- https://www.tinfoilcipher.co.uk/2022/05/14/simulating-aws-terraform-builds-with-localstack/
- https://docs.localstack.cloud/user-guide/integrations/terraform/
