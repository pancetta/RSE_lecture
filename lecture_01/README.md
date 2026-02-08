# Lecture 1: Introduction to Research Software Engineering

## Overview
This lecture introduces the fundamental concepts of Research Software Engineering (RSE), including best practices, tools, and methodologies for developing high-quality research software.

## Topics Covered
- What is Research Software Engineering?
- Version control with Git
- Best practices for research code
- Writing clear, documented code

## Files
- `lecture_01.py` - Main lecture content in Jupytext format

## Running the Lecture

### Using micromamba (Recommended)

1. Create and activate the environment for this lecture:
```bash
cd /path/to/RSE_lecture
micromamba env create -f lecture_01/environment.yml
micromamba activate rse_lecture_01
```

Or use the Makefile:
```bash
make install-lecture1
micromamba activate rse_lecture_01
```

2. Convert to notebook and run:
```bash
cd lecture_01
jupytext --to notebook lecture_01.py
jupyter notebook lecture_01.ipynb
```

### Using pip

Convert to notebook:
```bash
jupytext --to notebook lecture_01.py
jupyter notebook lecture_01.ipynb
```

Or from the main repository directory:
```bash
make convert
jupyter notebook
```
