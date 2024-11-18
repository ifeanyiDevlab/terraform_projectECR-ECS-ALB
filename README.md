Deploy Time API to AWS ECS

 

Prerequisites

- Terraform installed

- AWS CLI configured with proper permissions

- Docker image of the time API pushed to ECR

 

 Steps to Deploy

 

1. Clone this repository.

2. Push docker image to ECR and update image to ECS through task definition.

3. Initialize Terraform:

 

   Bash è

  Terraform init

Terraform validate

Terraform plan

Terraform apply

 

The last bash after creating the infrastructure outputs URL of the Application Loader Balancer. Which is to be used to access the applications content on a web browser.

 

 
