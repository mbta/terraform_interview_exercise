# Terraform Interview Exercise

## Objective

Use Terraform and LocalStack to configure a Lambda function and function URL.

## Prerequisites

All can be installed via [Homebrew](https://brew.sh/) on macOS or Linux

- [Python](https://www.python.org/downloads/): `brew install python@3.11`
- Docker CLI: `brew install docker`
- [Colima](https://github.com/abiosoft/colima): `brew install colima` (likely only needed on macOS)
- [Localstack](https://docs.localstack.cloud/getting-started/installation/): `brew install localstack`
- [Terraform](https://developer.hashicorp.com/terraform/downloads): `brew install terraform`

## Steps

1. Make sure Docker (or Colima) is running
1. Start LocalStack:

   ```bash
   $ localstack start
   ```

1. Initialize a Terraform root module in this directory
1. Add resources:
   - A [Lambda function](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/lambda_function) that runs the Python code contained in the `lambda/` directory
   - A [Lambda function URL](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/lambda_function_url) for the function
1. Validate, plan, and apply your changes
1. Get the URL of the Lambda function you created
1. Call the Lambda function using `curl` and observe its output
1. Destroy the running infrastructure

## Sources/Inspiration

- https://www.tinfoilcipher.co.uk/2022/05/14/simulating-aws-terraform-builds-with-localstack/
- https://docs.localstack.cloud/user-guide/integrations/terraform/
