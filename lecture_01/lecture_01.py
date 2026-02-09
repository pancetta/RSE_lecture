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
# # Lecture 1: Introduction to Research Software Engineering
# 
# ## Overview
# This lecture introduces the fundamental concepts of Research Software Engineering (RSE), 
# including best practices, tools, and methodologies for developing high-quality research software.
# 
# ## Learning Objectives
# - Understand what Research Software Engineering is
# - Learn about version control and its importance
# - Explore best practices for writing research code

# %% [markdown]
# ## What is Research Software Engineering?
# 
# Research Software Engineering (RSE) combines professional software engineering practices 
# with domain-specific research knowledge. It focuses on:
# 
# - **Reproducibility**: Ensuring research results can be reproduced
# - **Sustainability**: Creating software that can be maintained long-term
# - **Collaboration**: Enabling effective teamwork on research projects
# - **Quality**: Writing robust, tested, and documented code

# %%
# Example: A simple research function
import numpy as np
import matplotlib.pyplot as plt

def calculate_statistics(data):
    """
    Calculate basic statistics for a dataset.
    
    Parameters
    ----------
    data : array-like
        Input data
        
    Returns
    -------
    dict
        Dictionary containing mean, median, and std
    """
    return {
        'mean': np.mean(data),
        'median': np.median(data),
        'std': np.std(data)
    }

# Generate sample data
np.random.seed(42)
sample_data = np.random.normal(100, 15, 1000)

# Calculate statistics
stats = calculate_statistics(sample_data)
print(f"Mean: {stats['mean']:.2f}")
print(f"Median: {stats['median']:.2f}")
print(f"Standard Deviation: {stats['std']:.2f}")

# %% [markdown]
# ## Version Control with Git
# 
# Version control is a tool for **managing changes** to a set of files.
# 
# ### Why use version control?
# 
# - **Better kind of backup**: Never lose your work
# - **Review history**: "When did I introduce this bug?"
# - **Restore older code versions**: Undo mistakes easily
# - **Ability to undo mistakes**: Safe experimentation
# - **Maintain several versions**: Work on features independently
# - **Collaboration**: Share code and merge changes from multiple contributors
# 
# ### Git vs GitHub
# 
# - **Git**: Version control system tool to manage source code history
# - **GitHub**: Hosting service for Git repositories (alternatives: GitLab, Bitbucket)
# 
# ### Essential Git Commands
# 
# ```bash
# # Initialize a new repository
# git init
# 
# # Check status of your repository
# git status
# 
# # Stage changes for commit
# git add filename.py        # Add specific file
# git add .                  # Add all changes
# 
# # Commit changes with a message
# git commit -m "Description of changes"
# 
# # View commit history
# git log
# 
# # Connect to remote repository
# git remote add origin https://github.com/username/repo.git
# 
# # Push changes to remote
# git push origin main
# 
# # Pull changes from remote
# git pull origin main
# ```
# 
# ### Collaboration Workflow
# 
# When working with others:
# 1. **Clone** the repository: `git clone <url>`
# 2. **Pull** latest changes before starting work: `git pull`
# 3. Make your changes and **commit** them locally
# 4. **Pull** again to get any new changes from collaborators
# 5. Resolve any **merge conflicts** if they arise
# 6. **Push** your changes: `git push`
# 
# ### Handling Merge Conflicts
# 
# When two people edit the same lines of code, Git can't automatically merge:
# - Git marks the conflicted areas in the file with `<<<<<<<`, `=======`, and `>>>>>>>`
# - Manually edit the file to resolve the conflict
# - Stage and commit the resolved file
# 
# ### Branching Basics
# 
# Branches allow you to work on features independently:
# ```bash
# # Create a new branch
# git branch feature-name
# 
# # Switch to the branch
# git checkout feature-name
# 
# # Or do both at once
# git checkout -b feature-name
# 
# # Merge branch back to main
# git checkout main
# git merge feature-name
# ```

# %%
# Visualize our sample data
plt.figure(figsize=(10, 6))
plt.hist(sample_data, bins=30, alpha=0.7, color='blue', edgecolor='black')
plt.axvline(stats['mean'], color='red', linestyle='--', linewidth=2, label=f"Mean: {stats['mean']:.2f}")
plt.axvline(stats['median'], color='green', linestyle='--', linewidth=2, label=f"Median: {stats['median']:.2f}")
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Distribution of Sample Data')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# %% [markdown]
# ## Best Practices
# 
# 1. **Write clear, documented code**: Use docstrings and comments
# 2. **Follow style guides**: PEP 8 for Python
# 3. **Use version control**: Git for tracking changes
# 4. **Test your code**: Write unit tests
# 5. **Make it reproducible**: Document dependencies and environment
