# Phase 3 && 4 🚀

This repository demonstrates a DevOps workflow for containerizing, testing, and deploying a simple Python Flask application using Docker and Helm on Kubernetes. It also includes integration with Argo CD for GitOps-based continuous deployment to Kubernetes clusters.

## Project Structure 🗂️

- `app.py`: Minimal Flask app returning "Hello, World!!!!!" on `/`.
- `Dockerfile`: Containerizes the Flask app using Python 3.11 and [uv](https://github.com/astral-sh/uv) for dependency management.
- `pyproject.toml`, `uv.lock`: Python dependencies and lock file.
- `amitchart/`: Helm chart for deploying the app to Kubernetes.
  - `Chart.yaml`, `values.yaml`: Chart metadata and configuration values.
  - `templates/`: Helm templates for Kubernetes resources (deployment, service, ingress, etc).
- `tests/`: Pytest-based tests for both local Docker and Kubernetes deployments.
- `.github/workflows/`: CI/CD pipelines for linting, testing, Docker image build/push, and Helm chart publishing.

## Main Features ✨
- **Flask App** 🐍: Simple web server for demo purposes.
- **Dockerized** 🐳: Easily build and run the app in a container.
- **Helm Chart** ⎈: Deploys the app to Kubernetes with customizable values.
- **CI/CD** ⚙️: Automated linting, testing (Docker & Kubernetes), Docker image publishing, and Helm chart publishing via GitHub Actions.
## Getting Started 🏁

> **Note for Users:**  
> If you just want to install and use the application, please see [README-INSTALLATION.md](./README-INSTALLATION.md) for end-user instructions.  
> The following steps are intended for developers who want to build, test, or contribute to the project.

### Recommended Order for Developers

1. **Run Locally (Python):**  
  Set up your environment and run the app directly for rapid development and debugging.
2. **Run with Docker:**  
  Build and run the app in a container to ensure it works in a production-like environment.
3. **Deploy to Kubernetes with Helm:**  
  Use Helm to deploy the app to a Kubernetes cluster for integration testing or staging.
4. **Run Tests:**  
  Execute tests against both Docker and Kubernetes deployments to verify functionality.

Follow the detailed instructions below for each step.

### 1. Run Locally (Python) 💻
```bash
uv sync
uv run python app.py
# Visit http://localhost:5000
```

### 2. Run with Docker 🐳
```bash
docker build -t flask-test .
docker run -p 5000:5000 flask-test
# Visit http://localhost:5000
```

### 3. Deploy to Kubernetes with Helm ⎈
```bash
# 1. Start minikube
minikube start

# 2. Load the image into Minikube
minikube image load flask-test:latest

# 3. Deploy with Helm, using the local image
helm install test-app ./amitchart --set image.repository=flask-test,image.tag=latest,image.pullPolicy=Never
```

### 4. Run Tests 🧪
```bash
uv run pytest tests/test_hello.py -m docker      # Test local Docker
uv run pytest tests/test_hello.py -m kubernetes  # Test on Kubernetes
```

## CI/CD 🔄
- Linting and tests run on PRs and pushes (see `.github/workflows/ci-tests.yaml`).
- Docker images are built and pushed to Docker Hub on `main` branch (see `.github/workflows/ci-cd-helm.yml`).
- Helm chart is packaged and published to GitHub Pages.

## Requirements 📦
- Python 3.8+
- [uv](https://github.com/astral-sh/uv) (for local dev)
- Docker
- Kubernetes cluster (e.g., kind, minikube)
- Helm 3

## Customization 🛠️
- Edit `amitchart/values.yaml` to change image, service type, probes, etc.
- Extend `app.py` for more endpoints.
- Add more tests in `tests/`.

---

For more details, see comments in the respective files and the GitHub Actions workflows. 😊
