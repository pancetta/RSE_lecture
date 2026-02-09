# Lecture 3: Advanced Python & Working with Libraries

## Overview
This lecture continues building on Python fundamentals, covering more advanced concepts and how to 
work effectively with third-party libraries. We focus on tools commonly used in research software 
engineering: NumPy for numerical computing, file I/O for data processing, and creating reusable, 
well-structured code.

**Duration**: ~90 minutes

## Topics Covered
- Working with third-party libraries (NumPy)
- Numerical computing with NumPy arrays
- File input/output (reading and writing data)
- List comprehensions and functional programming
- Building data processing pipelines
- Creating reusable modules and classes
- Best practices for using libraries

## Files
- `lecture_03.py` - Main lecture content in Jupytext format

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
cd lecture_03
jupytext --to notebook lecture_03.py
jupyter notebook lecture_03.ipynb
```

Or from the main repository directory:
```bash
make convert
jupyter notebook
```
