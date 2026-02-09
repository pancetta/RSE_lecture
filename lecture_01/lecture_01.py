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
# # Lecture 1: Python Basics - Command Line & Introduction to Python
# 
# ## Overview
# This lecture provides a foundation for Research Software Engineering by introducing 
# basic command line usage and fundamental Python programming concepts. This is not a 
# comprehensive Python course, but rather focuses on the essential skills needed for 
# writing research software.
# 
# **Duration**: ~90 minutes
# 
# ## Learning Objectives
# - Understand basic command line navigation
# - Learn fundamental Python syntax and concepts
# - Create simple Python scripts for research tasks
# - Apply best practices in research software development

# %% [markdown]
# ## Part 1: Working with the Command Line
# 
# Research software often needs to be run from the command line, especially when:
# - Processing large datasets
# - Running on remote servers or clusters
# - Automating workflows
# - Integrating with other tools
# 
# ### Essential Command Line Commands
# 
# ```bash
# # Navigate directories
# pwd              # Print working directory
# ls               # List files
# cd directory     # Change directory
# 
# # File operations
# cat file.txt     # Display file contents
# head -n 5 file   # Show first 5 lines
# tail -n 5 file   # Show last 5 lines
# 
# # Running Python scripts
# python script.py           # Run a Python script
# python script.py arg1 arg2 # Run with arguments
# python script.py > out.txt # Redirect output to file
# ```

# %% [markdown]
# ## Part 2: Python Fundamentals
# 
# ### Variables and Data Types
# 
# Python is dynamically typed - you don't need to declare variable types explicitly.

# %%
# Basic data types
name = "Research Project"  # String
count = 42                 # Integer
temperature = 98.6         # Float
is_valid = True           # Boolean

print(f"Project: {name}")
print(f"Sample count: {count}")
print(f"Temperature: {temperature}°F")
print(f"Data is valid: {is_valid}")

# %% [markdown]
# ### Collections: Lists and Dictionaries
# 
# Lists and dictionaries are fundamental data structures in Python.

# %%
# Lists - ordered, mutable sequences
measurements = [23.5, 24.1, 23.8, 24.3, 23.9]
print("Measurements:", measurements)
print("First measurement:", measurements[0])
print("Last measurement:", measurements[-1])

# Add a new measurement
measurements.append(24.0)
print("After adding:", measurements)

# %%
# Dictionaries - key-value pairs
experiment = {
    'name': 'Temperature Study',
    'duration': 30,
    'samples': 150,
    'temperature': 25.0
}

print("Experiment:", experiment['name'])
print("Duration:", experiment['duration'], "days")

# Add new information
experiment['location'] = 'Lab A'
print("Updated experiment:", experiment)

# %% [markdown]
# ### Control Flow
# 
# Control structures allow you to make decisions and repeat operations.

# %%
# If statements
threshold = 24.0

for measurement in measurements:
    if measurement > threshold:
        print(f"{measurement} is above threshold")
    elif measurement < threshold:
        print(f"{measurement} is below threshold")
    else:
        print(f"{measurement} equals threshold")

# %%
# For loops - iterate over sequences
data_files = ['exp1.csv', 'exp2.csv', 'exp3.csv']

print("Processing files:")
for filename in data_files:
    print(f"  - {filename}")

# %%
# While loops - repeat while condition is true
count = 0
total = 0

while count < 5:
    total += measurements[count]
    count += 1

average = total / count
print(f"Average of first {count} measurements: {average:.2f}")

# %% [markdown]
# ### Functions
# 
# Functions help organize code into reusable pieces. In research software, 
# functions make analysis reproducible and easier to test.

# %%
def calculate_mean(values):
    """
    Calculate the arithmetic mean of a list of values.
    
    Parameters
    ----------
    values : list
        A list of numeric values
        
    Returns
    -------
    float
        The mean of the values
    """
    if len(values) == 0:
        return 0
    return sum(values) / len(values)


def calculate_std(values, mean=None):
    """
    Calculate the standard deviation of values.
    
    Parameters
    ----------
    values : list
        A list of numeric values
    mean : float, optional
        Pre-calculated mean (computed if not provided)
        
    Returns
    -------
    float
        The standard deviation
    """
    if len(values) == 0:
        return 0
    
    if mean is None:
        mean = calculate_mean(values)
    
    variance = sum((x - mean) ** 2 for x in values) / len(values)
    return variance ** 0.5


# Use our functions
mean = calculate_mean(measurements)
std = calculate_std(measurements, mean)

print(f"Mean: {mean:.2f}")
print(f"Standard Deviation: {std:.2f}")

# %% [markdown]
# ## Part 3: Creating Command-Line Scripts
# 
# ### Programs and Modules
# 
# To create a Python program that runs from the command line, we use a special pattern:

# %%
def main():
    """Main function for our program."""
    print("Hello from a command-line program!")


# This block only runs when the script is executed directly
if __name__ == '__main__':
    main()

# %% [markdown]
# The `if __name__ == '__main__'` check is crucial:
# - When you run a Python file directly: `__name__` equals `"__main__"`
# - When you import a Python file as a module: `__name__` equals the module name
# 
# This pattern allows the same file to be used both as:
# 1. A standalone program
# 2. A module that other programs can import

# %% [markdown]
# ### Handling Command-Line Arguments
# 
# The `argparse` library helps create professional command-line interfaces.

# %%
import argparse

def process_data(input_file, output_file, verbose=False):
    """
    Process data from input file and write to output file.
    
    Parameters
    ----------
    input_file : str
        Path to input file
    output_file : str
        Path to output file
    verbose : bool
        Whether to print progress messages
    """
    if verbose:
        print(f"Reading from: {input_file}")
        print(f"Writing to: {output_file}")
    
    # In a real program, we would process the data here
    return f"Processed {input_file} -> {output_file}"


# Example of how argparse would be used in a script:
# (This is just for demonstration - it won't work in a notebook)
"""
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Process research data files.'
    )
    parser.add_argument('input', help='Input data file')
    parser.add_argument('output', help='Output file')
    parser.add_argument('-v', '--verbose', action='store_true',
                       help='Print progress messages')
    
    args = parser.parse_args()
    process_data(args.input, args.output, args.verbose)
"""

# Simulate what happens when we call the function
result = process_data("data.csv", "results.csv", verbose=True)
print(result)

# %% [markdown]
# ### Documentation Strings (Docstrings)
# 
# Good documentation is essential for research software. Docstrings serve as:
# - Inline documentation for users
# - Reference material for collaborators
# - Foundation for automated documentation tools

# %%
def analyze_experiment(data, control_group=None):
    """
    Analyze experimental data against a control group.
    
    This function performs basic statistical analysis comparing
    experimental data to a control group. It calculates means,
    standard deviations, and the difference between groups.
    
    Parameters
    ----------
    data : list of float
        Experimental measurements
    control_group : list of float, optional
        Control group measurements for comparison
        
    Returns
    -------
    dict
        Dictionary containing:
        - 'mean': mean of data
        - 'std': standard deviation of data
        - 'control_mean': mean of control (if provided)
        - 'difference': difference from control (if provided)
        
    Examples
    --------
    >>> data = [10.2, 10.5, 10.3, 10.4]
    >>> result = analyze_experiment(data)
    >>> print(result['mean'])
    10.35
    """
    result = {
        'mean': calculate_mean(data),
        'std': calculate_std(data)
    }
    
    if control_group:
        control_mean = calculate_mean(control_group)
        result['control_mean'] = control_mean
        result['difference'] = result['mean'] - control_mean
    
    return result


# Test the function
experimental_data = [10.2, 10.5, 10.3, 10.4, 10.6]
control_data = [9.8, 9.9, 9.7, 10.0, 9.9]

results = analyze_experiment(experimental_data, control_data)
print("Analysis Results:")
for key, value in results.items():
    print(f"  {key}: {value:.3f}")

# Access the docstring
print("\nFunction documentation:")
print(analyze_experiment.__doc__)

# %% [markdown]
# ## Best Practices for Research Software
# 
# 1. **Write clear, self-documenting code**
#    - Use meaningful variable names
#    - Add docstrings to functions
#    - Comment complex logic
# 
# 2. **Keep functions focused**
#    - Each function should do one thing well
#    - Avoid functions that are too long (>50 lines often indicates a problem)
# 
# 3. **Handle errors gracefully**
#    - Check for invalid inputs
#    - Provide helpful error messages
# 
# 4. **Make code reusable**
#    - Write functions instead of copying code
#    - Organize related functions into modules
# 
# 5. **Follow Python conventions**
#    - PEP 8 style guide for formatting
#    - Use snake_case for functions and variables
#    - Use descriptive names

# %% [markdown]
# ## Exercise
# 
# Write a command-line script that:
# 1. Takes a list of numbers as input
# 2. Calculates and prints the mean and standard deviation
# 3. Identifies any outliers (values more than 2 standard deviations from the mean)
# 
# Try to use the functions we've defined and follow the patterns shown above.

# %%
# Your solution here
def find_outliers(values, threshold=2.0):
    """
    Find outliers in a dataset.
    
    Parameters
    ----------
    values : list
        Numeric values to analyze
    threshold : float
        Number of standard deviations to use as threshold
        
    Returns
    -------
    list
        List of outlier values
    """
    # Your code here
    pass
