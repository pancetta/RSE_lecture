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
# 
# ### Tests at Different Scales
# 
# | Level of Test | Area Covered | Notes |
# |--------------|--------------|-------|
# | **Unit testing** | Smallest logical block (often < 10 lines) | Should run fast (~1/100th sec), no network/disk access |
# | **Component testing** | Several logical blocks together | Useful for testing integration with 3rd party libraries |
# | **Integration testing** | All components / whole program | Can take longer, run less frequently |
# 
# ### Testing Vocabulary
# 
# - **Fixture**: Input data for tests
# - **Action**: Function being tested
# - **Expected result**: The output that should be obtained
# - **Actual result**: The output that is obtained
# - **Coverage**: Proportion of code paths that tests execute
# - **Regression test**: Test ensuring code behaves the same way after changes

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
# 
# ### Branch Coverage
# 
# Ensure you test all conditional paths:
# ```python
# if energy > 0:
#     # Do this - needs a test
# else:
#     # Do that - also needs a test
# ```
# 
# ## Mocking in Tests
# 
# **Mocking** means replacing real objects with pretend ones that record how they're called.
# This is useful when testing code that interacts with:
# - External APIs or web services
# - Databases
# - File systems
# - Slow or unreliable resources
# 
# ### Example: Mocking with unittest.mock
# 
# ```python
# from unittest.mock import Mock, patch
# 
# # Create a mock object
# mock_function = Mock(return_value=42)
# result = mock_function(1, 2, 3)  # Returns 42
# 
# # Check how it was called
# mock_function.assert_called_with(1, 2, 3)
# 
# # Patch a function temporarily
# with patch('requests.get') as mock_get:
#     mock_get.return_value.status_code = 200
#     # Your test code here
#     mock_get.assert_called_once()
# ```
# 
# ## Regression Testing
# 
# Regression tests ensure code behavior doesn't change unexpectedly:
# - Run program as a "black box"
# - Compare output against known reference output
# - Doesn't test correctness, but consistency
# - Particularly useful for legacy code
# 
# ### Regression Test Workflow
# 1. Set up input data
# 2. Run the program
# 3. Capture the output
# 4. Compare against expected/reference output
# 
# ## Debugging Techniques
# 
# When tests fail, use these debugging approaches:
# - **Print statements**: Quick but temporary
# - **Debugger (pdb)**: Step through code line by line
# - **Logging**: Better than print for production code
# - **Git bisect**: Find which commit introduced a bug

# %% [markdown]
# ## Continuous Integration (CI)
# 
# CI automatically runs your tests whenever you push code:
# - **Catches bugs early**: Before they reach production
# - **Ensures code works across different environments**: Multiple OS, Python versions
# - **Provides fast feedback**: Know immediately if changes break anything
# - **Common tools**: GitHub Actions, Travis CI, GitLab CI, CircleCI
# 
# ### Example: GitHub Actions Workflow
# 
# ```yaml
# name: Tests
# 
# on: [push, pull_request]
# 
# jobs:
#   test:
#     runs-on: ubuntu-latest
#     steps:
#       - uses: actions/checkout@v2
#       - name: Set up Python
#         uses: actions/setup-python@v2
#         with:
#           python-version: '3.9'
#       - name: Install dependencies
#         run: |
#           pip install -r requirements.txt
#           pip install pytest pytest-cov
#       - name: Run tests
#         run: pytest --cov=.
# ```
# 
# ### CI Best Practices
# 
# 1. **Keep tests fast**: Slow tests discourage frequent commits
# 2. **Test on multiple platforms**: Linux, macOS, Windows
# 3. **Test multiple Python versions**: Ensure compatibility
# 4. **Fail fast**: Stop on first failure to save time
# 5. **Monitor coverage**: Track if coverage decreases over time
# 
# ## Summary: Testing Checklist
# 
# When developing research software:
# - ✅ Write unit tests for all functions
# - ✅ Test edge cases (empty input, zeros, negative numbers, etc.)
# - ✅ Use mocks for external dependencies
# - ✅ Aim for >80% test coverage on critical code
# - ✅ Set up CI to run tests automatically
# - ✅ Write regression tests for bug fixes
# - ✅ Use a debugger when tests fail
