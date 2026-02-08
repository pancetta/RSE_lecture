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

1. Create and activate the base environment:
```bash
cd /path/to/RSE_lecture
make install
micromamba activate rse_lecture
```

Or manually:
```bash
micromamba env create -f environment.yml
micromamba activate rse_lecture
```

**Note:** Lecture 2 uses only the base environment with no additional dependencies.

2. Convert to notebook and run:
```bash
cd lecture_02
jupytext --to notebook lecture_02.py
jupyter notebook lecture_02.ipynb
```

Or from the main repository directory:
```bash
make convert
jupyter notebook
```
