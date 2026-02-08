# Lecture 2: Testing and Continuous Integration

## Overview
This lecture covers testing strategies for research software, including unit testing, integration testing, and setting up continuous integration pipelines.

## Topics Covered
- Why testing matters in research
- Writing unit tests with pytest
- Test coverage
- Continuous integration concepts

## Files
- `lecture_02.py` - Main lecture content in Jupytext format

## Running the Lecture

### Using micromamba (Recommended)

1. Create and activate the environment for this lecture:
```bash
cd /path/to/RSE_lecture
micromamba env create -f lecture_02/environment.yml
micromamba activate rse_lecture_02
```

Or use the Makefile:
```bash
make install-lecture2
micromamba activate rse_lecture_02
```

2. Convert to notebook and run:
```bash
cd lecture_02
jupytext --to notebook lecture_02.py
jupyter notebook lecture_02.ipynb
```

### Using pip

Convert to notebook:
```bash
jupytext --to notebook lecture_02.py
jupyter notebook lecture_02.ipynb
```

Or from the main repository directory:
```bash
make convert
jupyter notebook
```
