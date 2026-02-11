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
# 
# ## Quick Access
# 
# Scan the QR codes below for quick access to course materials:
# 
# <div style="display: flex; gap: 20px; align-items: flex-start;">
#   <div style="text-align: center;">
#     <img src="../course_qr_code.png" alt="Course Website QR Code" width="150"/>
#     <p><strong>Course Website</strong></p>
#   </div>
#   <div style="text-align: center;">
#     <img src="lecture_01_qr_code.png" alt="This Lecture QR Code" width="150"/>
#     <p><strong>This Lecture</strong></p>
#   </div>
# </div>
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
# This course covers essential Research Software Engineering practices through hands-on lectures. 
# Each lecture builds on the previous one, introducing new concepts while reinforcing earlier 
# material. The course is designed to take you from basic command-line skills to writing well-
# tested, professional-quality research software.
# 
# - **Lecture 1** (90 mins): Introduction to RSE, Shell Basics, and Git Fundamentals
# - **Lecture 2** (90 mins): Advanced Git, GitHub Collaboration, and Python Basics
# - **Lecture 3** (90 mins): Python Fundamentals and Advanced Concepts (including Error Handling)
# - **Lecture 4** (90 mins): Python Project Structure and Working with Libraries (NumPy, Matplotlib)
# - **Lecture 5** (90 mins): Testing Research Software
# - **Lecture 6** (90 mins): Automation and Continuous Integration
# 
# Each lecture is designed to be hands-on and practical, building on concepts from previous sessions.
# You'll learn by doing, with plenty of examples drawn from real research scenarios.
# 
# ### Learning Approach
# 
# Each lecture includes:
# - **Conceptual explanations**: Understanding the "why" before the "how"
# - **Practical examples**: Real code that you can run and modify
# - **Hands-on exercises**: Practice what you've learned immediately
# - **Best practices specific to research software**: Not just programming, but research-focused coding
# 
# **How to get the most from these lectures**: Don't just read the code—type it out yourself, run it, 
# modify it, and see what happens. Making mistakes is part of learning. The lectures provide examples, 
# but you'll learn much more by experimenting and occasionally breaking things (that's what version 
# control is for!).
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
# - **Repository**: https://github.com/pancetta/RSE_course_JuRSE
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
# git clone https://github.com/pancetta/RSE_course_JuRSE.git
# cd RSE_course_JuRSE
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
# **Why learn the command line?** While graphical interfaces are user-friendly, the command line 
# gives you precise control and allows you to automate repetitive tasks. Many research computing 
# environments (like high-performance computing clusters) only provide command-line access. 
# Additionally, most research software tools are designed to be run from the command line, making 
# it an essential skill for any research software engineer.
# 
# #### Basic Shell Commands
# 
# Here are the most important commands you'll use. Don't try to memorize all of these at once—
# you'll naturally remember the ones you use frequently. Keep this as a reference guide and 
# focus on practicing the navigation and file operation commands first.
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
# 
# **Common Pitfall**: Be very careful with `rm` commands, especially `rm -r`. There is no "undo" 
# or trash bin—deleted files are gone permanently. Always double-check the file or directory name 
# before pressing Enter. A good practice is to use `ls` first to verify you're targeting the right 
# files.

# %% [markdown]
# ### Introduction to Git
# 
# Git is a version control system that tracks changes to your code. Think of Git as a sophisticated 
# "save game" system for your code—it records not just the current state, but every change you've 
# made along the way, who made it, and why. This makes it incredibly powerful for both individual 
# work and collaboration.
# 
# #### Why Use Git?
# 
# - **History**: Track every change you make - see exactly what changed, when, and why
# - **Safety**: Easy to revert mistakes - go back to any previous version of your code
# - **Collaboration**: Work with others without conflicts - multiple people can edit simultaneously
# - **Backup**: Your code is safely stored - combined with GitHub, you have cloud backup
# - **Experimentation**: Try new ideas without fear - create branches to experiment safely
# 
# **Real-world scenario**: Imagine you're analyzing research data and make changes to your analysis 
# script that produce unexpected results. With Git, you can easily compare your current code with 
# yesterday's version to see exactly what changed. Or if you accidentally delete an important 
# function, you can retrieve it from your Git history instead of having to rewrite it from scratch.
# 
# #### Basic Git Workflow
# 
# The basic Git workflow has three main stages: (1) modify files in your working directory, 
# (2) stage the changes you want to commit, and (3) commit those changes to your repository 
# with a descriptive message. This might seem like extra steps at first, but the staging area 
# gives you fine control over what goes into each commit, allowing you to create logical, 
# focused commits even if you've changed multiple files.
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
# - **Make small, focused commits**: Each commit should represent one logical change. This makes 
#   it easier to understand your history and revert specific changes if needed.
# - **Write clear commit messages**: Use the format "Add feature" or "Fix bug" rather than "Changed 
#   stuff". Future you (and your collaborators) will thank you.
# - **Commit often**: Commit whenever you complete a small piece of work. It's better to have many 
#   small commits than one giant commit with 500 lines changed.
# - **Don't commit sensitive data**: Never commit passwords, API keys, or private data. Once in Git 
#   history, they're very difficult to remove completely.
# 
# **When to commit?** A good rule of thumb: commit whenever you've made a change that you might 
# want to return to later. This could be after fixing a bug, adding a new function, or refactoring 
# code to be cleaner. If you're about to try something experimental, commit first—then you can 
# always go back if the experiment doesn't work out.

# %% [markdown]
# ### Introduction to GitHub
# 
# GitHub is a platform for hosting Git repositories and collaborating with others. While Git 
# manages version control on your local computer, GitHub provides a central location where you 
# and your collaborators can share code, discuss changes, track issues, and automate workflows. 
# Think of Git as the tool and GitHub as the social network built around it.
# 
# #### Why Use GitHub?
# 
# - **Remote backup**: Your code is stored in the cloud—even if your laptop fails, your work is safe
# - **Collaboration**: Share code with colleagues and work together seamlessly
# - **Open source**: Share your research software with the world and get citations
# - **Discovery**: Find and use software from other researchers—don't reinvent the wheel
# - **Documentation**: README files, wikis, and GitHub Pages for beautiful project websites
# - **Professional portfolio**: Showcase your coding skills to potential employers or collaborators
# 
# **For researchers specifically**: GitHub has become the standard platform for sharing research 
# code. Many journals now require code to be published alongside papers, and GitHub provides a 
# citable DOI (Digital Object Identifier) through integration with Zenodo. This means your code 
# can be cited just like a paper, increasing your research impact.
# 
# #### Basic GitHub Workflow
# 
# The basic GitHub workflow connects your local Git repository with a remote repository on GitHub. 
# After making changes locally and committing them, you "push" those commits to GitHub. When your 
# collaborators make changes, you "pull" their commits to your local repository. This push-pull 
# cycle keeps everyone synchronized.
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
# **Typical workflow**: Before starting work each day, run `git pull` to get the latest changes 
# from your collaborators. Make your changes, commit them locally with `git commit`, then share 
# them with `git push`. Always pull before pushing to avoid conflicts.
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
# 1. **Fork** the repository on GitHub (creates your own copy)
# 2. **Clone** your fork locally to your computer
# 3. **Create a new branch** for your changes (keeps your work organized)
# 4. **Make changes and commit** (implement your feature or fix)
# 5. **Push to your fork** on GitHub
# 6. **Create a Pull Request** (ask the original project to include your changes)
# 
# **Why this workflow?** You don't have direct write access to other people's repositories (for 
# security reasons). Forking creates your own copy where you have full control. The pull request 
# system lets the original authors review your changes before accepting them, ensuring code quality 
# and preventing malicious changes. This same workflow is used by major open-source projects with 
# thousands of contributors.

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

# %% [markdown]
# ## Acknowledgements and References
# 
# This lecture draws inspiration and content from several excellent resources:
# 
# ### Primary Sources
# 
# - **Research Software Engineering with Python** by The Alan Turing Institute  
#   <https://alan-turing-institute.github.io/rse-course/html/>  
#   The structure and pedagogical approach of this course is heavily influenced by this comprehensive RSE course.
# 
# - **Research Software Engineering with Python** by Damien Irving, Kate Hertweck,
#   Luke Johnston, Joel Ostblom, Charlotte Wickham, and Greg Wilson (2022)
#   <https://third-bit.com/py-rse/>
#   An excellent book that informed our approach to teaching research software
#   engineering principles.
# 
# ### Documentation and Learning Resources
# 
# - **Git Documentation and Pro Git Book** by Scott Chacon and Ben Straub  
#   <https://git-scm.com/book/en/v2>  
#   For Git fundamentals and version control concepts.
# 
# - **GitHub Documentation**  
#   <https://docs.github.com/>  
#   For GitHub-specific features and collaboration workflows.
# 
# - **Software Carpentry: The Unix Shell**  
#   <https://swcarpentry.github.io/shell-novice/>  
#   For shell/command line basics and best practices.
# 
# - **Software Carpentry: Version Control with Git**  
#   <https://swcarpentry.github.io/git-novice/>  
#   For introductory Git concepts and exercises.
# 
# - **Society of Research Software Engineering**  
#   <https://society-rse.org/>  
#   For information about the RSE community and career paths.
# 
# ### Notes
# 
# While this lecture incorporates ideas and approaches from these sources, all content has been 
# adapted and restructured for this specific course context. Examples and exercises have been 
# developed independently for educational purposes.

# %% [markdown]
# ### Next Steps
# 
# In the next lecture, we'll explore advanced Git topics like branching and merging,
# learn about GitHub collaboration, and begin our journey into Python programming
# with fundamental concepts and syntax.
# 
# **Ready to continue? Move on to Lecture 2: Advanced Git, GitHub, and Python Basics!**

# %%
