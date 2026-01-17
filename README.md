# 🚀 Azure MLOps Pipeline (MLflow + Docker + CI/CD)

## 📌 Project Overview

This repository implements a **production-style MLOps pipeline** demonstrating how machine learning models can be trained, tracked, containerized, and validated through CI/CD using industry-standard tools.

The project focuses on **engineering-quality MLOps**, not notebooks or demos, and is designed to be **cloud-ready (Azure-compatible)**.

---

## 🧠 Architecture (Implemented)

```
Local / CI Environment
│
├── ML Training (scikit-learn)
│   └── Logs metrics & models to MLflow
│
├── MLflow Tracking Server (Dockerized)
│   ├── Experiments
│   ├── Runs
│   └── Model Registry
│
├── FastAPI Inference Service (Dockerized)
│
└── CI/CD Pipeline (GitHub Actions)
    ├── Docker build validation
    ├── Image build checks
    └── Linux/amd64 compatibility
```

---

## ✅ What Has Been Completed

### 🔹 1. Model Training & Experiment Tracking
- Implemented **Logistic Regression** training using scikit-learn
- Logged metrics, parameters, and artifacts
- Experiments and runs visible in **MLflow UI**

### 🔹 2. MLflow Model Registry
- Registered trained models in MLflow
- Versioned models visible in UI

### 🔹 3. Dockerized Services
- MLflow Tracking Server
- Trainer container
- FastAPI inference API

### 🔹 4. CI/CD with GitHub Actions (GREEN)
- Automated Docker builds
- Linux/amd64 compatibility validation

### 🔹 5. Azure Preparation (Paused)
- Azure Resource Group created
- Azure Container Apps environment created
- Azure Container Registry configured
- Deployment paused due to architecture compatibility (ARM vs AMD64)

---

## 🧪 Tech Stack

- Python 3
- scikit-learn
- MLflow
- FastAPI
- Docker
- GitHub Actions
- Azure Container Apps

---

## 📁 Repository Structure

```
azure-mlops-pipeline/
├── api/
├── training/
├── docker/
├── requirements.txt
└── .github/workflows/
```

---

## 🏁 Current Status

| Component | Status |
|--------|--------|
| Training | ✅ |
| MLflow | ✅ |
| Docker | ✅ |
| CI/CD | ✅ GREEN |
| Azure Deploy | ⏸️ Paused |

---

## 🚀 Future Work

- Azure deployment
- Monitoring & drift detection
- Automated model promotion

---

## 💼 Portfolio Value

This project demonstrates real-world **MLOps engineering**, CI/CD, Dockerization, and cloud-ready ML systems.
