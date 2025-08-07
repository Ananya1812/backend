# Backend

## Overview
This repository contains the backend application for the project, built with Python and FastAPI.

## Folder Structure

- `main.py` - Main FastAPI app
- `test_main.py` - Pytest tests
- `Dockerfile` - Docker build file
- `.github/workflows/` - CI/CD workflows

## Scripts

Run these commands from the `backend` directory:

- `python main.py` - Start the FastAPI server
- `pytest test_main.py` - Run backend tests

## CI/CD Workflows

- [Backend Tests](.github/workflows/backend-tests.yml): Runs tests and security scan
- [Build and Push Docker Image](.github/workflows/docker-image.yml): Builds and pushes Docker image
- [Publish to GitHub Packages](.github/workflows/docker-ghcr.yml): Publishes Docker image to GitHub Packages
- [Vulnerability Scan](.github/workflows/docker-scan.yml): Trivy scan for Docker image

## Docker

Build and run the backend Docker image:

```sh
docker build -t backend:latest .
docker run -d -p 8000:8000 backend:latest
```

## Vulnerability Scanning

Trivy scan is included in the CI pipeline. See the Actions tab for reports.

## Deployment

Deployment can be automated via GitHub Actions and SSH. See `.github/workflows/docker-deploy.yml` for details (add this workflow if not present).

## Useful Links

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Pytest Documentation](https://docs.pytest.org/en/stable/)
- [Trivy](https://aquasecurity.github.io/trivy/)

## Setup Instructions

1. Clone the repo
2. Run `pip install -r requirements.txt` (add requirements.txt if not present)
3. Use scripts above to develop, test, and build
4. Push to `main` to trigger CI/CD