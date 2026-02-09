# Lecture 2: Python Basics - Command Line & Introduction to Python

## Overview
This lecture provides a foundation for Research Software Engineering by introducing basic command 
line usage and fundamental Python programming concepts. This is not a comprehensive Python course, 
but rather focuses on the essential skills needed for writing research software.

**Duration**: ~90 minutes

## Topics Covered
- Working with the command line
- Python fundamentals (variables, data types, collections)
- Control flow (if statements, loops)
- Functions and documentation
- Creating command-line scripts
- Using argparse for command-line arguments
- Best practices for research software

## Files
- `lecture_02.py` - Main lecture content in Jupytext format

## Additional Dependencies
This lecture uses only the base dependencies (no additional packages required beyond Python standard library)

## Running the Lecture

1. Create and activate the environment:
```bash
cd /path/to/RSE_lecture
make install-lecture2
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
cd lecture_02
jupytext --to notebook lecture_02.py
jupyter notebook lecture_02.ipynb
```

Or from the main repository directory:
```bash
make convert
jupyter notebook
```
