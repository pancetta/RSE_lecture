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
# # Lecture 2: Testing and Continuous Integration
# 
# ## Overview
# This lecture covers testing strategies for research software, including unit testing, 
# integration testing, and setting up continuous integration pipelines.
# 
# ## Learning Objectives
# - Understand different types of software tests
# - Learn to write unit tests with pytest
# - Explore continuous integration concepts

# %% [markdown]
# ## Why Testing Matters in Research
# 
# Testing is crucial for:
# - **Correctness**: Ensuring your code does what you think it does
# - **Confidence**: Making changes without fear of breaking things
# - **Documentation**: Tests serve as examples of how to use your code
# - **Reproducibility**: Validated code produces reliable results

# %%
import numpy as np

def normalize_data(data, method='minmax'):
    """
    Normalize data using different methods.
    
    Parameters
    ----------
    data : array-like
        Input data to normalize
    method : str
        Normalization method: 'minmax' or 'zscore'
        
    Returns
    -------
    array-like
        Normalized data
    """
    data = np.array(data)
    
    if method == 'minmax':
        # Min-max normalization: (x - min) / (max - min)
        min_val = np.min(data)
        max_val = np.max(data)
        if max_val == min_val:
            return np.zeros_like(data)
        return (data - min_val) / (max_val - min_val)
    
    elif method == 'zscore':
        # Z-score normalization: (x - mean) / std
        mean = np.mean(data)
        std = np.std(data)
        if std == 0:
            return np.zeros_like(data)
        return (data - mean) / std
    
    else:
        raise ValueError(f"Unknown normalization method: {method}")

# Example usage
sample_data = [1, 2, 3, 4, 5, 10, 15, 20]
normalized_minmax = normalize_data(sample_data, method='minmax')
normalized_zscore = normalize_data(sample_data, method='zscore')

print("Original data:", sample_data)
print("Min-max normalized:", normalized_minmax)
print("Z-score normalized:", normalized_zscore)

# %% [markdown]
# ## Writing Unit Tests
# 
# Unit tests verify that individual functions work correctly. Here's an example 
# of how we would test our `normalize_data` function:
# 
# ```python
# import pytest
# import numpy as np
# 
# def test_normalize_minmax():
#     data = [0, 5, 10]
#     result = normalize_data(data, method='minmax')
#     expected = [0.0, 0.5, 1.0]
#     np.testing.assert_array_almost_equal(result, expected)
# 
# def test_normalize_zscore():
#     data = [1, 2, 3, 4, 5]
#     result = normalize_data(data, method='zscore')
#     # After z-score normalization, mean should be ~0, std should be ~1
#     assert abs(np.mean(result)) < 1e-10
#     assert abs(np.std(result) - 1.0) < 1e-10
# 
# def test_normalize_invalid_method():
#     with pytest.raises(ValueError):
#         normalize_data([1, 2, 3], method='invalid')
# ```

# %%
# Let's visualize the difference between normalization methods
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# Original data
axes[0].bar(range(len(sample_data)), sample_data, color='blue', alpha=0.7)
axes[0].set_title('Original Data')
axes[0].set_xlabel('Index')
axes[0].set_ylabel('Value')
axes[0].grid(True, alpha=0.3)

# Min-max normalized
axes[1].bar(range(len(normalized_minmax)), normalized_minmax, color='green', alpha=0.7)
axes[1].set_title('Min-Max Normalized')
axes[1].set_xlabel('Index')
axes[1].set_ylabel('Value')
axes[1].grid(True, alpha=0.3)

# Z-score normalized
axes[2].bar(range(len(normalized_zscore)), normalized_zscore, color='red', alpha=0.7)
axes[2].set_title('Z-Score Normalized')
axes[2].set_xlabel('Index')
axes[2].set_ylabel('Value')
axes[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# %% [markdown]
# ## Test Coverage
# 
# Test coverage measures what percentage of your code is executed by tests.
# - Aim for high coverage (>80%) in critical code
# - 100% coverage doesn't mean bug-free code
# - Focus on testing important functionality and edge cases

# %% [markdown]
# ## Continuous Integration (CI)
# 
# CI automatically runs your tests whenever you push code:
# - Catches bugs early
# - Ensures code works across different environments
# - Common tools: GitHub Actions, Travis CI, GitLab CI
