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
# Welcome to the Research Software Engineering (RSE) lecture series! This introductory 
# lecture provides an overview of what RSE is, why it matters for modern research, and 
# how to get started with the tools and practices we'll cover throughout this course.
# 
# **Duration**: ~90 minutes
# 
# ## Learning Objectives
# - Understand what Research Software Engineering is and why it matters
# - Learn about the structure and content of this course
# - Get familiar with accessing and using the course materials
# - Gain a basic introduction to essential development tools:
#   - Shell/command line
#   - Git version control
#   - GitHub collaboration

# %% [markdown]
# ## Part 1: What is Research Software Engineering?
# 
# ### The Role of Software in Research
# 
# Modern research increasingly relies on software:
# - **Data Analysis**: Processing and analyzing experimental or observational data
# - **Simulations**: Modeling complex systems (climate, molecular dynamics, economics)
# - **Automation**: Automating repetitive tasks and workflows
# - **Reproducibility**: Ensuring research results can be verified and replicated
# 
# ### What is a Research Software Engineer?
# 
# A Research Software Engineer (RSE) combines:
# - **Domain Knowledge**: Understanding of the research field
# - **Software Development Skills**: Professional programming practices
# - **Collaborative Mindset**: Working with researchers to build better tools
# 
# ### Why RSE Matters
# 
# Research software engineering is important because:
# 
# 1. **Quality**: Well-engineered software produces more reliable results
# 2. **Efficiency**: Good practices save time in the long run
# 3. **Reproducibility**: Proper version control and documentation enable others to verify your work
# 4. **Impact**: Reusable, well-documented software increases research impact
# 5. **Career**: RSE skills are valuable in both academia and industry
# 
# ### The Research Software Engineering Community
# 
# - [Society of Research Software Engineering](https://society-rse.org/)
# - RSE conferences and meetups worldwide
# - Growing recognition of RSE as a career path
# - Best practices developed by and for researchers

# %% [markdown]
# ## Part 2: Course Structure and Content
# 
# ### Course Overview
# 
# This course covers essential Research Software Engineering practices through hands-on lectures:
# 
# - **Lecture 1** (90 mins): Introduction to RSE, Shell Basics, and Git Fundamentals
# - **Lecture 2** (90 mins): Advanced Git, GitHub Collaboration, and Python Basics
# - **Lecture 3** (90 mins): Python Fundamentals and Advanced Concepts (including Error Handling)
# - **Lecture 4** (90 mins): Python Project Structure and Working with Libraries (NumPy, Matplotlib)
# 
# Each lecture is designed to be hands-on and practical, building on concepts from previous sessions
# 
# ### Learning Approach
# 
# Each lecture includes:
# - Conceptual explanations
# - Practical examples
# - Hands-on exercises
# - Best practices specific to research software
# 
# ### Prerequisites
# 
# - Basic computer literacy
# - Willingness to learn programming
# - No prior programming experience required for this course

# %% [markdown]
# ## Part 3: Accessing and Installing Course Materials
# 
# ### How to Access This Course
# 
# The course materials are available on GitHub:
# - **Repository**: https://github.com/pancetta/RSE_lecture
# - **Website**: Rendered as an interactive website using Jupyter Book
# - **Format**: Python files (using Jupytext) that convert to Jupyter notebooks
# 
# ### Installation Steps
# 
# #### 1. Clone the Repository
# 
# First, you need Git installed on your system. Then:
# 
# ```bash
# git clone https://github.com/pancetta/RSE_lecture.git
# cd RSE_lecture
# ```
# 
# #### 2. Install Micromamba (or Conda/Mamba)
# 
# We use micromamba for managing Python environments:
# - **Linux/macOS**: Follow instructions at https://mamba.readthedocs.io/en/latest/installation/micromamba-installation.html
# - **Windows**: Use Git Bash or WSL (Windows Subsystem for Linux)
# 
# #### 3. Create the Environment
# 
# ```bash
# micromamba env create -f environment.yml
# micromamba activate rse_lecture
# ```
# 
# Or using the Makefile:
# 
# ```bash
# make install
# micromamba activate rse_lecture
# ```
# 
# #### 4. View the Course Website
# 
# Build and serve the website locally:
# 
# ```bash
# make serve-website
# ```
# 
# Then open your browser to http://localhost:8000
# 
# ### Working with Jupyter Notebooks
# 
# Convert Python lecture files to notebooks:
# 
# ```bash
# python convert_to_notebooks.py
# ```
# 
# Then start Jupyter:
# 
# ```bash
# jupyter notebook
# ```

# %% [markdown]
# ## Part 4: Introduction to Essential Tools
# 
# ### The Command Line / Shell
# 
# The command line (also called terminal, shell, or console) is essential for:
# - Running research software
# - Automating tasks
# - Working on remote servers
# - Version control with Git
# 
# #### Basic Shell Commands
# 
# Here are the most important commands you'll use:
# 
# ```bash
# # Navigation
# pwd              # Print working directory - shows where you are
# ls               # List files and directories
# ls -la           # List with details (size, permissions, hidden files)
# cd directory     # Change directory
# cd ..            # Go up one directory
# cd ~             # Go to home directory
# 
# # File operations
# cat file.txt     # Display file contents
# less file.txt    # View file with scrolling (press 'q' to quit)
# head file.txt    # Show first 10 lines
# tail file.txt    # Show last 10 lines
# 
# # Creating and modifying
# mkdir dirname    # Create a directory
# touch file.txt   # Create an empty file
# cp src dest      # Copy file
# mv src dest      # Move/rename file
# rm file.txt      # Remove file (careful!)
# rm -r directory  # Remove directory and contents (very careful!)
# 
# # Getting help
# man command      # Show manual for a command
# command --help   # Show help for a command
# ```
# 
# #### Shell Tips
# 
# - **Tab completion**: Press Tab to auto-complete file and directory names
# - **Command history**: Use Up/Down arrow keys to recall previous commands
# - **Copy/Paste**: Ctrl+Shift+C / Ctrl+Shift+V in most terminals
# - **Clear screen**: Type `clear` or press Ctrl+L

# %% [markdown]
# ### Introduction to Git
# 
# Git is a version control system that tracks changes to your code:
# 
# #### Why Use Git?
# 
# - **History**: Track every change you make
# - **Safety**: Easy to revert mistakes
# - **Collaboration**: Work with others without conflicts
# - **Backup**: Your code is safely stored
# 
# #### Basic Git Workflow
# 
# ```bash
# # Configure Git (first time only)
# git config --global user.name "Your Name"
# git config --global user.email "your.email@example.com"
# 
# # Create a new repository
# git init
# 
# # Check status of your repository
# git status
# 
# # Add files to staging area
# git add filename.py      # Add specific file
# git add .                # Add all changed files
# 
# # Commit changes with a message
# git commit -m "Description of what you changed"
# 
# # View commit history
# git log
# git log --oneline        # Compact view
# 
# # See what changed
# git diff                 # Changes not yet staged
# git diff --staged        # Changes staged for commit
# ```
# 
# #### Git Best Practices
# 
# - Make small, focused commits
# - Write clear commit messages
# - Commit often
# - Don't commit sensitive data (passwords, API keys)

# %% [markdown]
# ### Introduction to GitHub
# 
# GitHub is a platform for hosting Git repositories and collaborating with others:
# 
# #### Why Use GitHub?
# 
# - **Remote backup**: Your code is stored in the cloud
# - **Collaboration**: Share code with colleagues
# - **Open source**: Share your research software with the world
# - **Discovery**: Find and use software from other researchers
# - **Documentation**: README, wiki, and GitHub Pages
# 
# #### Basic GitHub Workflow
# 
# ```bash
# # Clone an existing repository
# git clone https://github.com/username/repository.git
# cd repository
# 
# # After making changes and committing locally:
# 
# # Push your changes to GitHub
# git push
# 
# # Get latest changes from GitHub
# git pull
# 
# # Create a new branch for a feature
# git checkout -b feature-name
# 
# # Switch back to main branch
# git checkout main
# ```
# 
# #### GitHub Features
# 
# - **Issues**: Track bugs and feature requests
# - **Pull Requests**: Propose and review changes
# - **Actions**: Automate testing and deployment
# - **Pages**: Host documentation websites
# - **Releases**: Package and distribute your software
# 
# #### Forking and Contributing
# 
# To contribute to someone else's project:
# 
# 1. Fork the repository on GitHub
# 2. Clone your fork locally
# 3. Create a new branch for your changes
# 4. Make changes and commit
# 5. Push to your fork
# 6. Create a Pull Request

# %% [markdown]
# ## Part 5: Getting Started with This Course
# 
# ### Your First Steps
# 
# Now that you have an overview, here's what to do next:
# 
# 1. **Install the course environment** (if you haven't already)
# 2. **Explore the repository structure**
# 3. **Try converting a lecture to a notebook**
# 4. **Practice basic shell commands**
# 5. **Make a test commit to a practice repository**
# 
# ### Tips for Success
# 
# - **Practice regularly**: Programming is a skill that improves with practice
# - **Don't be afraid to make mistakes**: Version control makes it easy to undo
# - **Ask questions**: Use GitHub Issues or discussions
# - **Start small**: Begin with simple scripts and gradually build complexity
# - **Read other people's code**: Learn from well-written research software
# 
# ### Resources
# 
# - [Software Carpentry](https://software-carpentry.org/): Free workshops on scientific computing
# - [The Turing Way](https://the-turing-way.netlify.app/): Handbook for reproducible research
# - [Git Book](https://git-scm.com/book/en/v2): Comprehensive Git documentation
# - [GitHub Skills](https://skills.github.com/): Interactive GitHub tutorials

# %% [markdown]
# ## Summary
# 
# In this introductory lecture, we covered:
# 
# - **What RSE is**: Combining research domain knowledge with software engineering practices
# - **Why it matters**: Quality, efficiency, reproducibility, impact, and career development
# - **Course structure**: Hands-on lectures covering essential RSE skills
# - **Getting started**: How to access, install, and use the course materials
# - **Essential tools**:
#   - Shell/command line for running software and automation
#   - Git for version control and tracking changes
#   - GitHub for collaboration and sharing code
# 
# ### Next Steps
# 
# In the next lecture, we'll explore advanced Git topics like branching and merging,
# learn about GitHub collaboration, and begin our journey into Python programming
# with fundamental concepts and syntax.
# 
# **Ready to continue? Move on to Lecture 2: Advanced Git, GitHub, and Python Basics!**

# %%
