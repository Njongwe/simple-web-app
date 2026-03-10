markdown
# Architecture Diagram

## System Flow


┌─────────────┐
│  Developer  │
└──────┬──────┘
      │ git push
      ▼
┌─────────────┐
│   GitHub    │
└──────┬──────┘
      │ webhook trigger
      ▼
┌─────────────────┐
│ GitHub Actions  │
│  - Build        │
│  - Test         │
│  - Push to ECR  │
└──────┬──────────┘
      │
      ▼
┌─────────────┐         ┌──────────────┐
│   AWS ECR   │────────▶│   AWS EC2    │
│  (Registry) │  pull   │  (Server)    │
└─────────────┘         └──────┬───────┘
                              │
                              ▼
                       ┌──────────────┐
                       │  End Users   │
                       │  (Browser)   │
                       └──────────────┘

## AWS Infrastructure

- **EC2 Instance:** t3.micro (Free Tier)
- **Security Group:** Allows HTTP (80) and SSH (22)
- **IAM Role:** EC2-ECR-Role with ECR read permissions
- **ECR Repository:** Stores Docker images

## Security

- SSH key-based authentication
- IAM roles for service-to-service communication
- Security groups for network isolation
- Secrets stored in GitHub (not in code)

