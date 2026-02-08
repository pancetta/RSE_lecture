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

## Additional Dependencies
This lecture requires matplotlib in addition to the base dependencies:
- matplotlib>=3.5.0

## Running the Lecture

1. Create and activate the environment:
```bash
cd /path/to/RSE_lecture
make install-lecture1
micromamba activate rse_lecture
```

Or manually:
```bash
micromamba env create -f environment.yml
micromamba install -n rse_lecture -c conda-forge matplotlib>=3.5.0
micromamba activate rse_lecture
```

2. Convert to notebook and run:
```bash
cd lecture_01
jupytext --to notebook lecture_01.py
jupyter notebook lecture_01.ipynb
```

Or from the main repository directory:
```bash
make convert
jupyter notebook
```
