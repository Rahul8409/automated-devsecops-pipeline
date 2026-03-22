# Automated DevSecOps Pipeline (Local Environment)

## Project Overview
This project demonstrates the design and implementation of an automated DevSecOps pipeline using Infrastructure as code (Iac) concepts in a local environment.

The pipeline automates buliding, security scanning, and validation of a containerized application.

---

## Technologies used 
- Python (Flask)
- Docker
- GitHub Actions (CI/CD)
- Trivy (Security Scanning)
- Linux (WSL)

---

## Project Workflow
1. Developer pushes code to GitHub
2. GitHub Actions triggers CI pipeline 
3. Docker image is bulit automatically
4. Trivy scans the image for vulnerabilities 
5. Pipeline reports security status

---

## Security Implementation
- Integrated Trivy for vulnerability scanning 
- Detects HIGH and CRITICAL vulnerabilities
- Pipeline can be configured to fail on security issues

---

## Docker Implementation 
- Containerized Flask application 
- Lightweight Python base image
- Optimized dependency installation 

---

## CI/CD Pipeline

The CI pipeline is implemented using GItHub Actions and includes:

- Code checkout
- Docker image build
- Security scanning using Trivy 

---

## Screenshots
![alt text](<Screenshot 2026-02-28 114313.png>)

---

## Key Learnings
- CI/CD pipeline automation 
- Docker containerization
- DevSecOps practices (Shift Left Security)
- Debugging real-world pipeline issues

---