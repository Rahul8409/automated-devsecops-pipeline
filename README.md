# 🔐 Automated DevSecOps Pipeline Using IaC

<div align="center">

![DevSecOps](https://img.shields.io/badge/DevSecOps-Pipeline-blue?style=for-the-badge&logo=github-actions)
![Terraform](https://img.shields.io/badge/Terraform-IaC-7B42BC?style=for-the-badge&logo=terraform)
![Kubernetes](https://img.shields.io/badge/Kubernetes-Orchestration-326CE5?style=for-the-badge&logo=kubernetes)
![Docker](https://img.shields.io/badge/Docker-Container-2496ED?style=for-the-badge&logo=docker)
![Trivy](https://img.shields.io/badge/Trivy-Security-EE0000?style=for-the-badge&logo=aqua)
![Prometheus](https://img.shields.io/badge/Prometheus-Monitoring-E6522C?style=for-the-badge&logo=prometheus)
![Grafana](https://img.shields.io/badge/Grafana-Observability-F46800?style=for-the-badge&logo=grafana)

**Major Project | Enrollment No: 2201031000002**  
**Student: Rahul Aparnathi | Guide: Mrs. Parul Sharma**

</div>

---

## 📌 Table of Contents

- [Introduction](#-introduction)
- [Problem Statement](#-problem-statement)
- [Objectives](#-objectives)
- [Scope](#-scope)
- [Why DevSecOps?](#-why-devsecops)
- [Technology Stack](#-technology-stack)
- [System Architecture](#-system-architecture)
- [Infrastructure as Code (IaC)](#-infrastructure-as-code-iac)
- [CI/CD Pipeline Workflow](#-cicd-pipeline-workflow)
- [Security Implementation](#-security-implementation-devsecops)
- [Monitoring and Observability](#-monitoring-and-observability)
- [Automated Rollback Mechanism](#-automated-rollback-mechanism)
- [Results and Output](#-results-and-output)
- [Advantages](#-advantages)
- [Limitations](#-limitations)
- [Future Enhancements](#-future-enhancements)
- [Conclusion](#-conclusion)
- [References](#-references)

---

## 🚀 Introduction

Modern software systems demand **fast**, **secure**, and **reliable** deployment practices. Traditional manual deployments are:

- 🐢 **Slow** — bottlenecked by human processes
- ❌ **Error-prone** — configuration mistakes happen often
- 🔓 **Insecure** — security is an afterthought

This project bridges the gap by combining **DevSecOps** and **Infrastructure as Code (IaC)** to deliver a fully automated, secure, and observable deployment pipeline — running entirely on a **local cloud environment at zero cost**.

> **DevOps improves speed, but DevSecOps integrates security at every single stage.**

---

## ❗ Problem Statement

Manual infrastructure and deployment practices cause:

| Issue | Impact |
|---|---|
| Configuration inconsistencies | Unreliable deployments |
| Deployment failures | Downtime and rollback delays |
| Security vulnerabilities | Data breaches and compliance risk |
| Late-stage security patching | High remediation cost |
| High cloud costs | Inaccessible for students and learners |

> **Goal:** Eliminate these problems through full automation, integrated security, and a zero-cost local infrastructure.

---

## 🎯 Objectives

- ✅ Automate infrastructure provisioning using **IaC (Terraform)**
- ✅ Build a **CI/CD pipeline** for automated application deployment
- ✅ Integrate **security scanning** (DevSecOps) directly into the pipeline
- ✅ Deploy **containerized applications** using Kubernetes
- ✅ Implement **monitoring** for application performance and health
- ✅ Achieve all of the above using a **local cloud environment at zero cost**

---

## 🗺️ Scope

### ✔️ In Scope

- Single application deployment
- Local cloud infrastructure (Kind / WSL2)
- Fully automated CI/CD pipeline
- Integrated security scanning (Trivy)
- Monitoring and automated rollback mechanism

### ❌ Out of Scope

- Multi-cloud deployment
- AI-based decision making
- Production-level traffic handling

---

## 🛡️ Why DevSecOps?

Security vulnerabilities are **increasing at an unprecedented rate**, and fixing issues late in the software lifecycle is exponentially more expensive.

```
Traditional DevOps:   Dev → Build → Test → Deploy → (Security Later)
DevSecOps:            Dev → [Sec] Build → [Sec] Test → [Sec] Deploy
```

### Key Benefits

| Benefit | Description |
|---|---|
| 🔍 Early Detection | Vulnerabilities found during build, not production |
| ⚡ Secure Automation | Security gates baked into pipeline |
| 🚀 Faster Releases | Fewer rollbacks due to security surprises |

> **"Security is shifted left into the development lifecycle."**

---

## 🛠️ Technology Stack

| Category | Tools |
|---|---|
| **Version Control** | Git, GitHub |
| **CI/CD** | GitHub Actions |
| **Containerization** | Docker |
| **Orchestration** | Kubernetes (Kind) |
| **Infrastructure as Code** | Terraform |
| **Security Scanning** | Trivy |
| **Monitoring** | Prometheus, Grafana |
| **Operating System** | Ubuntu / WSL2 |

---

## 🏗️ System Architecture

```
Developer
    │
    ▼
┌──────────────┐
│   GitHub     │  ← Code Push
│  Repository  │
└──────┬───────┘
       │ Trigger
       ▼
┌──────────────────────────────────────────────────┐
│              GitHub Actions CI/CD Pipeline        │
│                                                  │
│  ┌──────────┐  ┌──────────┐  ┌───────────────┐  │
│  │  Build   │→ │  Test    │→ │ Security Scan │  │
│  │  Docker  │  │          │  │    (Trivy)    │  │
│  │  Image   │  │          │  │               │  │
│  └──────────┘  └──────────┘  └──────┬────────┘  │
│                                     │            │
│                               ┌─────▼────────┐  │
│                               │  Terraform   │  │
│                               │  Provision   │  │
│                               └─────┬────────┘  │
│                                     │            │
│                               ┌─────▼────────┐  │
│                               │  Kubernetes  │  │
│                               │  Deployment  │  │
│                               └─────┬────────┘  │
└─────────────────────────────────────┼────────────┘
                                      │
                    ┌─────────────────▼──────────────────┐
                    │   Prometheus + Grafana Monitoring   │
                    └────────────────────────────────────┘
```

---

## 📦 Infrastructure as Code (IaC)

Infrastructure is fully defined and managed using **Terraform** scripts.

### Key Benefits of IaC

```hcl
# Example: Terraform Kubernetes namespace provisioning
resource "kubernetes_namespace" "app" {
  metadata {
    name = "devsecops-app"
  }
}
```

| Feature | Description |
|---|---|
| 🗂️ Version Controlled | Infrastructure changes tracked in Git |
| 🔁 Reproducible Deployments | Same config → Same result every time |
| ↩️ Easy Rollback | Revert to a previous Terraform state |
| 🚫 No Manual Errors | Eliminates human configuration mistakes |

---

## 🔄 CI/CD Pipeline Workflow

```yaml
# GitHub Actions pipeline overview
name: DevSecOps Pipeline

on:
  push:
    branches: [main]

jobs:
  pipeline:
    steps:
      - name: 1️⃣  Code Checkout
        uses: actions/checkout@v3

      - name: 2️⃣  Build Docker Image
        run: docker build -t app:${{ github.sha }} .

      - name: 3️⃣  Run Tests
        run: docker run app:${{ github.sha }} npm test

      - name: 4️⃣  Security Scan (Trivy)
        uses: aquasecurity/trivy-action@master
        with:
          image-ref: app:${{ github.sha }}
          exit-code: '1'            # ← Fail pipeline on HIGH/CRITICAL issues
          severity: 'HIGH,CRITICAL'

      - name: 5️⃣  Deploy to Kubernetes
        run: kubectl apply -f k8s/

      - name: 6️⃣  Monitor Application
        run: echo "Prometheus & Grafana collecting metrics..."
```

### Pipeline Stages

```
Code Checkout → Build Docker Image → Run Tests → Security Scan → Deploy → Monitor
      1               2                 3              4             5        6
```

---

## 🔒 Security Implementation (DevSecOps)

Security is embedded as a **mandatory gate** in the CI/CD pipeline using **Trivy**.

```bash
# Trivy container scan command
trivy image --exit-code 1 --severity HIGH,CRITICAL app:latest
```

### Security Features

| Feature | Detail |
|---|---|
| 🔍 Container Image Scanning | Trivy scans every built Docker image |
| 🚨 Vulnerability Detection | Detects HIGH and CRITICAL CVEs |
| 🚫 Pipeline Gate | Build fails automatically if issues found |
| ✅ Secure Deployments | Only scanned, clean images reach Kubernetes |

> **No vulnerable image will ever reach production.**

---

## 📊 Monitoring and Observability

```
Application Pods
      │
      ▼
┌─────────────┐     scrape metrics     ┌─────────────────┐
│ Prometheus  │ ◄────────────────────  │  App Metrics    │
│  (Collect)  │                        │  Endpoint       │
└──────┬──────┘                        └─────────────────┘
       │ query
       ▼
┌─────────────┐
│   Grafana   │  → Dashboards, Alerts
│ (Visualize) │
└─────────────┘
```

### Metrics Monitored

| Metric | Description |
|---|---|
| 🖥️ CPU Usage | Per-pod and node CPU consumption |
| 🧠 Memory Usage | RAM utilization per deployment |
| 💚 Pod Health | Running / Pending / Failed pod states |
| 🌐 App Availability | Uptime and endpoint response status |

---

## ↩️ Automated Rollback Mechanism

The system automatically detects deployment failures and reverts to the **last stable version** without manual intervention.

```bash
# Kubernetes rollback command (triggered automatically on failure)
kubectl rollout undo deployment/app-deployment

# Check rollout status
kubectl rollout status deployment/app-deployment
```

### How It Works

```
Deploy New Version
       │
       ▼
  Health Check ──── FAIL ───► Detect Failure
       │                             │
    PASS                             ▼
       │                    Auto Rollback to
       ▼                    Last Stable Version
  ✅ Live in Production             │
                                    ▼
                            ✅ High Availability Restored
```

---

## 📈 Results and Output

| Result | Status |
|---|---|
| Fully automated DevSecOps pipeline | ✅ Achieved |
| Secure and reliable deployments | ✅ Achieved |
| Zero cloud cost implementation | ✅ Achieved |
| Reduced deployment time | ✅ Achieved |
| Improved system stability | ✅ Achieved |

---

## ✅ Advantages

| Advantage | Description |
|---|---|
| 💰 Cost-Effective | Runs entirely on local infrastructure — zero cloud spend |
| 🔐 Secure by Design | Security integrated at every pipeline stage |
| 📈 Scalable Architecture | Kubernetes enables horizontal scaling |
| 🤖 Reduced Manual Effort | End-to-end automation eliminates human steps |
| 🏭 Industry-Standard Tools | Uses tools adopted by top engineering teams |

---

## ⚠️ Limitations

- 🖥️ Runs on **local infrastructure** only — not deployed to a real cloud provider
- 📉 **Limited scalability** compared to production cloud environments
- 🎯 **Single application focus** — multi-service orchestration not covered

---

## 🔮 Future Enhancements

- ☁️ **Multi-cloud deployment** — AWS, Azure, GCP support
- 🔐 **Advanced security policies** — OPA/Gatekeeper, RBAC hardening
- 📈 **Auto-scaling implementation** — HPA and VPA for Kubernetes
- 🤖 **AI-based anomaly detection** — ML-driven alerts and predictions
- 🔗 **Cloud provider integration** — Full AWS / Azure pipeline support

---

## 🏁 Conclusion

This project successfully demonstrates a **complete, automated DevSecOps pipeline** built with industry-standard tools and best practices:

- 🔄 **Automated** — From code push to deployment, zero manual steps
- 🔐 **Secure** — Security scanning embedded at every stage
- 📊 **Observable** — Real-time metrics via Prometheus and Grafana
- 💰 **Zero Cost** — Runs entirely on local infrastructure
- 🌍 **Relevant** — Mirrors real-world modern cloud-native DevOps practices

> This project is a practical proof-of-concept showing that enterprise-grade DevSecOps is achievable without cloud spend.

---

## 📚 References

- 🐳 [Docker Documentation](https://docs.docker.com/)
- ☸️ [Kubernetes Documentation](https://kubernetes.io/docs/)
- 🏗️ [Terraform Documentation](https://developer.hashicorp.com/terraform/docs)
- ⚙️ [GitHub Actions Documentation](https://docs.github.com/en/actions)
- 📊 [Prometheus Documentation](https://prometheus.io/docs/)
- 📈 [Grafana Documentation](https://grafana.com/docs/)

---

<div align="center">

**Made with ❤️ by Rahul Aparnathi**  
*Enrollment No: 2201031000002 | Guide: Mrs. Parul Sharma*

![GitHub](https://img.shields.io/badge/GitHub-DevSecOps-181717?style=flat-square&logo=github)
![License](https://img.shields.io/badge/License-Academic-green?style=flat-square)

</div>
