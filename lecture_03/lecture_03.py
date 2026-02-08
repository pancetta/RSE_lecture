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
# # Lecture 3: Documentation and Code Quality
# 
# ## Overview
# This lecture focuses on writing good documentation, maintaining code quality,
# and using tools to automate quality checks.
# 
# ## Learning Objectives
# - Learn to write effective documentation
# - Understand code quality metrics
# - Explore automated code quality tools

# %% [markdown]
# ## The Importance of Documentation
# 
# Good documentation is essential for:
# - **Usability**: Helping others (and future you) use your code
# - **Maintenance**: Making it easier to update and fix bugs
# - **Collaboration**: Enabling others to contribute
# - **Impact**: Increasing the likelihood your software will be used and cited

# %% [markdown]
# ## Types of Documentation
# 
# 1. **Code comments**: Explain why, not what
# 2. **Docstrings**: Document functions, classes, and modules
# 3. **README**: Project overview and quick start guide
# 4. **Tutorials**: Step-by-step guides for common tasks
# 5. **API documentation**: Comprehensive reference for all features

# %%
import numpy as np
from typing import List, Tuple, Optional

class DataAnalyzer:
    """
    A class for analyzing numerical data.
    
    This class provides methods for statistical analysis and visualization
    of numerical datasets.
    
    Parameters
    ----------
    data : array-like
        The input data to analyze
    name : str, optional
        A name for the dataset (default: "Dataset")
        
    Attributes
    ----------
    data : np.ndarray
        The stored data as a numpy array
    name : str
        The name of the dataset
        
    Examples
    --------
    >>> analyzer = DataAnalyzer([1, 2, 3, 4, 5], name="Sample")
    >>> analyzer.get_summary()
    {'count': 5, 'mean': 3.0, 'std': 1.41...}
    """
    
    def __init__(self, data: List[float], name: str = "Dataset"):
        self.data = np.array(data)
        self.name = name
        
    def get_summary(self) -> dict:
        """
        Calculate summary statistics for the data.
        
        Returns
        -------
        dict
            Dictionary containing count, mean, std, min, and max
            
        Examples
        --------
        >>> analyzer = DataAnalyzer([1, 2, 3, 4, 5])
        >>> stats = analyzer.get_summary()
        >>> stats['mean']
        3.0
        """
        return {
            'count': len(self.data),
            'mean': np.mean(self.data),
            'std': np.std(self.data),
            'min': np.min(self.data),
            'max': np.max(self.data)
        }
    
    def find_outliers(self, threshold: float = 3.0) -> Tuple[np.ndarray, np.ndarray]:
        """
        Find outliers using the z-score method.
        
        Points with |z-score| > threshold are considered outliers.
        
        Parameters
        ----------
        threshold : float, optional
            Z-score threshold for outlier detection (default: 3.0)
            
        Returns
        -------
        outlier_indices : np.ndarray
            Indices of outlier points
        outlier_values : np.ndarray
            Values of outlier points
            
        Notes
        -----
        This method assumes the data is normally distributed.
        For non-normal distributions, consider using other methods
        like IQR (Interquartile Range).
        """
        mean = np.mean(self.data)
        std = np.std(self.data)
        
        if std == 0:
            return np.array([]), np.array([])
        
        z_scores = np.abs((self.data - mean) / std)
        outlier_mask = z_scores > threshold
        outlier_indices = np.where(outlier_mask)[0]
        outlier_values = self.data[outlier_mask]
        
        return outlier_indices, outlier_values

# Example usage
data_with_outliers = [1, 2, 2, 3, 3, 3, 4, 4, 5, 100]
analyzer = DataAnalyzer(data_with_outliers, name="Sample with Outliers")

# Get summary statistics
summary = analyzer.get_summary()
print(f"Summary for {analyzer.name}:")
for key, value in summary.items():
    print(f"  {key}: {value:.2f}")

# Find outliers
outlier_idx, outlier_vals = analyzer.find_outliers(threshold=2.0)
print(f"\nOutliers found at indices: {outlier_idx}")
print(f"Outlier values: {outlier_vals}")

# %% [markdown]
# ## Code Quality Metrics
# 
# Important metrics for code quality:
# - **Complexity**: Cyclomatic complexity (aim for < 10)
# - **Duplication**: Avoid copy-paste code
# - **Naming**: Use clear, descriptive names
# - **Length**: Keep functions short and focused
# - **Style**: Follow language conventions (e.g., PEP 8 for Python)

# %%
# Visualize the data and outliers
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Box plot
axes[0].boxplot(data_with_outliers, vert=True)
axes[0].set_title('Box Plot - Outliers Visible')
axes[0].set_ylabel('Value')
axes[0].grid(True, alpha=0.3)

# Scatter plot with outliers highlighted
normal_mask = np.ones(len(data_with_outliers), dtype=bool)
normal_mask[outlier_idx] = False

axes[1].scatter(np.arange(len(data_with_outliers))[normal_mask], 
                np.array(data_with_outliers)[normal_mask],
                color='blue', alpha=0.6, s=100, label='Normal')
axes[1].scatter(outlier_idx, outlier_vals,
                color='red', alpha=0.8, s=150, marker='*', label='Outliers')
axes[1].set_title('Scatter Plot - Outliers Highlighted')
axes[1].set_xlabel('Index')
axes[1].set_ylabel('Value')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# %% [markdown]
# ## Automated Quality Tools
# 
# Tools to help maintain code quality:
# 
# ### Linters
# - **pylint**: Comprehensive Python linter
# - **flake8**: Style guide enforcement
# - **black**: Automatic code formatter
# 
# ### Type Checkers
# - **mypy**: Static type checker for Python
# 
# ### Documentation Generators
# - **Sphinx**: Generate HTML documentation from docstrings
# - **MkDocs**: Markdown-based documentation
# 
# Example usage:
# ```bash
# # Install tools
# pip install pylint flake8 black mypy sphinx
# 
# # Run linter
# pylint my_module.py
# 
# # Format code
# black my_module.py
# 
# # Type check
# mypy my_module.py
# ```

# %% [markdown]
# ## Best Practices for Documentation
# 
# 1. **Write documentation as you code**: Don't leave it for later
# 2. **Keep it up to date**: Update docs when you change code
# 3. **Include examples**: Show how to use your code
# 4. **Explain the why**: Comments should explain reasoning, not mechanics
# 5. **Use standard formats**: Follow NumPy or Google docstring conventions

# %% [markdown]
# ## Exercise
# 
# 1. Review the `DataAnalyzer` class documentation. Is anything missing?
# 2. Add a new method `remove_outliers()` that returns a new `DataAnalyzer` with outliers removed
# 3. Write comprehensive documentation for your new method
# 4. What edge cases should you document?
