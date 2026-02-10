# Dockerfile for containerized data analysis demo
# This demonstrates best practices from Lecture 9

FROM python:3.10-slim

# Set metadata
LABEL maintainer="RSE Course"
LABEL description="Demo container for Lecture 9: Containerization"
LABEL version="1.0"

# Set working directory
WORKDIR /app

# Install Python dependencies
# Copy requirements first for better layer caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY analyze_data.py .

# Create non-root user (security best practice)
RUN useradd -m -s /bin/bash researcher && \
    chown -R researcher:researcher /app

# Switch to non-root user
USER researcher

# Default command
CMD ["python", "analyze_data.py"]
