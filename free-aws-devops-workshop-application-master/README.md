# Workshop-1 Application Deployment Guide

This repository contains the application code, Docker configuration, and GitHub Actions workflow for building and deploying a simple web application to Amazon ECS. The application serves a basic HTML page that displays a customizable message.

The configurations provided here are intended for educational purposes and do not encompass all DevOps best practices. They serve as an introductory guide to Terraform and AWS workshops. We plan to cover improvements, more sophisticated practices, and deeper insights into Terraform and AWS in future DevOps sessions.

## Contents

- `app.py`: Python web server application.
- `Dockerfile`: Docker configuration file to build the application's container image.
- `build-deploy.yaml`: GitHub Actions workflow for automating the build and deployment process to Amazon ECS.
- `.aws/task-definition.json`: ECS task definition template that needs to be populated with your configuration.

## Prerequisites

Before proceeding with the deployment, ensure you have:

- An AWS account with the necessary permissions to create and manage ECS resources.
- A GitHub account to fork this repository and set up GitHub Actions.
- Docker installed on your local machine for testing purposes (optional).
- **The infrastructure created as per the guide in the [INFRALESS-IO free-aws-devops-workshop-terraform repository](https://github.com/INFRALESS-IO/free-aws-devops-workshop-terraform).** This is required to have the necessary AWS resources (ECS cluster, ECR repository, etc.) ready for the deployment of this application.

## Fetching the ECS Task Definition

To prepare your ECS task definition, navigate to the Amazon ECS console within your AWS account. Select the relevant cluster and then view the task definitions. You can create a new task definition or modify an existing one. After configuring your task definition, download or copy its JSON representation into the `.aws/task-definition.json` file in your project.

### Updating the Task Definition's Environment Variable

The `app.py` uses an environment variable `HELLO_WORLD_TEXT` to customize the greeting message displayed on the web page. You can test different greetings by updating this environment variable in the task definition:

1. Open your task definition JSON file.
2. Find the `environment` section under the container definitions.
3. Add or modify the `HELLO_WORLD_TEXT` environment variable with your desired greeting message.

For example:

```json
"environment": [
    {
        "name": "HELLO_WORLD_TEXT",
        "value": "Hello, Workshop!"
    }
]
```

Commit and push the updated task definition file if you've made changes.


## Deployment Steps

### Step 1: Fork and Clone the Repository

Fork this repository to your GitHub account and clone it to your local machine for any modifications.

### Step 2: Set Up AWS Credentials

Configure your AWS credentials as GitHub Secrets in the repository settings:

- `AWS_ACCESS_KEY_ID`: Your AWS access key ID.
- `AWS_SECRET_ACCESS_KEY`: Your AWS secret access key.

These credentials are used by GitHub Actions to authenticate with AWS for deploying the application.

### Step 3: Prepare the ECS Task Definition

Populate the `.aws/task-definition.json` file with your ECS task definition content. This JSON defines the configuration of your application within ECS, including the Docker image to use, CPU and memory allocations, and required environment variables.

### Step 4: Customize the Application (Optional)

You can modify the `app.py` file to change the HTML content or the environment variable used for the customizable message. If you make changes, commit and push them to your repository.

### Step 5: Deploy the Application

The `build-deploy.yaml` GitHub Actions workflow is triggered on a push to the `master` branch. It automates the following tasks:

1. **Checkout**: Checks out the repository code to the GitHub Actions runner.
2. **Configure AWS credentials**: Sets up AWS credentials using the secrets configured in the repository settings.
3. **Login to Amazon ECR**: Authenticates the GitHub Actions runner with Amazon ECR to enable pushing Docker images.
4. **Build, tag, and push image to Amazon ECR**: Builds the Docker image from the `Dockerfile`, tags it, and pushes it to the specified ECR repository.
5. **Fill in the new image ID in the Amazon ECS task definition**: Updates the ECS task definition with the new Docker image ID.
6. **Deploy Amazon ECS task definition**: Deploys the updated task definition to the specified ECS service, updating the running application.

Monitor the GitHub Actions tab to check the status of the deployment workflow.

### Step 6: Access the Application

Once deployed, access the application using the public IP or domain name associated with your ECS service's load balancer. The application will display a greeting message.

## Dockerfile Explained

The `Dockerfile` includes the following steps:

- **FROM**: Uses the official Python 3.9 slim image as the base.
- **WORKDIR**: Sets the working directory inside the container to `/app`.
- **COPY**: Copies the application files from your project directory into the container.
- **EXPOSE**: Makes port 8000 available to the outside of the container.
- **CMD**: Specifies the command to run `app.py` when the container starts.

## Reporting Issues or Suggestions

If you encounter any problems or have suggestions for improvements, please use the GitHub Issues tab of this repository. We welcome your feedback to enhance the application.

## AWS Billing and Resource Management Notice

Monitoring your AWS billing and managing resources is crucial to avoid unnecessary costs. Remember to clean up resources that you no longer need. We are not responsible for any financial or data loss due to resource mismanagement.

## Join Our Community

For more information and updates on future workshops, join our [AWS & DevOps Academy WhatsApp Group](https://chat.whatsapp.com/I6UjXJYlrl2JXfhGFniOZX).
