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
# # Lecture 2: Advanced Git, GitHub, GitLab, and Python Basics
# 
# ## Overview
# This lecture builds on Git fundamentals from Lecture 1, introduces collaboration with GitHub and GitLab,
# and begins our journey into Python programming. We'll learn advanced version control workflows
# and start writing our first Python code.
# 
# **Duration**: ~90 minutes
# 
# ## Learning Objectives
# - Master Git branching and merging workflows
# - Understand .gitignore patterns and file management
# - Collaborate effectively using GitHub and GitLab
# - Understand differences between GitHub and GitLab workflows
# - Learn fundamental Python syntax and concepts
# - Write basic Python programs

# %% [markdown]
# ## Part 1: Advanced Git Concepts
# 
# ### Git Branching
# 
# Branches allow you to work on different features or experiments without affecting the main codebase.
# 
# #### Why Use Branches?
# 
# - **Isolation**: Work on new features without breaking the main code
# - **Collaboration**: Multiple people can work simultaneously
# - **Experimentation**: Try new ideas safely
# - **Organization**: Separate development, testing, and production code
# 
# #### Basic Branch Commands
# 
# ```bash
# # Create a new branch
# git branch feature-analysis
# 
# # List all branches (* marks current branch)
# git branch
# 
# # Switch to a branch
# git checkout feature-analysis
# 
# # Create and switch in one command
# git checkout -b new-feature
# 
# # Modern alternative (Git 2.23+)
# git switch feature-analysis
# git switch -c new-feature
# ```

# %% [markdown]
# ### Branching Workflow Example
# 
# Let's walk through a typical workflow:
# 
# ```bash
# # Start on main branch
# git checkout main
# 
# # Create a new feature branch
# git checkout -b add-statistics
# 
# # Make changes to your code
# # ... edit files ...
# 
# # Stage and commit changes
# git add analysis.py
# git commit -m "Add mean and median calculations"
# 
# # More changes
# # ... edit files ...
# git add analysis.py
# git commit -m "Add standard deviation calculation"
# 
# # View your branch history
# git log --oneline --graph
# ```

# %% [markdown]
# ### Merging Branches
# 
# Once your feature is complete, merge it back into the main branch.
# 
# #### Fast-Forward Merge
# 
# When main hasn't changed since you branched:
# 
# ```bash
# # Switch to main
# git checkout main
# 
# # Merge feature branch
# git merge add-statistics
# 
# # Delete the feature branch (optional)
# git branch -d add-statistics
# ```
# 
# #### Three-Way Merge
# 
# When both branches have new commits:
# 
# ```bash
# # Git creates a merge commit
# git checkout main
# git merge add-statistics
# 
# # Git will open an editor for merge commit message
# # Save and close to complete the merge
# ```

# %% [markdown]
# ### Handling Merge Conflicts
# 
# Conflicts occur when the same lines are changed in both branches.
# 
# ```bash
# # When a conflict occurs
# git merge feature-branch
# # Auto-merging file.py
# # CONFLICT (content): Merge conflict in file.py
# # Automatic merge failed; fix conflicts and then commit the result.
# 
# # Check which files have conflicts
# git status
# 
# # Open conflicted files - you'll see markers like:
# # <<<<<<< HEAD
# # Your changes
# # =======
# # Their changes
# # >>>>>>> feature-branch
# 
# # Edit files to resolve conflicts
# # Remove conflict markers
# # Keep the code you want
# 
# # Stage resolved files
# git add file.py
# 
# # Complete the merge
# git commit -m "Merge feature-branch, resolved conflicts"
# ```

# %% [markdown]
# ### The .gitignore File
# 
# Not all files should be tracked by Git. Use `.gitignore` to exclude:
# - Build artifacts and compiled code
# - Dependencies (like `node_modules/`, `venv/`)
# - Temporary files
# - Sensitive data (passwords, API keys)
# - Large data files
# 
# #### Common .gitignore Patterns
# 
# ```gitignore
# # Python
# __pycache__/
# *.pyc
# *.pyo
# *.pyd
# .Python
# venv/
# env/
# *.egg-info/
# dist/
# build/
# 
# # Jupyter
# .ipynb_checkpoints/
# *.ipynb_checkpoints
# 
# # Data files (be careful with research data!)
# *.csv
# *.dat
# data/*.txt
# 
# # OS files
# .DS_Store
# Thumbs.db
# 
# # IDE
# .vscode/
# .idea/
# *.swp
# 
# # Specific files
# secrets.txt
# config_local.py
# ```
# 
# Create a `.gitignore` file in your repository root and Git will automatically ignore matching files.

# %% [markdown]
# ### Best Practices for Branching
# 
# 1. **Keep branches focused**: One feature or fix per branch
# 2. **Use descriptive names**: `fix-data-loading` not `temp` or `test`
# 3. **Merge or delete completed branches**: Don't let them pile up
# 4. **Pull before you push**: Get latest changes from remote
# 5. **Commit often on branches**: Makes it easier to track progress

# %% [markdown]
# ## Part 2: GitHub Collaboration
# 
# ### GitHub Workflow Basics
# 
# GitHub extends Git with collaboration features:
# 
# #### Forking a Repository
# 
# - Click "Fork" on GitHub to create your own copy
# - Clone your fork locally
# - Make changes on a branch
# - Push to your fork
# - Create a Pull Request to propose changes
# 
# #### Pull Requests (PRs)
# 
# A Pull Request is a request to merge your changes into another repository:
# 
# 1. **Create**: After pushing a branch to GitHub, click "New Pull Request"
# 2. **Describe**: Explain what changes you made and why
# 3. **Review**: Others can comment on your code
# 4. **Update**: Push new commits to address feedback
# 5. **Merge**: Maintainer merges when ready
# 
# #### Working with Remotes
# 
# ```bash
# # View remote repositories
# git remote -v
# 
# # Add a remote (e.g., upstream original)
# git remote add upstream https://github.com/original/repo.git
# 
# # Fetch changes from remote
# git fetch origin
# git fetch upstream
# 
# # Pull changes (fetch + merge)
# git pull origin main
# 
# # Push your changes
# git push origin my-branch
# ```

# %% [markdown]
# ### GitHub Best Practices
# 
# 1. **Write clear PR descriptions**: Explain the problem and solution
# 2. **Keep PRs focused**: Small, reviewable changes
# 3. **Respond to reviews**: Address feedback promptly
# 4. **Use Issues**: Track bugs and feature requests
# 5. **Document in README**: Help others understand your project

# %% [markdown]
# ## Part 2b: GitLab Collaboration
# 
# GitLab is another popular platform for Git repository hosting and collaboration.
# While similar to GitHub, GitLab has some unique features and terminology.
# 
# ### GitLab vs GitHub: Key Differences
# 
# - **Merge Requests** (GitLab) vs **Pull Requests** (GitHub)
# - GitLab can be self-hosted or used on GitLab.com
# - Integrated CI/CD pipelines built into GitLab
# - Different interface and feature set
# 
# ### Forking in GitLab
# 
# Forking in GitLab works similarly to GitHub:
# 
# 1. **Navigate** to the project you want to fork
# 2. **Click "Fork"** in the upper-right corner
# 3. **Choose namespace**: Select where to create your fork (personal namespace or group)
# 4. **Configure fork options**:
#    - Edit project name and slug (URL)
#    - Choose which branches to include (all branches or only default)
#    - Set visibility level (public, internal, or private)
# 5. **Create fork**: GitLab creates your personal copy
# 
# #### Keeping Your Fork Updated
# 
# ```bash
# # Add the upstream repository
# git remote add upstream https://gitlab.com/original-owner/project.git
# 
# # View your remotes
# git remote -v
# # origin    https://gitlab.com/your-username/project.git (fetch)
# # origin    https://gitlab.com/your-username/project.git (push)
# # upstream  https://gitlab.com/original-owner/project.git (fetch)
# # upstream  https://gitlab.com/original-owner/project.git (push)
# 
# # Fetch changes from upstream
# git fetch upstream
# 
# # Merge upstream changes into your main branch
# git checkout main
# git merge upstream/main
# 
# # Push updates to your fork
# git push origin main
# ```
# 
# GitLab also provides a UI button to update your fork directly from the web interface.

# %% [markdown]
# ### Merge Requests in GitLab
# 
# Merge Requests (MRs) are GitLab's equivalent to GitHub's Pull Requests.
# 
# #### Creating a Merge Request
# 
# ```bash
# # Create a new branch in your fork
# git checkout -b feature-improvement
# 
# # Make your changes
# # ... edit files ...
# 
# # Commit and push to your fork
# git add .
# git commit -m "Add feature improvement"
# git push origin feature-improvement
# ```
# 
# Then on GitLab:
# 
# 1. **Navigate** to your fork on GitLab
# 2. **Click "Create merge request"** (appears after pushing a branch)
# 3. **Configure the merge request**:
#    - Choose source branch (your feature branch)
#    - Choose target branch (usually `main` in upstream)
#    - Select target project (upstream repository)
# 4. **Write description**: Explain your changes
#    - Use merge request templates if available
#    - Reference related issues with `#issue-number`
#    - Use closing patterns like `Closes #123` to auto-close issues
# 5. **Assign reviewers and assignees**
# 6. **Create merge request**
# 
# #### Merge Request Features
# 
# GitLab Merge Requests include:
# 
# - **Inline code reviews**: Comment on specific lines
# - **Threaded discussions**: Track conversations
# - **Approval rules**: Require approvals before merging (Premium/Ultimate)
# - **CI/CD pipelines**: Automatic testing
# - **Auto-merge**: Merge automatically when conditions are met
# - **Draft status**: Mark MRs as work-in-progress
# 
# #### Working with Remotes in GitLab
# 
# ```bash
# # Clone your fork
# git clone https://gitlab.com/your-username/project.git
# cd project
# 
# # Add upstream remote
# git remote add upstream https://gitlab.com/original-owner/project.git
# 
# # Create a feature branch
# git checkout -b fix-bug
# 
# # Make changes and commit
# # ... edit files ...
# git add .
# git commit -m "Fix critical bug"
# 
# # Before pushing, sync with upstream
# git fetch upstream
# git rebase upstream/main
# 
# # Push to your fork
# git push origin fix-bug
# 
# # Create merge request on GitLab
# ```

# %% [markdown]
# ### GitLab Best Practices
# 
# 1. **Use descriptive MR titles**: Summarize the change clearly
# 2. **Link to issues**: Connect MRs to related issues for context
# 3. **Keep MRs focused**: One feature or fix per merge request
# 4. **Use draft MRs**: Mark work-in-progress with "Draft:" prefix
# 5. **Respond to feedback**: Address reviewer comments promptly
# 6. **Use CI/CD**: Ensure pipelines pass before merging
# 7. **Squash commits**: Keep history clean (when appropriate)
# 8. **Update documentation**: Include docs in your changes

# %% [markdown]
# ### Comparison: GitHub vs GitLab Workflows
# 
# | Feature | GitHub | GitLab |
# |---------|--------|--------|
# | Contribution model | Pull Request | Merge Request |
# | Fork update | Manual or sync fork button | Manual or update fork button |
# | Review process | Code review, comments | Code review, threaded discussions |
# | CI/CD | GitHub Actions | GitLab CI/CD (built-in) |
# | Project hosting | GitHub.com only | GitLab.com or self-hosted |
# | Issue tracking | GitHub Issues | GitLab Issues |
# | Draft/WIP | Draft Pull Request | Draft Merge Request |
# 
# Both platforms support similar workflows - the choice often depends on:
# - Your organization's preference
# - Self-hosting requirements
# - Specific features needed
# - Existing infrastructure

# %% [markdown]
# ## Part 3: Introduction to Python
# 
# Python is a versatile, beginner-friendly programming language widely used in research.
# 
# ### Why Python for Research?
# 
# - **Easy to learn**: Clear, readable syntax
# - **Powerful libraries**: NumPy, pandas, matplotlib, scikit-learn
# - **Interactive**: Jupyter notebooks for exploration
# - **Community**: Large, helpful community
# - **Cross-platform**: Works on Windows, macOS, Linux

# %% [markdown]
# ### Python Basics: Variables and Data Types
# 
# Variables store data. Python is dynamically typed - you don't declare types.

# %%
# Basic data types
project_name = "RNA Analysis"  # String
sample_count = 42              # Integer
temperature = 37.5             # Float
is_complete = True             # Boolean
nothing = None                 # None type

print(f"Project: {project_name}")
print(f"Samples: {sample_count}")
print(f"Temperature: {temperature}°C")
print(f"Complete: {is_complete}")
print(f"Placeholder: {nothing}")

# %%
# Type checking
print(f"Type of project_name: {type(project_name)}")
print(f"Type of sample_count: {type(sample_count)}")
print(f"Type of temperature: {type(temperature)}")
print(f"Type of is_complete: {type(is_complete)}")

# %% [markdown]
# ### Working with Strings

# %%
# String operations
sequence = "ATCGATCG"
print(f"Sequence: {sequence}")
print(f"Length: {len(sequence)}")
print(f"First base: {sequence[0]}")
print(f"Last base: {sequence[-1]}")
print(f"First three: {sequence[0:3]}")
print(f"Reversed: {sequence[::-1]}")

# String methods
print(f"Lowercase: {sequence.lower()}")
print(f"Count of A: {sequence.count('A')}")
print(f"Replace A with N: {sequence.replace('A', 'N')}")

# %% [markdown]
# ### Lists: Ordered Collections
# 
# Lists store multiple values in order. They are mutable (can be changed).

# %%
# Creating and using lists
measurements = [23.5, 24.1, 23.8, 24.3, 23.9]
print(f"Measurements: {measurements}")
print(f"First measurement: {measurements[0]}")
print(f"Last measurement: {measurements[-1]}")
print(f"Number of measurements: {len(measurements)}")

# Modifying lists
measurements.append(24.0)
print(f"After appending: {measurements}")

measurements[0] = 23.6
print(f"After modification: {measurements}")

# %%
# List operations
genes = ['BRCA1', 'TP53', 'EGFR']
print(f"Genes: {genes}")

# Adding elements
genes.append('MYC')
genes.insert(1, 'KRAS')
print(f"After adding: {genes}")

# Removing elements
genes.remove('TP53')
print(f"After removing TP53: {genes}")

last_gene = genes.pop()
print(f"Popped: {last_gene}, Remaining: {genes}")

# %%
# List slicing
data = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(f"Original: {data}")
print(f"First three: {data[0:3]}")
print(f"Middle elements: {data[3:7]}")
print(f"Every other element: {data[::2]}")
print(f"Reversed: {data[::-1]}")

# %% [markdown]
# ### Dictionaries: Key-Value Pairs
# 
# Dictionaries store data as key-value pairs. Keys must be unique.

# %%
# Creating dictionaries
experiment = {
    'name': 'Temperature Study',
    'duration_days': 30,
    'sample_size': 150,
    'temperature': 25.0,
    'completed': True
}

print("Experiment details:")
for key, value in experiment.items():
    print(f"  {key}: {value}")

# %%
# Accessing dictionary values
print(f"\nExperiment name: {experiment['name']}")
print(f"Duration: {experiment['duration_days']} days")

# Adding new keys
experiment['location'] = 'Lab A'
experiment['researcher'] = 'Dr. Smith'

# Modifying values
experiment['completed'] = False

print(f"\nUpdated experiment: {experiment}")

# %%
# Dictionary methods
print(f"Keys: {list(experiment.keys())}")
print(f"Values: {list(experiment.values())}")

# Safe access with get()
funding = experiment.get('funding', 'Not specified')
print(f"Funding: {funding}")

# Check if key exists
if 'location' in experiment:
    print(f"Location found: {experiment['location']}")

# %% [markdown]
# ### Control Flow: Making Decisions
# 
# Control structures let programs make decisions and repeat actions.

# %%
# If statements
temperature = 26.5
threshold = 25.0

if temperature > threshold:
    print(f"{temperature}°C is above threshold")
elif temperature < threshold:
    print(f"{temperature}°C is below threshold")
else:
    print(f"{temperature}°C equals threshold")

# %%
# Combining conditions
temp = 24.5
humidity = 65

if temp >= 20 and temp <= 30:
    print("Temperature in optimal range")
    
if humidity < 70 or temp < 22:
    print("At least one parameter is outside ideal range")

# %% [markdown]
# ### Loops: Repeating Actions
# 
# #### For Loops
# 
# Iterate over sequences (lists, strings, ranges).

# %%
# For loop with list
samples = ['S1', 'S2', 'S3', 'S4']

print("Processing samples:")
for sample in samples:
    print(f"  Analyzing {sample}")

# %%
# For loop with range
print("\nCounting:")
for i in range(5):
    print(f"  Count: {i}")

print("\nCounting from 10 to 15:")
for i in range(10, 16):
    print(f"  Count: {i}")

# %%
# Enumerate for index and value
data_files = ['exp1.csv', 'exp2.csv', 'exp3.csv']

for index, filename in enumerate(data_files):
    print(f"File {index + 1}: {filename}")

# %% [markdown]
# #### While Loops
# 
# Repeat while a condition is true.

# %%
# While loop example
count = 0
total = 0
measurements = [23.5, 24.1, 23.8, 24.3, 23.9]

while count < len(measurements):
    total += measurements[count]
    count += 1

average = total / len(measurements)
print(f"Average of {len(measurements)} measurements: {average:.2f}")

# %% [markdown]
# ### Basic Functions
# 
# Functions organize code into reusable blocks.

# %%
def greet(name):
    """Greet a person by name."""
    return f"Hello, {name}!"

# Call the function
message = greet("Researcher")
print(message)

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

# Test the function
data = [10.2, 10.5, 10.3, 10.4, 10.6]
mean = calculate_mean(data)
print(f"Mean: {mean:.2f}")

# %%
def analyze_sequence(sequence):
    """
    Analyze a DNA sequence.
    
    Parameters
    ----------
    sequence : str
        DNA sequence string
        
    Returns
    -------
    dict
        Dictionary with sequence statistics
    """
    return {
        'length': len(sequence),
        'gc_content': (sequence.count('G') + sequence.count('C')) / len(sequence) * 100,
        'a_count': sequence.count('A'),
        't_count': sequence.count('T'),
        'g_count': sequence.count('G'),
        'c_count': sequence.count('C')
    }

# Analyze a sequence
dna = "ATCGATCGTAGCTAGC"
stats = analyze_sequence(dna)
print(f"Sequence analysis for {dna}:")
for key, value in stats.items():
    if key == 'gc_content':
        print(f"  {key}: {value:.1f}%")
    else:
        print(f"  {key}: {value}")

# %% [markdown]
# ## Putting It Together: A Small Project
# 
# Let's combine Git, GitHub knowledge, and Python skills.

# %%
def process_experimental_data(data_points, threshold=25.0):
    """
    Process experimental data and filter by threshold.
    
    Parameters
    ----------
    data_points : list
        List of measurements
    threshold : float
        Minimum value to include
        
    Returns
    -------
    dict
        Processing results
    """
    # Filter data
    filtered = [x for x in data_points if x >= threshold]
    
    # Calculate statistics
    if len(filtered) > 0:
        mean = sum(filtered) / len(filtered)
        min_val = min(filtered)
        max_val = max(filtered)
    else:
        mean = min_val = max_val = 0
    
    return {
        'original_count': len(data_points),
        'filtered_count': len(filtered),
        'mean': mean,
        'min': min_val,
        'max': max_val,
        'filtered_data': filtered
    }

# Example usage
experimental_data = [23.5, 24.1, 26.8, 24.3, 27.1, 23.9, 25.5]
results = process_experimental_data(experimental_data, threshold=25.0)

print("Processing Results:")
print(f"  Original samples: {results['original_count']}")
print(f"  Samples above threshold: {results['filtered_count']}")
print(f"  Mean of filtered data: {results['mean']:.2f}")
print(f"  Range: {results['min']:.2f} - {results['max']:.2f}")

# %% [markdown]
# ## Summary
# 
# In this lecture, we covered:
# 
# ### Advanced Git
# - **Branching**: Creating isolated development environments
# - **Merging**: Combining branches and resolving conflicts
# - **.gitignore**: Managing which files Git tracks
# - **Best practices**: Workflow tips for effective version control
# 
# ### GitHub Collaboration
# - **Forking and Pull Requests**: Contributing to projects on GitHub
# - **Remote repositories**: Working with GitHub
# - **Collaboration best practices**: Effective teamwork on GitHub
# 
# ### GitLab Collaboration
# - **Forking in GitLab**: Creating personal copies of projects
# - **Merge Requests**: GitLab's contribution workflow
# - **Remote management**: Syncing with upstream repositories
# - **Platform comparison**: Understanding GitHub vs GitLab differences
# 
# ### Python Basics
# - **Variables and types**: Strings, numbers, booleans
# - **Collections**: Lists and dictionaries
# - **Control flow**: If statements and loops
# - **Functions**: Creating reusable code

# %% [markdown]
# ## Acknowledgements and References
# 
# This lecture builds upon concepts from multiple authoritative sources:
# 
# ### Primary Sources
# 
# - **Research Software Engineering with Python** by The Alan Turing Institute  
#   <https://alan-turing-institute.github.io/rse-course/html/>  
#   Git branching workflows, collaboration patterns, and Python introduction content adapted from this course.
# 
# - **Research Software Engineering with Python** by Damien Irving, Kate Hertweck, Luke Johnston, Joel Ostblom, Charlotte Wickham, and Greg Wilson (2022)  
#   <https://third-bit.com/py-rse/>  
#   Python fundamentals and best practices informed by this comprehensive textbook.
# 
# ### Platform Documentation
# 
# - **GitHub Documentation**  
#   <https://docs.github.com/>  
#   - Pull Requests: <https://docs.github.com/en/pull-requests>
#   - Forking Workflow: <https://docs.github.com/en/get-started/quickstart/fork-a-repo>
#   - Branch Protection: <https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches>
#   - GitHub Flow: <https://docs.github.com/en/get-started/quickstart/github-flow>
# 
# - **GitLab Documentation**  
#   <https://docs.gitlab.com/>  
#   - Merge Requests: <https://docs.gitlab.com/ee/user/project/merge_requests/>
#   - GitLab Flow: <https://docs.gitlab.com/ee/topics/gitlab_flow.html>
#   - Forking Workflow: <https://docs.gitlab.com/ee/user/project/repository/forking_workflow.html>
# 
# ### Additional Resources
# 
# - **Pro Git Book** by Scott Chacon and Ben Straub  
#   <https://git-scm.com/book/en/v2>  
#   Advanced Git concepts including branching, merging, and conflict resolution.
# 
# - **Software Carpentry: Version Control with Git**  
#   <https://swcarpentry.github.io/git-novice/>  
#   Collaborative Git workflows and best practices.
# 
# - **Python Documentation**  
#   <https://docs.python.org/3/>  
#   Official Python language reference for syntax and built-in types.
# 
# ### Notes
# 
# The lecture structure, examples, and exercises have been developed specifically for this course,
# drawing on best practices from the sources above. Platform-specific content (GitHub/GitLab)
# references official documentation to ensure accuracy.

# %% [markdown]
# ### Next Steps
# 
# In Lecture 3, we'll dive deeper into Python with:
# - Advanced function concepts
# - Error handling with try/except
# - File input/output
# - List comprehensions and functional programming
# 
# **Ready to continue? Move on to Lecture 3: Python Fundamentals and Advanced Concepts!**

# %%
