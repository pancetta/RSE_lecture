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
# # Lecture 3: Advanced Python & Working with Libraries
# 
# ## Overview
# This lecture continues building on Python fundamentals, covering more advanced concepts 
# and how to work effectively with third-party libraries. We focus on tools commonly used 
# in research software engineering: NumPy for numerical computing, file I/O for data 
# processing, and creating reusable, well-structured code.
# 
# **Duration**: ~90 minutes
# 
# ## Learning Objectives
# - Work with NumPy for efficient numerical computing
# - Read and write data files in various formats
# - Understand list comprehensions and functional programming
# - Create well-structured, modular programs
# - Process and analyze real research data

# %% [markdown]
# ## Working with Third-Party Libraries
# 
# Research software rarely operates in isolation. Third-party libraries provide:
# - **Efficiency**: Optimized implementations of common operations
# - **Reliability**: Well-tested code used by thousands of researchers
# - **Productivity**: Focus on your research, not reinventing the wheel
# 
# ### Installing Libraries
# 
# ```bash
# # Using pip
# pip install numpy pandas matplotlib
# 
# # Using conda/mamba
# conda install numpy pandas matplotlib
# 
# # From requirements.txt
# pip install -r requirements.txt
# ```

# %% [markdown]
# ## NumPy: Numerical Computing in Python
# 
# NumPy is the foundation of scientific Python. It provides:
# - Multi-dimensional arrays (much faster than Python lists)
# - Mathematical functions optimized for arrays
# - Tools for linear algebra, random numbers, and more

# %%
import numpy as np

# Create arrays different ways
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.arange(0, 10, 2)  # Start, stop, step
arr3 = np.linspace(0, 1, 5)  # Start, stop, num_points
arr4 = np.zeros(5)
arr5 = np.ones((3, 3))

print("Array from list:", arr1)
print("Array with arange:", arr2)
print("Array with linspace:", arr3)
print("Array of zeros:", arr4)
print("2D array of ones:\n", arr5)

# %% [markdown]
# ### Array Operations
# 
# NumPy operations are vectorized - they work on entire arrays at once.

# %%
# Generate some experimental data
np.random.seed(42)
temperatures = np.random.normal(25.0, 2.0, 100)  # Mean=25°C, std=2°C

# Array arithmetic (vectorized - much faster than loops!)
temps_fahrenheit = temperatures * 9/5 + 32

# Statistical operations
print(f"Mean temperature: {np.mean(temperatures):.2f}°C")
print(f"Std deviation: {np.std(temperatures):.2f}°C")
print(f"Min temperature: {np.min(temperatures):.2f}°C")
print(f"Max temperature: {np.max(temperatures):.2f}°C")
print(f"Median temperature: {np.median(temperatures):.2f}°C")

# %%
# Boolean indexing - filter data based on conditions
high_temps = temperatures[temperatures > 27]
low_temps = temperatures[temperatures < 23]

print(f"Number of high readings (>27°C): {len(high_temps)}")
print(f"Number of low readings (<23°C): {len(low_temps)}")
print(f"Normal range readings: {100 - len(high_temps) - len(low_temps)}")

# %% [markdown]
# ### Multi-dimensional Arrays
# 
# Research data often comes in matrices or higher dimensions.

# %%
# Create a 2D array representing a grid of measurements
# (e.g., temperature at different locations and times)
measurements = np.random.normal(25, 2, (10, 5))  # 10 time points, 5 locations

print("Shape of data:", measurements.shape)
print(f"Total measurements: {measurements.size}")
print("\nFirst 3 time points, all locations:")
print(measurements[:3, :])

# Operations along axes
time_averages = np.mean(measurements, axis=0)  # Average over time
location_averages = np.mean(measurements, axis=1)  # Average over locations

print(f"\nAverage per location: {time_averages}")
print(f"Average per time point: {location_averages}")

# %% [markdown]
# ## File Input/Output
# 
# Reading and writing data files is essential for research software.

# %% [markdown]
# ### Working with Text Files

# %%
# Writing data to a file
data_to_save = """# Experimental Results
# Date: 2024-01-15
# Experiment: Temperature Monitoring
Sample,Temperature,Humidity
1,25.3,65.2
2,24.8,64.1
3,26.1,63.8
4,25.5,65.5
5,24.9,64.7
"""

# Note: In a real scenario, you would write to an actual file
# with open('experiment_data.csv', 'w') as f:
#     f.write(data_to_save)

print("Data that would be written to file:")
print(data_to_save)

# %% [markdown]
# ### Reading CSV Files with Python's csv Module

# %%
import csv
from io import StringIO

# Simulate reading from a file using StringIO
csv_data = StringIO(data_to_save)

# Skip comment lines and read CSV
rows = []
for line in csv_data:
    if not line.startswith('#'):
        rows.append(line.strip())

# Parse CSV data
csv_content = StringIO('\n'.join(rows))
reader = csv.DictReader(csv_content)

data_dict = {'Sample': [], 'Temperature': [], 'Humidity': []}
for row in reader:
    data_dict['Sample'].append(row['Sample'])
    data_dict['Temperature'].append(float(row['Temperature']))
    data_dict['Humidity'].append(float(row['Humidity']))

print("Parsed data:")
print(f"Samples: {data_dict['Sample']}")
print(f"Temperatures: {data_dict['Temperature']}")
print(f"Humidities: {data_dict['Humidity']}")

# %% [markdown]
# ### NumPy File I/O
# 
# NumPy provides convenient functions for saving and loading arrays.

# %%
# Save array to text file (CSV-like)
sample_data = np.random.rand(5, 3)
print("Data to save:")
print(sample_data)

# In practice, you would use:
# np.savetxt('data.csv', sample_data, delimiter=',', 
#            header='col1,col2,col3', comments='')

# Load from text file:
# loaded_data = np.loadtxt('data.csv', delimiter=',', skiprows=1)

# For binary format (faster, preserves precision):
# np.save('data.npy', sample_data)      # Save
# loaded_data = np.load('data.npy')     # Load

# %% [markdown]
# ## List Comprehensions and Functional Programming
# 
# Python provides elegant ways to transform and filter data.

# %%
# Traditional loop approach
measurements_c = [23.5, 24.1, 25.6, 22.8, 26.3]
measurements_f = []
for temp in measurements_c:
    measurements_f.append(temp * 9/5 + 32)

print("Traditional loop:", measurements_f)

# List comprehension (more Pythonic)
measurements_f = [temp * 9/5 + 32 for temp in measurements_c]
print("List comprehension:", measurements_f)

# %%
# Filter with list comprehension
valid_temps = [temp for temp in measurements_c if 23 <= temp <= 26]
print("Valid temperatures:", valid_temps)

# Conditional transformation
adjusted = [temp if temp >= 24 else 24 for temp in measurements_c]
print("Adjusted (min 24°C):", adjusted)

# %%
# Dictionary comprehension
temp_dict = {f"sample_{i}": temp for i, temp in enumerate(measurements_c, 1)}
print("Temperature dictionary:", temp_dict)

# Invert dictionary
inverted = {v: k for k, v in temp_dict.items()}
print("Inverted:", inverted)

# %% [markdown]
# ## Building a Data Processing Pipeline
# 
# Let's create a complete example that processes research data.

# %%
import string
from collections import Counter

def count_words(text):
    """
    Count word frequencies in text.
    
    Parameters
    ----------
    text : str
        Input text to analyze
        
    Returns
    -------
    collections.Counter
        Word frequency counter object that maps words to their counts
    """
    # Split into words and clean
    words = text.split()
    # Remove punctuation and convert to lowercase
    cleaned = [word.strip(string.punctuation).lower() 
               for word in words if word]
    # Filter out empty strings
    cleaned = [word for word in cleaned if word]
    return Counter(cleaned)


def filter_common_words(word_counts, min_count=2):
    """
    Filter words that appear less than min_count times.
    
    Parameters
    ----------
    word_counts : Counter
        Word frequency counter
    min_count : int
        Minimum number of occurrences
        
    Returns
    -------
    dict
        Filtered word counts
    """
    return {word: count for word, count in word_counts.items() 
            if count >= min_count}


# Example text (simulating a research abstract)
sample_text = """
Research software engineering combines software engineering practices 
with domain research. Software quality and reproducibility are essential 
for research. Good software practices enable better research outcomes.
Testing and documentation improve software reliability.
"""

# Process the text
word_counts = count_words(sample_text)
filtered_counts = filter_common_words(word_counts, min_count=2)

print("All word counts:")
for word, count in word_counts.most_common(10):
    print(f"  {word}: {count}")

print("\nWords appearing 2+ times:")
for word, count in sorted(filtered_counts.items(), 
                          key=lambda x: x[1], reverse=True):
    print(f"  {word}: {count}")

# %% [markdown]
# ## Creating Reusable Modules
# 
# Organize related functions into modules for better code organization.

# %%
class DataProcessor:
    """
    A class for processing experimental data.
    
    This demonstrates object-oriented programming for organizing
    related functionality.
    """
    
    def __init__(self, data, name="Experiment"):
        """
        Initialize the processor.
        
        Parameters
        ----------
        data : array-like
            Experimental data
        name : str
            Name of the experiment
        """
        self.data = np.array(data)
        self.name = name
    
    def get_statistics(self):
        """Calculate and return basic statistics."""
        return {
            'mean': np.mean(self.data),
            'std': np.std(self.data),
            'min': np.min(self.data),
            'max': np.max(self.data),
            'median': np.median(self.data)
        }
    
    def normalize(self, method='zscore'):
        """
        Normalize the data.
        
        Parameters
        ----------
        method : str
            'zscore' or 'minmax'
            
        Returns
        -------
        array
            Normalized data
        """
        if method == 'zscore':
            mean = np.mean(self.data)
            std = np.std(self.data)
            if std == 0:
                return np.zeros_like(self.data)
            return (self.data - mean) / std
        elif method == 'minmax':
            min_val = np.min(self.data)
            max_val = np.max(self.data)
            if max_val == min_val:
                return np.zeros_like(self.data)
            return (self.data - min_val) / (max_val - min_val)
        else:
            raise ValueError(f"Unknown method: {method}")
    
    def find_outliers(self, threshold=2.0):
        """
        Find outliers using z-score method.
        
        Parameters
        ----------
        threshold : float
            Number of standard deviations from mean
            
        Returns
        -------
        array
            Boolean array indicating outliers
        """
        z_scores = np.abs(self.normalize('zscore'))
        return z_scores > threshold


# Use the class
processor = DataProcessor(temperatures, name="Temperature Study")

stats = processor.get_statistics()
print(f"Statistics for {processor.name}:")
for key, value in stats.items():
    print(f"  {key}: {value:.2f}")

outliers = processor.find_outliers(threshold=2.0)
print(f"\nNumber of outliers (>2σ): {np.sum(outliers)}")
print(f"Outlier values: {temperatures[outliers][:5]}...")  # Show first 5

# %% [markdown]
# ## Putting It All Together: A Complete Script
# 
# Here's how you might structure a complete research data processing script:

# %%
def load_and_process_data(filename=None, data=None):
    """
    Load data from file or use provided data, then process it.
    
    Parameters
    ----------
    filename : str, optional
        Path to data file
    data : array-like, optional
        Data array (if not loading from file)
        
    Returns
    -------
    dict
        Processing results
    """
    # Load data (simulated here)
    if data is None:
        # In real code: data = np.loadtxt(filename)
        data = np.random.normal(25, 2, 100)
    
    # Process
    processor = DataProcessor(data, name="Loaded Data")
    stats = processor.get_statistics()
    normalized = processor.normalize('zscore')
    outliers = processor.find_outliers()
    
    return {
        'stats': stats,
        'normalized': normalized,
        'outlier_count': np.sum(outliers),
        'outlier_indices': np.where(outliers)[0]
    }


# Run the pipeline
results = load_and_process_data(data=temperatures)

print("Processing Results:")
print(f"  Mean: {results['stats']['mean']:.2f}")
print(f"  Std: {results['stats']['std']:.2f}")
print(f"  Outliers: {results['outlier_count']}")

# %% [markdown]
# ## Best Practices for Using Libraries
# 
# 1. **Read the documentation**
#    - Understand what a library does before using it
#    - Check version compatibility
# 
# 2. **Pin your dependencies**
#    - Specify exact versions in `requirements.txt` or `environment.yml`
#    - Ensures reproducibility across systems
# 
# 3. **Don't reinvent the wheel**
#    - Use established libraries for common tasks
#    - But understand what they're doing
# 
# 4. **Handle errors from libraries**
#    - Wrap library calls in try-except when appropriate
#    - Provide context-specific error messages
# 
# 5. **Keep dependencies minimal**
#    - Only include libraries you actually use
#    - Fewer dependencies = easier maintenance

# %% [markdown]
# ## Exercise
# 
# Create a complete data analysis script that:
# 
# 1. Generates or loads a dataset (e.g., measurement data)
# 2. Calculates summary statistics
# 3. Identifies and removes outliers
# 4. Saves the cleaned data to a file
# 5. Includes proper documentation and error handling
# 
# Use the patterns and functions we've learned in this lecture.

# %%
# Your solution here
