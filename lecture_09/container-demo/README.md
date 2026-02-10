# Container Demo for Lecture 9

This directory contains a simple containerized data analysis application that demonstrates the concepts from Lecture 9: Containerization and Reproducibility.

## What This Demonstrates

- Writing a Dockerfile following best practices
- Using layer caching (requirements copied before code)
- Running as non-root user (security)
- Pinning dependency versions (reproducibility)

## Running Locally

### With Docker

```bash
cd lecture_09/container-demo

# Build the container
docker build -t data-analysis-demo .

# Run the analysis
docker run data-analysis-demo
```

### With Podman

```bash
cd lecture_09/container-demo

# Build the container
podman build -t data-analysis-demo .

# Run the analysis
podman run data-analysis-demo
```

## Running in CI

This example is automatically built and tested in the GitHub Actions CI pipeline (see `.github/workflows/ci.yml`), demonstrating how containers integrate with continuous integration workflows.

## Files

- `Dockerfile` - Container definition following Lecture 9 best practices
- `requirements.txt` - Pinned Python dependencies
- `analyze_data.py` - Simple data analysis script
- `README.md` - This file
