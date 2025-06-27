# helm-phase-3 🚀

This repository demonstrates a DevOps workflow for containerizing, testing, and deploying a simple Python Flask application using Docker and Helm on Kubernetes.

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

### 1. Run Locally (Python) 💻
```bash
uv sync  # or pip install -r requirements.txt
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
# Build and load Docker image to your cluster (e.g., kind)
# helm install test-app ./amitchart --set image.repository=flask-test,image.tag=latest,image.pullPolicy=Never
# See amitchart/templates/NOTES.txt for access instructions
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
