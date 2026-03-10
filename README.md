markdown
# Simple Web Application with CI/CD Pipeline

## Project Overview
A Python Flask web application deployed on AWS EC2 with automated CI/CD pipeline using GitHub Actions.

## Technologies Used
- **Application:** Python, Flask
- **Containerization:** Docker
- **Cloud Provider:** AWS (EC2, ECR)
- **CI/CD:** GitHub Actions
- **Infrastructure:** AWS Security Groups, IAM Roles

## Architecture

Developer → GitHub → GitHub Actions → AWS ECR → AWS EC2

## Features
- Automated deployment on code push
- Containerized application using Docker
- Secure AWS infrastructure
- Health check endpoint

## Deployment Process
1. Code pushed to GitHub main branch
2. GitHub Actions triggered automatically
3. Docker image built and pushed to AWS ECR
4. Application deployed to EC2 instance
5. Live website updated with zero downtime

## Skills Demonstrated
- CI/CD pipeline implementation
- Docker containerization
- AWS cloud services (EC2, ECR, IAM)
- Infrastructure security (Security Groups)
- Version control with Git
- Automated deployment workflows

## Live Demo
Application URL: http://13.221.207.189

## Setup Instructions
See [SETUP.md](SETUP.md) for detailed setup instructions.

## Author
NITCHEU SHOKOLEU OLIVER NJONGWE - DevOps Student

## Project Date
March 2026
