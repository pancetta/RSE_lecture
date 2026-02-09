# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.14.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Lecture 4: Python Project Structure and Scientific Libraries
# 
# ## Overview
# This lecture teaches you how to organize research code into professional projects and
# introduces essential scientific computing libraries. You'll learn best practices for
# structuring Python projects and gain hands-on experience with NumPy and Matplotlib,
# the foundational tools for numerical computing and visualization in Python.
# 
# **Duration**: ~90 minutes
# 
# ## Learning Objectives
# - Organize research code into proper Python packages and modules
# - Understand and use virtual environments
# - Master NumPy for numerical computing
# - Create publication-quality visualizations with Matplotlib
# - Apply best practices for reproducible research software

# %% [markdown]
# ## Part 1: Python Project Structure (30 minutes)
# 
# ### Why Project Structure Matters
# 
# As your research code grows, proper organization becomes critical:
# 
# - **Maintainability**: Easy to find and update code
# - **Reusability**: Share code across projects and with collaborators
# - **Reproducibility**: Others can run and verify your work
# - **Collaboration**: Team members can navigate and contribute
# - **Testing**: Easier to write and run tests
# - **Distribution**: Package your code for others to install
# 
# ### Anatomy of a Research Python Project
# 
# A typical research project structure:
# 
# ```
# my_research_project/
# ├── README.md              # Project description and usage
# ├── LICENSE                # Software license
# ├── requirements.txt       # Python dependencies (pip)
# ├── environment.yml        # Conda environment specification
# ├── setup.py              # Package installation configuration
# ├── .gitignore            # Files to exclude from version control
# ├── data/                 # Data files (often in .gitignore)
# │   ├── raw/              # Original, immutable data
# │   └── processed/        # Cleaned, transformed data
# ├── notebooks/            # Jupyter notebooks for exploration
# │   └── analysis.ipynb
# ├── src/                  # Source code (or use project name)
# │   ├── __init__.py       # Makes src a Python package
# │   ├── data_processing.py
# │   ├── analysis.py
# │   └── visualization.py
# ├── tests/                # Unit tests
# │   ├── __init__.py
# │   └── test_analysis.py
# ├── scripts/              # Command-line scripts
# │   └── run_analysis.py
# └── docs/                 # Documentation
#     └── usage.md
# ```

# %% [markdown]
# ### Understanding Modules and Packages
# 
# **Module**: A single Python file (`.py`) containing functions, classes, and variables
# 
# **Package**: A directory containing multiple modules and an `__init__.py` file
# 
# #### Example Module Structure

# %%
# Let's simulate creating a simple package structure
# In practice, these would be separate files

# File: src/data_processing.py
def load_data(filename):
    """Load experimental data from a file."""
    # Simplified example
    print(f"Loading data from {filename}")
    return [1.2, 2.3, 3.1, 4.5, 2.8]

def clean_data(data, threshold=0.0):
    """Remove negative values and outliers."""
    return [x for x in data if x > threshold]


# File: src/analysis.py
def calculate_statistics(data):
    """Calculate basic statistics for a dataset."""
    n = len(data)
    mean = sum(data) / n
    variance = sum((x - mean) ** 2 for x in data) / n
    std = variance ** 0.5
    
    return {
        'mean': mean,
        'std': std,
        'min': min(data),
        'max': max(data),
        'n': n
    }


# File: src/__init__.py (makes src a package)
# __init__.py can be empty or expose key functions:
# from .data_processing import load_data, clean_data
# from .analysis import calculate_statistics

# %%
# Using the modules
data = load_data("experiment_01.csv")
cleaned_data = clean_data(data, threshold=1.0)
stats = calculate_statistics(cleaned_data)

print("Data Statistics:")
for key, value in stats.items():
    if isinstance(value, float):
        print(f"  {key}: {value:.2f}")
    else:
        print(f"  {key}: {value}")

# %% [markdown]
# ### The __init__.py File
# 
# The `__init__.py` file serves several purposes:
# 
# 1. **Marks a directory as a Python package**
# 2. **Controls what gets imported** when someone does `import package_name`
# 3. **Can contain initialization code** for the package
# 
# #### Different __init__.py Patterns

# %%
# Pattern 1: Empty __init__.py
# (Just marks directory as package, users must import specific modules)
# import src.data_processing
# import src.analysis

# Pattern 2: Expose key functions
# File: src/__init__.py
# from .data_processing import load_data, clean_data
# from .analysis import calculate_statistics
# 
# Now users can do:
# from src import load_data, calculate_statistics

# Pattern 3: Define __all__ for controlled exports
# File: src/__init__.py
# from .data_processing import load_data, clean_data
# from .analysis import calculate_statistics
# 
# __all__ = ['load_data', 'clean_data', 'calculate_statistics']
# 
# This controls what 'from src import *' brings in

print("__init__.py patterns demonstrated above")

# %% [markdown]
# ### Managing Dependencies: requirements.txt
# 
# The `requirements.txt` file lists all Python packages your project needs.
# 
# #### Creating requirements.txt
# 
# ```bash
# # Method 1: Manually create
# # requirements.txt
# numpy>=1.20.0
# matplotlib>=3.3.0
# pandas>=1.2.0
# scipy>=1.6.0
# 
# # Method 2: Generate from current environment
# pip freeze > requirements.txt
# 
# # Method 3: Use pipreqs to scan your code (better!)
# pip install pipreqs
# pipreqs /path/to/project
# ```
# 
# #### Installing from requirements.txt
# 
# ```bash
# pip install -r requirements.txt
# ```
# 
# #### Best Practices
# 
# - **Pin versions** for reproducibility: `numpy==1.21.0`
# - **Use minimum versions** for flexibility: `numpy>=1.20.0`
# - **Separate dev dependencies**: Create `requirements-dev.txt` for testing tools

# %% [markdown]
# ### Conda Environment Files (environment.yml)
# 
# For conda users, `environment.yml` is the equivalent of `requirements.txt`.
# 
# #### Example environment.yml
# 
# ```yaml
# name: my_research_env
# channels:
#   - conda-forge
#   - defaults
# dependencies:
#   - python=3.9
#   - numpy=1.21
#   - matplotlib=3.4
#   - pandas=1.3
#   - scipy=1.7
#   - jupyter
#   - pip
#   - pip:
#     - some-pip-only-package
# ```
# 
# #### Using environment.yml
# 
# ```bash
# # Create environment from file
# conda env create -f environment.yml
# 
# # Activate the environment
# conda activate my_research_env
# 
# # Export your current environment
# conda env export > environment.yml
# 
# # Update environment from file
# conda env update -f environment.yml
# ```

# %% [markdown]
# ### Virtual Environments: Why and How
# 
# **Virtual environments** isolate project dependencies, preventing conflicts.
# 
# #### Why Use Virtual Environments?
# 
# 1. **Isolation**: Each project has its own dependencies
# 2. **Reproducibility**: Lock exact versions for your project
# 3. **No conflicts**: Project A can use NumPy 1.19, Project B can use 1.21
# 4. **Clean system**: Don't clutter global Python installation
# 5. **Easy cleanup**: Delete environment to remove all packages
# 
# #### Creating Virtual Environments
# 
# **Option 1: venv (built-in, Python 3.3+)**
# 
# ```bash
# # Create virtual environment
# python -m venv myenv
# 
# # Activate (Linux/Mac)
# source myenv/bin/activate
# 
# # Activate (Windows)
# myenv\Scripts\activate
# 
# # Install packages
# pip install numpy matplotlib
# 
# # Deactivate
# deactivate
# ```
# 
# **Option 2: conda**
# 
# ```bash
# # Create environment with specific Python version
# conda create -n myenv python=3.9
# 
# # Activate
# conda activate myenv
# 
# # Install packages
# conda install numpy matplotlib
# 
# # Deactivate
# conda deactivate
# ```

# %%
# Check if we're in a virtual environment
import sys
import os

def check_virtual_env():
    """Check if running in a virtual environment."""
    in_venv = hasattr(sys, 'real_prefix') or (
        hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix
    )
    
    if in_venv:
        print("✓ Running in a virtual environment")
        print(f"  Environment: {sys.prefix}")
    else:
        print("✗ Not in a virtual environment")
        print(f"  Using system Python: {sys.prefix}")
    
    print(f"  Python version: {sys.version.split()[0]}")
    print(f"  Executable: {sys.executable}")

check_virtual_env()

# %% [markdown]
# ### Setup.py Basics
# 
# `setup.py` makes your project installable with `pip install .`
# 
# #### Minimal setup.py
# 
# ```python
# from setuptools import setup, find_packages
# 
# setup(
#     name='my-research-project',
#     version='0.1.0',
#     author='Your Name',
#     author_email='your.email@university.edu',
#     description='Analysis tools for X research',
#     packages=find_packages(),
#     install_requires=[
#         'numpy>=1.20.0',
#         'matplotlib>=3.3.0',
#         'pandas>=1.2.0',
#     ],
#     python_requires='>=3.7',
# )
# ```
# 
# #### Installing Your Package
# 
# ```bash
# # Regular install
# pip install .
# 
# # Editable/development install (changes reflected immediately)
# pip install -e .
# 
# # Install with optional dependencies
# pip install -e ".[dev]"  # if you defined dev extras
# ```
# 
# #### Why Use setup.py?
# 
# - Import your code from anywhere: `from my_research_project import analysis`
# - Share with others: `pip install git+https://github.com/user/repo.git`
# - Publish to PyPI: `pip install my-research-project`

# %%
# Demonstrate what setup.py enables
# After installing with setup.py, you can do:

# Instead of:
# sys.path.append('../src')  # Fragile!
# from src import analysis

# You can simply:
# from my_research_project import analysis  # Clean!

print("setup.py enables clean, absolute imports")
print("Your package becomes a proper Python package")

# %% [markdown]
# ### Best Practices Summary: Project Structure
# 
# 1. **Use a clear directory structure** - Separate source, tests, data, notebooks
# 2. **Always use virtual environments** - One per project
# 3. **Document dependencies** - requirements.txt or environment.yml
# 4. **Make your code a package** - Use __init__.py and setup.py
# 5. **Keep data out of git** - Use .gitignore for large/sensitive data
# 6. **Include a README** - Explain what, why, and how
# 7. **Add a LICENSE** - Make sharing clear and legal
# 8. **Version your code** - Use semantic versioning (major.minor.patch)

# %% [markdown]
# ---
# ## Part 2: Working with NumPy (30 minutes)
# 
# ### Why NumPy for Scientific Computing?
# 
# NumPy (Numerical Python) is the foundation of scientific computing in Python:
# 
# **Advantages:**
# - **Speed**: 10-100x faster than pure Python lists
# - **Memory efficient**: Compact storage of numerical data
# - **Vectorization**: Write clean code without loops
# - **Integration**: Works seamlessly with SciPy, Pandas, Matplotlib
# - **Universal**: Standard in research, industry, and education
# 
# **Use NumPy for:**
# - Numerical arrays and matrices
# - Mathematical operations on arrays
# - Linear algebra, statistics, random numbers
# - Foundation for other libraries (pandas, scikit-learn, etc.)

# %%
import numpy as np
import time

# Demonstrate NumPy speed advantage
def python_sum_squares(n):
    """Calculate sum of squares using pure Python."""
    return sum(i**2 for i in range(n))

def numpy_sum_squares(n):
    """Calculate sum of squares using NumPy."""
    return np.sum(np.arange(n)**2)

# Benchmark
n = 1_000_000

start = time.time()
result_python = python_sum_squares(n)
time_python = time.time() - start

start = time.time()
result_numpy = numpy_sum_squares(n)
time_numpy = time.time() - start

print(f"Python: {result_python:,} ({time_python:.4f} seconds)")
print(f"NumPy:  {result_numpy:,} ({time_numpy:.4f} seconds)")
print(f"NumPy is {time_python/time_numpy:.1f}x faster!")

# %% [markdown]
# ### Creating NumPy Arrays
# 
# NumPy's fundamental data structure is the **ndarray** (n-dimensional array).

# %%
# Method 1: From Python lists
temps_list = [20.1, 21.3, 19.8, 22.5, 21.0]
temps = np.array(temps_list)
print(f"From list: {temps}")
print(f"Type: {type(temps)}")
print(f"Data type: {temps.dtype}")
print()

# Method 2: np.arange (like range, but returns array)
# np.arange(start, stop, step)
measurements = np.arange(0, 10, 2)  # 0, 2, 4, 6, 8
print(f"np.arange(0, 10, 2): {measurements}")
print()

# For floats
time_points = np.arange(0.0, 5.0, 0.5)
print(f"Time points: {time_points}")
print()

# Method 3: np.linspace (linearly spaced values)
# np.linspace(start, stop, num)
# More intuitive than arange for floats
time_series = np.linspace(0, 10, 11)  # 11 points from 0 to 10
print(f"np.linspace(0, 10, 11): {time_series}")
print()

# Method 4: Arrays of zeros
zeros = np.zeros(5)
print(f"Zeros: {zeros}")
print()

# Method 5: Arrays of ones
ones = np.ones(5)
print(f"Ones: {ones}")
print()

# Method 6: Empty array (uninitialized, faster but values are random)
empty = np.empty(5)
print(f"Empty (random values): {empty}")

# %% [markdown]
# ### Array Attributes and Information

# %%
# Create a sample array
data = np.array([1.5, 2.3, 3.7, 4.2, 5.1, 6.0])

print(f"Array: {data}")
print(f"Shape: {data.shape}")          # Dimensions
print(f"Size: {data.size}")            # Total elements
print(f"Data type: {data.dtype}")      # Element type
print(f"Dimensions: {data.ndim}")      # Number of dimensions
print(f"Item size: {data.itemsize} bytes")  # Size of each element
print(f"Total bytes: {data.nbytes} bytes")  # Total memory

# %% [markdown]
# ### Array Operations: Vectorization
# 
# NumPy's power comes from **vectorized operations** - operations on entire arrays
# without explicit loops.

# %%
# Create experimental temperature data (in Celsius)
temps_celsius = np.array([20.1, 21.3, 19.8, 22.5, 21.0, 20.5, 23.1])
print(f"Temperatures (°C): {temps_celsius}")
print()

# Convert to Fahrenheit: F = C * 9/5 + 32
# No loop needed! Operation applies to every element
temps_fahrenheit = temps_celsius * 9/5 + 32
print(f"Temperatures (°F): {temps_fahrenheit}")
print()

# Normalize to mean=0, std=1 (standardization)
mean_temp = temps_celsius.mean()
std_temp = temps_celsius.std()
temps_normalized = (temps_celsius - mean_temp) / std_temp
print(f"Normalized temps: {temps_normalized}")
print(f"Check - mean: {temps_normalized.mean():.10f}, std: {temps_normalized.std():.2f}")
print()

# Element-wise operations
data1 = np.array([1, 2, 3, 4, 5])
data2 = np.array([10, 20, 30, 40, 50])

print(f"Addition: {data1 + data2}")
print(f"Subtraction: {data1 - data2}")
print(f"Multiplication: {data1 * data2}")
print(f"Division: {data2 / data1}")
print(f"Power: {data1 ** 2}")

# %% [markdown]
# ### Indexing and Slicing
# 
# NumPy arrays support powerful indexing and slicing operations.

# %%
# Create sample data
measurements = np.array([10.5, 12.3, 15.1, 11.8, 13.7, 14.2, 16.5, 15.8, 14.1, 12.9])
print(f"Measurements: {measurements}")
print()

# Basic indexing (0-based)
print(f"First measurement: {measurements[0]}")
print(f"Last measurement: {measurements[-1]}")
print(f"Third measurement: {measurements[2]}")
print()

# Slicing: array[start:stop:step]
print(f"First 3: {measurements[:3]}")
print(f"Last 3: {measurements[-3:]}")
print(f"Middle values: {measurements[3:7]}")
print(f"Every other: {measurements[::2]}")
print(f"Reversed: {measurements[::-1]}")
print()

# Fancy indexing: using arrays of indices
indices = np.array([0, 2, 4, 6])
print(f"Selected indices {indices}: {measurements[indices]}")

# %% [markdown]
# ### Boolean Indexing (Filtering)
# 
# One of NumPy's most powerful features: filter arrays using conditions.

# %%
# Experimental results
results = np.array([12.5, 15.3, 14.1, 18.7, 13.2, 19.5, 11.8, 16.4, 14.9, 17.2])
print(f"Results: {results}")
print()

# Create boolean mask
threshold = 15.0
mask = results > threshold
print(f"Mask (> {threshold}): {mask}")
print()

# Apply mask to get filtered values
high_results = results[mask]
print(f"High results (> {threshold}): {high_results}")
print()

# Compact form (common usage)
print(f"Results > 15: {results[results > 15]}")
print(f"Results < 13: {results[results < 13]}")
print(f"Results between 14 and 17: {results[(results >= 14) & (results <= 17)]}")
print()

# Multiple conditions (note: use & for AND, | for OR, not 'and'/'or')
# Parentheses are required!
outliers = results[(results < 13) | (results > 18)]
print(f"Outliers (< 13 or > 18): {outliers}")
print()

# Count how many meet condition
n_high = np.sum(results > threshold)  # True = 1, False = 0
print(f"Number of high results: {n_high}")

# %% [markdown]
# ### Statistical Operations
# 
# NumPy provides comprehensive statistical functions.

# %%
# Simulate daily temperature measurements over 2 weeks
np.random.seed(42)  # For reproducibility
daily_temps = np.random.normal(loc=21.0, scale=2.5, size=14)  # mean=21°C, std=2.5°C
daily_temps = np.round(daily_temps, 1)

print(f"Daily temperatures (°C): {daily_temps}")
print()

# Basic statistics
print(f"Mean: {np.mean(daily_temps):.2f} °C")
print(f"Median: {np.median(daily_temps):.2f} °C")
print(f"Standard deviation: {np.std(daily_temps):.2f} °C")
print(f"Variance: {np.var(daily_temps):.2f}")
print(f"Minimum: {np.min(daily_temps):.2f} °C")
print(f"Maximum: {np.max(daily_temps):.2f} °C")
print(f"Range: {np.ptp(daily_temps):.2f} °C")  # peak-to-peak
print()

# Percentiles
print(f"25th percentile: {np.percentile(daily_temps, 25):.2f} °C")
print(f"75th percentile: {np.percentile(daily_temps, 75):.2f} °C")
print()

# Indices of min/max
print(f"Coldest day: Day {np.argmin(daily_temps) + 1}")
print(f"Warmest day: Day {np.argmax(daily_temps) + 1}")
print()

# Cumulative operations
cumulative_sum = np.cumsum(daily_temps)
print(f"Cumulative temperature sum: {cumulative_sum[-1]:.1f} °C")

# %%
# More statistical functions
data = np.array([23.5, 24.1, 23.8, 25.2, 24.0, 23.9, 24.5])

print(f"Data: {data}")
print(f"Sum: {np.sum(data):.2f}")
print(f"Product: {np.prod(data):.2e}")
print(f"Mean: {np.mean(data):.2f}")
print(f"Std: {np.std(data):.2f}")
print(f"Quantiles (25%, 50%, 75%): {np.quantile(data, [0.25, 0.5, 0.75])}")

# %% [markdown]
# ### 2D Arrays and Multi-dimensional Operations
# 
# NumPy excels at multi-dimensional arrays (matrices and tensors).

# %%
# Create a 2D array (matrix)
# Experiment data: 4 trials × 6 time points
experiment_data = np.array([
    [10.2, 10.5, 11.1, 11.8, 12.5, 13.1],  # Trial 1
    [10.1, 10.3, 10.9, 11.5, 12.1, 12.8],  # Trial 2
    [10.3, 10.7, 11.3, 12.0, 12.7, 13.4],  # Trial 3
    [10.0, 10.4, 11.0, 11.6, 12.3, 13.0],  # Trial 4
])

print(f"Experiment data shape: {experiment_data.shape}")  # (4 trials, 6 time points)
print(f"Data:\n{experiment_data}")
print()

# Access elements
print(f"Trial 1, Time 1: {experiment_data[0, 0]}")
print(f"Trial 3, Time 4: {experiment_data[2, 3]}")
print()

# Slicing 2D arrays
print(f"All of Trial 2: {experiment_data[1, :]}")
print(f"Time point 3 for all trials: {experiment_data[:, 2]}")
print(f"First 2 trials, first 3 time points:\n{experiment_data[:2, :3]}")
print()

# Statistics along axes
print(f"Mean per trial (across time): {np.mean(experiment_data, axis=1)}")
print(f"Mean per time point (across trials): {np.mean(experiment_data, axis=0)}")
print(f"Overall mean: {np.mean(experiment_data):.2f}")

# %%
# Creating special 2D arrays
print("Zeros (3×4 matrix):")
print(np.zeros((3, 4)))
print()

print("Ones (2×5 matrix):")
print(np.ones((2, 5)))
print()

print("Identity matrix (4×4):")
print(np.eye(4))
print()

print("Diagonal matrix:")
print(np.diag([1, 2, 3, 4]))
print()

# Random matrices
print("Random uniform [0, 1) (3×3):")
np.random.seed(42)
print(np.random.random((3, 3)))
print()

print("Random normal (mean=0, std=1) (2×4):")
print(np.random.randn(2, 4))

# %%
# Matrix operations
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print("Matrix A:")
print(A)
print("\nMatrix B:")
print(B)
print()

print("Element-wise multiplication (A * B):")
print(A * B)
print()

print("Matrix multiplication (A @ B):")
print(A @ B)  # or np.dot(A, B)
print()

print("Transpose of A:")
print(A.T)
print()

# Reshape
data_1d = np.arange(12)
print(f"1D array: {data_1d}")
print(f"Reshaped to 3×4:\n{data_1d.reshape(3, 4)}")
print(f"Reshaped to 4×3:\n{data_1d.reshape(4, 3)}")

# %% [markdown]
# ### Practical Example: Analyzing Experimental Data

# %%
# Simulate a week of temperature measurements (3 readings per day)
np.random.seed(42)
days = 7
readings_per_day = 3

# Temperature data: 7 days × 3 readings
temperatures = np.random.normal(loc=22.0, scale=1.5, size=(days, readings_per_day))
temperatures = np.round(temperatures, 1)

print("Temperature data (°C):")
print("        Morning  Afternoon  Evening")
for day in range(days):
    print(f"Day {day+1}:   {temperatures[day, 0]:5.1f}    {temperatures[day, 1]:5.1f}     {temperatures[day, 2]:5.1f}")
print()

# Analysis
daily_means = np.mean(temperatures, axis=1)
daily_ranges = np.ptp(temperatures, axis=1)  # max - min per day

reading_means = np.mean(temperatures, axis=0)

print(f"Daily mean temperatures: {daily_means}")
print(f"Daily temperature ranges: {daily_ranges}")
print()

print(f"Average morning temperature: {reading_means[0]:.2f} °C")
print(f"Average afternoon temperature: {reading_means[1]:.2f} °C")
print(f"Average evening temperature: {reading_means[2]:.2f} °C")
print()

print(f"Overall mean: {np.mean(temperatures):.2f} °C")
print(f"Overall std: {np.std(temperatures):.2f} °C")
print(f"Warmest reading: {np.max(temperatures):.2f} °C")
print(f"Coldest reading: {np.min(temperatures):.2f} °C")
print()

# Find days with high average temperature
threshold = 22.5
hot_days = np.where(daily_means > threshold)[0] + 1  # +1 for 1-indexing
print(f"Days with average > {threshold}°C: {hot_days}")

# %% [markdown]
# ### NumPy Best Practices
# 
# 1. **Use vectorization** - Avoid Python loops, use NumPy operations
# 2. **Preallocate arrays** - Use `np.zeros()` or `np.empty()` instead of appending
# 3. **Use appropriate dtypes** - `float32` vs `float64`, `int32` vs `int64`
# 4. **Broadcasting** - NumPy automatically broadcasts arrays of different shapes
# 5. **In-place operations** - Use `+=`, `-=` to save memory
# 6. **Use built-in functions** - NumPy functions are optimized (C/Fortran)
# 7. **Boolean indexing** - Elegant filtering without loops

# %% [markdown]
# ---
# ## Part 3: Visualization with Matplotlib (30 minutes)
# 
# ### Why Visualization Matters in Research
# 
# Visualization is crucial for:
# 
# - **Exploration**: Understand your data's structure and patterns
# - **Communication**: Present findings to colleagues and reviewers
# - **Validation**: Spot errors, outliers, and unexpected behavior
# - **Publication**: High-quality figures for papers and presentations
# - **Interpretation**: Make complex data accessible
# 
# Matplotlib is Python's foundational plotting library, used by researchers worldwide.

# %%
import matplotlib.pyplot as plt

# Configure matplotlib for better-looking plots
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 10
plt.rcParams['lines.linewidth'] = 2

print("Matplotlib imported and configured!")

# %% [markdown]
# ### Basic Line Plots
# 
# Line plots are ideal for showing trends over time or continuous variables.

# %%
# Create sample data: reaction rate vs temperature
temperatures = np.linspace(20, 100, 9)
reaction_rates = 0.5 * np.exp(0.03 * temperatures) + np.random.normal(0, 1, size=9)

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(temperatures, reaction_rates)
plt.xlabel('Temperature (°C)')
plt.ylabel('Reaction Rate (mol/L/s)')
plt.title('Effect of Temperature on Reaction Rate')
plt.grid(True, alpha=0.3)
plt.show()

# %% [markdown]
# ### Customizing Plots: Colors, Markers, and Styles

# %%
# Same data, better presentation
plt.figure(figsize=(10, 6))
plt.plot(temperatures, reaction_rates, 
         marker='o',           # Add circular markers
         color='steelblue',    # Custom color
         linestyle='-',        # Line style: '-', '--', '-.', ':'
         linewidth=2,
         markersize=8,
         markerfacecolor='white',
         markeredgewidth=2,
         markeredgecolor='steelblue',
         label='Experimental data')

plt.xlabel('Temperature (°C)', fontsize=12)
plt.ylabel('Reaction Rate (mol/L/s)', fontsize=12)
plt.title('Effect of Temperature on Reaction Rate', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3, linestyle='--')
plt.legend()
plt.tight_layout()  # Prevent label cutoff
plt.show()

# %% [markdown]
# ### Scatter Plots
# 
# Scatter plots show relationships between two variables without implying order.

# %%
# Simulate experimental data: concentration vs absorbance
np.random.seed(42)
concentrations = np.array([0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0])
absorbance = 0.15 * concentrations + 0.05 + np.random.normal(0, 0.05, size=10)

# Create scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(concentrations, absorbance,
            s=100,  # Size of markers
            c='crimson',  # Color
            alpha=0.6,  # Transparency
            edgecolors='black',  # Marker edge color
            linewidths=1.5)

# Add best-fit line
z = np.polyfit(concentrations, absorbance, 1)  # Linear fit
p = np.poly1d(z)
plt.plot(concentrations, p(concentrations), 
         'k--', linewidth=2, alpha=0.5, label=f'Fit: y = {z[0]:.3f}x + {z[1]:.3f}')

plt.xlabel('Concentration (mM)', fontsize=12)
plt.ylabel('Absorbance (AU)', fontsize=12)
plt.title('Calibration Curve: Absorbance vs Concentration', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.legend(fontsize=11)
plt.tight_layout()
plt.show()

# %% [markdown]
# ### Multiple Lines on One Plot

# %%
# Compare three experimental conditions
time = np.linspace(0, 10, 50)
control = np.exp(-0.2 * time) + np.random.normal(0, 0.05, 50)
treatment1 = np.exp(-0.3 * time) + np.random.normal(0, 0.05, 50)
treatment2 = np.exp(-0.4 * time) + np.random.normal(0, 0.05, 50)

plt.figure(figsize=(10, 6))
plt.plot(time, control, label='Control', marker='o', markersize=4, linewidth=2)
plt.plot(time, treatment1, label='Treatment A', marker='s', markersize=4, linewidth=2)
plt.plot(time, treatment2, label='Treatment B', marker='^', markersize=4, linewidth=2)

plt.xlabel('Time (hours)', fontsize=12)
plt.ylabel('Concentration (µM)', fontsize=12)
plt.title('Drug Decay Over Time', fontsize=14, fontweight='bold')
plt.legend(fontsize=11, loc='upper right')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# %% [markdown]
# ### Subplots: Multiple Plots in One Figure
# 
# Subplots allow you to compare multiple datasets side by side.

# %%
# Create figure with 2×2 subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Subplot 1: Temperature over time
time_days = np.arange(1, 31)
temperature = 20 + 5 * np.sin(2 * np.pi * time_days / 7) + np.random.normal(0, 1, 30)
axes[0, 0].plot(time_days, temperature, 'o-', color='orangered')
axes[0, 0].set_xlabel('Day')
axes[0, 0].set_ylabel('Temperature (°C)')
axes[0, 0].set_title('Daily Temperature')
axes[0, 0].grid(True, alpha=0.3)

# Subplot 2: Histogram of temperatures
axes[0, 1].hist(temperature, bins=15, color='skyblue', edgecolor='black', alpha=0.7)
axes[0, 1].set_xlabel('Temperature (°C)')
axes[0, 1].set_ylabel('Frequency')
axes[0, 1].set_title('Temperature Distribution')
axes[0, 1].grid(True, alpha=0.3, axis='y')

# Subplot 3: Scatter plot
x = np.random.normal(0, 1, 100)
y = 2 * x + np.random.normal(0, 0.5, 100)
axes[1, 0].scatter(x, y, alpha=0.5, c='green', edgecolors='black')
axes[1, 0].set_xlabel('X variable')
axes[1, 0].set_ylabel('Y variable')
axes[1, 0].set_title('Correlation Analysis')
axes[1, 0].grid(True, alpha=0.3)

# Subplot 4: Bar plot
categories = ['A', 'B', 'C', 'D', 'E']
values = [23, 45, 56, 78, 32]
axes[1, 1].bar(categories, values, color='mediumpurple', edgecolor='black', alpha=0.7)
axes[1, 1].set_xlabel('Category')
axes[1, 1].set_ylabel('Value')
axes[1, 1].set_title('Categorical Data')
axes[1, 1].grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.show()

# %% [markdown]
# ### Advanced Customization: Publication-Quality Figures

# %%
# Create a publication-ready figure
np.random.seed(42)
x = np.linspace(0, 10, 100)
y1 = np.sin(x) + np.random.normal(0, 0.1, 100)
y2 = np.cos(x) + np.random.normal(0, 0.1, 100)

fig, ax = plt.subplots(figsize=(10, 6))

# Plot data with error bands
ax.plot(x, np.sin(x), 'b-', linewidth=2.5, label='Theory: sin(x)')
ax.scatter(x[::5], y1[::5], s=60, c='blue', marker='o', 
           edgecolors='black', linewidths=1, zorder=3, label='Experimental data')

ax.plot(x, np.cos(x), 'r-', linewidth=2.5, label='Theory: cos(x)')
ax.scatter(x[::5], y2[::5], s=60, c='red', marker='s', 
           edgecolors='black', linewidths=1, zorder=3, label='Control data')

# Styling
ax.set_xlabel('Time (s)', fontsize=14, fontweight='bold')
ax.set_ylabel('Amplitude', fontsize=14, fontweight='bold')
ax.set_title('Oscillatory Behavior in Chemical System', fontsize=16, fontweight='bold', pad=20)

# Grid
ax.grid(True, alpha=0.3, linestyle='--', linewidth=0.8)

# Legend
ax.legend(fontsize=11, frameon=True, shadow=True, loc='upper right')

# Spines (borders)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_linewidth(1.5)
ax.spines['bottom'].set_linewidth(1.5)

# Tick parameters
ax.tick_params(axis='both', which='major', labelsize=11, width=1.5, length=6)

plt.tight_layout()
plt.show()

# %% [markdown]
# ### Different Plot Types

# %%
# Demonstrate various plot types useful in research
fig, axes = plt.subplots(2, 3, figsize=(15, 10))

# 1. Line plot with error bars
x = np.arange(0, 10)
y = x ** 1.5
yerr = y * 0.1  # 10% error
axes[0, 0].errorbar(x, y, yerr=yerr, fmt='o-', capsize=5, capthick=2,
                    color='steelblue', ecolor='gray', linewidth=2)
axes[0, 0].set_title('Error Bars', fontweight='bold')
axes[0, 0].set_xlabel('X')
axes[0, 0].set_ylabel('Y')
axes[0, 0].grid(True, alpha=0.3)

# 2. Bar plot
categories = ['Method 1', 'Method 2', 'Method 3', 'Method 4']
performance = [85, 92, 78, 88]
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A']
axes[0, 1].bar(categories, performance, color=colors, edgecolor='black', alpha=0.8)
axes[0, 1].set_title('Method Comparison', fontweight='bold')
axes[0, 1].set_ylabel('Performance (%)')
axes[0, 1].set_ylim(0, 100)
axes[0, 1].grid(True, alpha=0.3, axis='y')

# 3. Histogram
data = np.random.normal(100, 15, 1000)
axes[0, 2].hist(data, bins=30, color='coral', edgecolor='black', alpha=0.7)
axes[0, 2].axvline(np.mean(data), color='red', linestyle='--',
                   linewidth=2, label=f'Mean = {np.mean(data):.1f}')
axes[0, 2].set_title('Distribution', fontweight='bold')
axes[0, 2].set_xlabel('Value')
axes[0, 2].set_ylabel('Frequency')
axes[0, 2].legend()
axes[0, 2].grid(True, alpha=0.3, axis='y')

# 4. Box plot
data1 = np.random.normal(100, 10, 100)
data2 = np.random.normal(110, 15, 100)
data3 = np.random.normal(95, 8, 100)
axes[1, 0].boxplot([data1, data2, data3], labels=['Group A', 'Group B', 'Group C'])
axes[1, 0].set_title('Box Plot Comparison', fontweight='bold')
axes[1, 0].set_ylabel('Measurement')
axes[1, 0].grid(True, alpha=0.3, axis='y')

# 5. Heatmap
matrix = np.random.rand(10, 10)
im = axes[1, 1].imshow(matrix, cmap='viridis', aspect='auto')
axes[1, 1].set_title('Heatmap', fontweight='bold')
axes[1, 1].set_xlabel('X index')
axes[1, 1].set_ylabel('Y index')
plt.colorbar(im, ax=axes[1, 1])

# 6. Filled plot (area)
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.sin(x) + 0.5
axes[1, 2].fill_between(x, y1, y2, alpha=0.5, color='lightgreen', label='Range')
axes[1, 2].plot(x, (y1 + y2) / 2, 'k-', linewidth=2, label='Mean')
axes[1, 2].set_title('Filled Area', fontweight='bold')
axes[1, 2].set_xlabel('X')
axes[1, 2].set_ylabel('Y')
axes[1, 2].legend()
axes[1, 2].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# %% [markdown]
# ### Saving Figures
# 
# Save your figures in various formats for different purposes.

# %%
# Create a figure to save
plt.figure(figsize=(10, 6))
x = np.linspace(0, 10, 100)
plt.plot(x, np.sin(x), 'b-', linewidth=2, label='sin(x)')
plt.plot(x, np.cos(x), 'r--', linewidth=2, label='cos(x)')
plt.xlabel('X', fontsize=12)
plt.ylabel('Y', fontsize=12)
plt.title('Trigonometric Functions', fontsize=14, fontweight='bold')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()

# Save in different formats
# PNG for presentations and web (raster)
plt.savefig('figure_example.png', dpi=300, bbox_inches='tight')

# PDF for publications (vector, scalable)
plt.savefig('figure_example.pdf', bbox_inches='tight')

# SVG for editing in Inkscape/Illustrator (vector)
plt.savefig('figure_example.svg', bbox_inches='tight')

print("Figure saved as:")
print("  - figure_example.png (300 DPI, for presentations)")
print("  - figure_example.pdf (vector, for publications)")
print("  - figure_example.svg (vector, for editing)")

plt.show()

# %% [markdown]
# ### Best Practices for Publication-Quality Figures
# 
# **1. Resolution and Format**
# - Use **300+ DPI** for raster images (PNG, JPG)
# - Prefer **vector formats** (PDF, SVG, EPS) for publications
# - PNG for web/presentations, PDF/SVG for papers
# 
# **2. Fonts and Labels**
# - Use **clear, readable fonts** (11-14pt)
# - **Bold axis labels and titles**
# - Include **units** in axis labels
# - Use **descriptive titles**
# 
# **3. Colors**
# - Use **colorblind-friendly palettes**
# - Consider **grayscale printing**
# - Avoid too many colors (3-5 max)
# - Use **consistent colors** across figures
# 
# **4. Data Presentation**
# - Always include **error bars** when appropriate
# - Add **legends** for multiple series
# - Use **grid lines** sparingly (subtle, alpha < 0.5)
# - Show **raw data points** when possible
# 
# **5. Size and Layout**
# - Match **journal column width** (typically 3.5" or 7" wide)
# - Use **aspect ratios** that fit the data (not always square)
# - `tight_layout()` or `bbox_inches='tight'` to avoid cropping
# 
# **6. Accessibility**
# - Use **markers** and **line styles**, not just colors
# - Add **annotations** for key features
# - Keep it **simple** - remove chart junk
# - Test in **grayscale**

# %%
# Example: Publication-ready figure with all best practices
fig, ax = plt.subplots(figsize=(7, 5))  # Journal column width

# Colorblind-friendly colors
colors = ['#0173B2', '#DE8F05', '#029E73']  # Blue, Orange, Green

# Simulate data with error bars
np.random.seed(42)
x = np.array([1, 2, 3, 4, 5])
y1 = np.array([2.3, 4.1, 5.8, 7.2, 8.9])
y2 = np.array([1.8, 3.9, 5.5, 7.5, 9.2])
y3 = np.array([2.1, 3.7, 5.2, 6.8, 8.5])

err1 = np.array([0.2, 0.3, 0.3, 0.4, 0.4])
err2 = np.array([0.3, 0.2, 0.4, 0.3, 0.5])
err3 = np.array([0.2, 0.3, 0.3, 0.3, 0.4])

# Plot with different markers for accessibility
ax.errorbar(x, y1, yerr=err1, fmt='o-', color=colors[0], linewidth=2.5, 
            markersize=8, capsize=5, capthick=2, label='Method A')
ax.errorbar(x, y2, yerr=err2, fmt='s--', color=colors[1], linewidth=2.5, 
            markersize=8, capsize=5, capthick=2, label='Method B')
ax.errorbar(x, y3, yerr=err3, fmt='^-.', color=colors[2], linewidth=2.5, 
            markersize=8, capsize=5, capthick=2, label='Method C')

# Labels with units
ax.set_xlabel('Concentration (mM)', fontsize=13, fontweight='bold')
ax.set_ylabel('Yield (%)', fontsize=13, fontweight='bold')
ax.set_title('Comparison of Synthesis Methods', fontsize=14, fontweight='bold', pad=15)

# Styling
ax.legend(fontsize=11, frameon=True, loc='upper left')
ax.grid(True, alpha=0.3, linestyle='--')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.tick_params(labelsize=11)

# Set reasonable axis limits
ax.set_ylim(0, 12)
ax.set_xlim(0.5, 5.5)

plt.tight_layout()
plt.savefig('publication_figure.pdf', dpi=300, bbox_inches='tight')
plt.savefig('publication_figure.png', dpi=300, bbox_inches='tight')
print("Publication-quality figure saved!")
plt.show()

# %% [markdown]
# ### Practical Research Example: Complete Analysis with Visualization

# %%
# Complete workflow: data generation → analysis → visualization
np.random.seed(42)

# Simulate a 30-day experiment measuring enzyme activity at different pH levels
days = 30
ph_levels = [5.0, 6.0, 7.0, 8.0]
measurements = {}

# Generate data
for ph in ph_levels:
    # Activity depends on pH (optimal around 7.0)
    optimal_activity = 100 * np.exp(-0.5 * ((ph - 7.0) / 1.5) ** 2)
    daily_activity = optimal_activity + np.random.normal(0, 5, days)
    measurements[ph] = daily_activity

# Analysis
mean_activities = {ph: np.mean(measurements[ph]) for ph in ph_levels}
std_activities = {ph: np.std(measurements[ph]) for ph in ph_levels}

# Visualization
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Plot 1: Time series
time = np.arange(1, days + 1)
for i, ph in enumerate(ph_levels):
    ax1.plot(time, measurements[ph], alpha=0.6, linewidth=1.5, 
             label=f'pH {ph}', color=plt.cm.viridis(i/len(ph_levels)))

ax1.set_xlabel('Day', fontsize=12, fontweight='bold')
ax1.set_ylabel('Enzyme Activity (U/mL)', fontsize=12, fontweight='bold')
ax1.set_title('Enzyme Activity Over Time', fontsize=13, fontweight='bold')
ax1.legend(fontsize=10)
ax1.grid(True, alpha=0.3)

# Plot 2: Summary bar plot with error bars
ph_labels = [f'pH {ph}' for ph in ph_levels]
means = [mean_activities[ph] for ph in ph_levels]
stds = [std_activities[ph] for ph in ph_levels]

bars = ax2.bar(ph_labels, means, yerr=stds, capsize=8, 
               color=plt.cm.viridis(np.linspace(0, 1, len(ph_levels))),
               edgecolor='black', linewidth=1.5, alpha=0.8)

ax2.set_ylabel('Mean Activity (U/mL)', fontsize=12, fontweight='bold')
ax2.set_title('pH Dependence of Enzyme Activity', fontsize=13, fontweight='bold')
ax2.grid(True, alpha=0.3, axis='y')
ax2.set_ylim(0, max(means) * 1.3)

# Add value labels on bars
for i, (bar, mean, std) in enumerate(zip(bars, means, stds)):
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2., height + std + 2,
             f'{mean:.1f}±{std:.1f}',
             ha='center', va='bottom', fontsize=10, fontweight='bold')

plt.tight_layout()
plt.savefig('enzyme_analysis.png', dpi=300, bbox_inches='tight')
print("Complete analysis figure saved!")
plt.show()

# Print statistical summary
print("\nStatistical Summary:")
print("-" * 50)
for ph in ph_levels:
    print(f"pH {ph}: {mean_activities[ph]:.1f} ± {std_activities[ph]:.1f} U/mL")
print(f"\nOptimal pH: {max(mean_activities, key=mean_activities.get)}")

# %% [markdown]
# ---
# ## Summary and Key Takeaways
# 
# ### Part 1: Python Project Structure
# 
# ✓ **Organization matters** - Use packages, modules, and clear directory structure  
# ✓ **Virtual environments** - Isolate dependencies per project  
# ✓ **Document dependencies** - requirements.txt or environment.yml  
# ✓ **Make it a package** - Use __init__.py and setup.py for reusable code  
# ✓ **Version control** - .gitignore data files, track code  
# 
# ### Part 2: NumPy for Scientific Computing
# 
# ✓ **Speed and efficiency** - 10-100x faster than Python lists  
# ✓ **Array creation** - np.array(), np.arange(), np.linspace(), np.zeros(), np.ones()  
# ✓ **Vectorization** - Operations on entire arrays, no loops  
# ✓ **Boolean indexing** - Elegant filtering with conditions  
# ✓ **Statistics** - mean(), std(), min(), max(), median(), percentile()  
# ✓ **Multi-dimensional** - Powerful 2D arrays and matrix operations  
# 
# ### Part 3: Matplotlib for Visualization
# 
# ✓ **Many plot types** - Line, scatter, bar, histogram, heatmap, etc.  
# ✓ **Customization** - Colors, markers, labels, titles, legends  
# ✓ **Subplots** - Multiple plots in one figure  
# ✓ **Publication-quality** - DPI, vector formats, accessibility  
# ✓ **Save figures** - PNG (raster), PDF/SVG (vector)  
# ✓ **Best practices** - Clear labels, error bars, colorblind-friendly, simple  

# %% [markdown]
# ## Next Steps
# 
# In **Lecture 5**, we'll explore:
# - **Pandas** for data manipulation and analysis
# - **Data cleaning** and transformation workflows
# - **Advanced file I/O** (CSV, Excel, HDF5, JSON)
# - **Time series analysis** with real research data
# - **Combining NumPy, Pandas, and Matplotlib** for complete workflows
# 
# ### Practice Exercises
# 
# 1. **Project Structure**: Create a research project with proper structure
#    including src/, tests/, data/, and notebooks/ directories
# 
# 2. **NumPy Practice**: Analyze a matrix of experimental data:
#    - Load or create a 10×5 matrix (10 samples, 5 measurements)
#    - Calculate statistics per sample and per measurement
#    - Identify outliers using boolean indexing
#    - Normalize data to mean=0, std=1
# 
# 3. **Matplotlib Practice**: Create a publication-quality figure:
#    - Generate synthetic data with noise
#    - Create subplots showing raw data, processed data, and distribution
#    - Add proper labels, legends, and styling
#    - Save as both PNG (300 DPI) and PDF
# 
# 4. **Integrated Project**: Build a complete analysis pipeline:
#    - Structure: Organize into proper package
#    - Data: Generate or load experimental data (NumPy)
#    - Analysis: Calculate statistics, fit models
#    - Visualization: Create comprehensive figures (Matplotlib)
#    - Documentation: Add README and docstrings

# %% [markdown]
# ## Additional Resources
# 
# ### Documentation
# - [NumPy Documentation](https://numpy.org/doc/)
# - [NumPy Tutorial](https://numpy.org/doc/stable/user/quickstart.html)
# - [Matplotlib Documentation](https://matplotlib.org/)
# - [Matplotlib Gallery](https://matplotlib.org/stable/gallery/index.html)
# - [Python Packaging Guide](https://packaging.python.org/)
# 
# ### Books
# - "Python for Data Analysis" by Wes McKinney
# - "Effective Python" by Brett Slatkin
# - "Research Software Engineering with Python" (online book)
# 
# ### Tutorials
# - [NumPy Tutorial on SciPy Lectures](http://scipy-lectures.org/intro/numpy/)
# - [Matplotlib Tutorial](https://matplotlib.org/stable/tutorials/index.html)
# - [Real Python: NumPy](https://realpython.com/numpy-tutorial/)

# %% [markdown]
# ## Acknowledgements and References
# 
# This lecture draws from established best practices in scientific Python computing:
# 
# ### Primary Sources
# 
# - **Research Software Engineering with Python** by The Alan Turing Institute  
#   <https://alan-turing-institute.github.io/rse-course/html/>  
#   Project structure patterns, NumPy usage examples, and visualization best practices adapted from this course.
# 
# - **Research Software Engineering with Python** by Damien Irving, Kate Hertweck,
#   Luke Johnston, Joel Ostblom, Charlotte Wickham, and Greg Wilson (2022)
#   <https://third-bit.com/py-rse/>
#   Chapter on "Creating Packages" and "Programming Style" informed our project
#   structure guidance.
# 
# ### Library Documentation
# 
# - **NumPy Documentation**  
#   <https://numpy.org/doc/>  
#   Official NumPy reference for array operations, mathematical functions, and performance tips.
#   - NumPy Quickstart: <https://numpy.org/doc/stable/user/quickstart.html>
#   - Array Creation: <https://numpy.org/doc/stable/user/basics.creation.html>
# 
# - **Matplotlib Documentation**  
#   <https://matplotlib.org/stable/>  
#   Official Matplotlib reference for plotting functions and customization.
#   - Tutorials: <https://matplotlib.org/stable/tutorials/index.html>
#   - Gallery: <https://matplotlib.org/stable/gallery/index.html>
# 
# - **Python Packaging Guide**  
#   <https://packaging.python.org/>  
#   Official Python packaging documentation for project structure and distribution.
# 
# ### Additional References
# 
# - **NumPy Paper**: Harris, C.R., Millman, K.J., van der Walt, S.J. et al.
#   (2020). "Array programming with NumPy". Nature 585, 357–362.
# - **Matplotlib Paper**: Hunter, J. D. (2007). "Matplotlib: A 2D graphics
#   environment". Computing in Science & Engineering, 9(3), 90-95.
# 
# ### Notes
# 
# All examples and exercises have been developed specifically for research software engineering education.
# NumPy and Matplotlib code follows official documentation and community best practices. Project structure
# recommendations synthesize patterns from multiple sources in the scientific Python ecosystem.

# %% [markdown]
# **Great work completing Lecture 4! You now have the tools to organize professional 
# research code and perform numerical computing with visualization. Keep practicing!** 🎉
