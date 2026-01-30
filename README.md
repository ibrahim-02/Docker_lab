# 🐳 Docker Practice Lab

A hands-on Docker lab assignment for the **MLOps (Machine Learning Operations)** course at Northeastern University.

---


## 🧪 Lab 01: Model Training

### Objective
Train a **Gradient Boosting Classifier** on the Breast Cancer dataset and save the model as `.pkl` file.

### Dockerfile

```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY src/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src/ .
CMD ["python", "main.py"]
```

### Key Points

| Line | What it does |
|------|--------------|
| `FROM python:3.10-slim` | Uses lightweight Python image (~45MB vs ~900MB full) |
| `COPY requirements.txt` first | Enables **layer caching** — if requirements don't change, Docker skips reinstalling |
| `--no-cache-dir` | Reduces image size by not storing pip cache |
| `CMD` | Runs training script on container start |

### Run Lab 01

```bash
cd lab_01
docker build -t breast-cancer-trainer .
docker run breast-cancer-trainer
```

---

## 🚀 Lab 02: Model Deployment

### Objective
Deploy the trained model as a **Flask REST API** with a web interface for predictions.

### Dockerfile

```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 4000
CMD ["python", "main.py"]
```

### Key Points

| Line | What it does |
|------|--------------|
| `EXPOSE 4000` | Documents the port Flask runs on (informational only) |
| `COPY . .` | Copies everything — model file, templates, main.py |

### Docker Compose

```yaml
version: '3.8'

services:
  breast-cancer-api:
    build: .
    container_name: cancer-detect-ai
    ports:
      - "4000:4000"
    restart: unless-stopped
```

### Key Points

| Line | What it does |
|------|--------------|
| `build: .` | Builds image from Dockerfile in current directory |
| `ports: "4000:4000"` | Maps host port → container port |
| `restart: unless-stopped` | Auto-restarts if container crashes |

### Run Lab 02

```bash
cd lab_02
docker-compose up --build
```

**Access**: http://localhost:4000/predict

---

## 🔧 Quick Docker Commands

```bash
# Build & Run
docker build -t <name> .
docker run -p 4000:4000 <name>

# Docker Compose
docker-compose up --build    # Start
docker-compose down          # Stop

# Useful
docker ps                    # List running containers
docker logs <container>      # View logs
```

---

## 🎯 What You Learned

- ✅ Writing Dockerfiles for ML applications
- ✅ Layer caching for faster builds
- ✅ Port mapping and EXPOSE
- ✅ Docker Compose for easy deployment
- ✅ Containerizing ML models with Flask API

---

## 👨‍🏫 Course Info

**Course**: MLOps | **University**: Northeastern University | **Instructor**: Prof. Ramin Mohammadi
