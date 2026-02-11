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
# <div style="background-color: #f3e5f5; border-left: 5px solid #9c27b0; padding: 15px; margin: 10px 0; border-radius: 5px;">
#     <h4 style="color: #7b1fa2; margin-top: 0;">💡 Try It Yourself</h4>
#     <p>Deepen your shell skills with these exploration activities:</p>
#     <ul>
#         <li><strong>Experiment with glob patterns:</strong> Try using wildcards like
#         <code>*.txt</code>, <code>data_*.csv</code>, or <code>**/*.py</code> to match multiple files
#         at once</li>
#         <li><strong>Chain commands together:</strong> Use <code>&&</code> to run multiple commands
#         sequentially (e.g., <code>mkdir test_dir && cd test_dir && touch file.txt</code>)</li>
#         <li><strong>Explore your system:</strong> Navigate to different directories on your computer,
#         use <code>ls -la</code> to see hidden files, and practice using tab completion to speed up
#         navigation</li>
#     </ul>
# </div>

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

# %%
# Visualize the Git workflow
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

fig, ax = plt.subplots(figsize=(12, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 5)
ax.axis('off')

# Define boxes for the three stages
boxes = [
    {'x': 0.5, 'y': 2, 'width': 2.5, 'height': 1.5, 'label': 'Working\nDirectory',
     'color': '#ffebee', 'desc': 'Edit files'},
    {'x': 3.5, 'y': 2, 'width': 2.5, 'height': 1.5, 'label': 'Staging\nArea',
     'color': '#fff3e0', 'desc': 'git add'},
    {'x': 6.5, 'y': 2, 'width': 2.5, 'height': 1.5, 'label': 'Repository\n(.git)',
     'color': '#e8f5e9', 'desc': 'git commit'}
]

# Draw boxes
for box in boxes:
    fancy_box = FancyBboxPatch(
        (box['x'], box['y']), box['width'], box['height'],
        boxstyle="round,pad=0.1", 
        edgecolor='#333', linewidth=2,
        facecolor=box['color']
    )
    ax.add_patch(fancy_box)
    
    # Add label
    ax.text(box['x'] + box['width']/2, box['y'] + box['height']/2 + 0.3,
            box['label'], ha='center', va='center',
            fontsize=12, fontweight='bold')
    
    # Add description
    ax.text(box['x'] + box['width']/2, box['y'] + box['height']/2 - 0.3,
            box['desc'], ha='center', va='center',
            fontsize=10, style='italic', color='#555')

# Draw arrows between stages
arrow1 = FancyArrowPatch((3, 2.75), (3.5, 2.75),
                         arrowstyle='->', mutation_scale=20,
                         linewidth=2, color='#1976d2')
ax.add_patch(arrow1)

arrow2 = FancyArrowPatch((6, 2.75), (6.5, 2.75),
                         arrowstyle='->', mutation_scale=20,
                         linewidth=2, color='#1976d2')
ax.add_patch(arrow2)

# Add title
ax.text(5, 4.5, 'Git Three-Stage Workflow', ha='center',
        fontsize=16, fontweight='bold')

# Add workflow steps at bottom
ax.text(5, 0.8, '1. Modify files → 2. Stage changes (git add) → 3. Commit to history (git commit)',
        ha='center', fontsize=11, color='#333',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='#f5f5f5', edgecolor='#999'))

plt.tight_layout()
plt.show()

# %% [markdown]
# The diagram above shows how Git manages your code through three distinct areas:
# 
# 1. **Working Directory**: Where you edit your files normally
# 2. **Staging Area**: Where you prepare changes before committing (lets you choose exactly what to commit)
# 3. **Repository**: Where Git permanently stores your project history
# 
# This three-stage approach gives you precise control over what goes into each commit.
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

# %%
# Visualize Git commit history as a timeline
fig, ax = plt.subplots(figsize=(12, 4))
ax.set_xlim(-0.5, 5.5)
ax.set_ylim(-1, 2)
ax.axis('off')

# Define commits
commits = [
    {'x': 0, 'hash': 'a1b2c3d', 'msg': 'Initial commit', 'file': 'README.md'},
    {'x': 1, 'hash': 'e4f5g6h', 'msg': 'Add data processing', 'file': 'process.py'},
    {'x': 2, 'hash': 'i7j8k9l', 'msg': 'Fix bug in analysis', 'file': 'analysis.py'},
    {'x': 3, 'hash': 'm0n1o2p', 'msg': 'Add visualization', 'file': 'plot.py'},
    {'x': 4, 'hash': 'q3r4s5t', 'msg': 'Update documentation', 'file': 'README.md'},
]

# Draw timeline
ax.plot([-0.3, 4.3], [0, 0], 'k-', linewidth=2, alpha=0.3)

# Draw commits
for commit in commits:
    # Commit circle
    circle = plt.Circle((commit['x'], 0), 0.15, color='#1976d2', zorder=3)
    ax.add_patch(circle)
    
    # Commit hash
    ax.text(commit['x'], -0.5, commit['hash'],
            ha='center', fontsize=9, family='monospace',
            color='#666')
    
    # Commit message
    ax.text(commit['x'], 0.6, commit['msg'],
            ha='center', fontsize=9, fontweight='bold',
            color='#333')
    
    # File changed
    ax.text(commit['x'], 1.1, f"({commit['file']})",
            ha='center', fontsize=8, style='italic',
            color='#777')

# Add arrows between commits
for i in range(len(commits) - 1):
    ax.annotate('', xy=(commits[i+1]['x'], 0), xytext=(commits[i]['x'], 0),
                arrowprops=dict(arrowstyle='->', lw=2, color='#999'))

# Add labels
ax.text(-0.3, -0.85, 'Oldest', ha='center', fontsize=10, color='#666')
ax.text(4.3, -0.85, 'Newest', ha='center', fontsize=10, color='#666')
ax.text(2, 1.7, 'Git Commit History Timeline', ha='center',
        fontsize=14, fontweight='bold')

plt.tight_layout()
plt.show()

# %% [markdown]
# The timeline above shows how Git tracks your project history through a sequence of commits.
# Each commit is like a snapshot of your project at a specific point in time. Git remembers:
# - **What changed** (the actual file modifications)
# - **When it changed** (timestamp)
# - **Who changed it** (author)
# - **Why it changed** (commit message)
# 
# With `git log`, you can view this history. With `git checkout <hash>`, you can even go back
# to any point in time to see or restore old versions!

# %% [markdown]
# <div style="background-color: #f3e5f5; border-left: 5px solid #9c27b0; padding: 15px; margin: 10px 0; border-radius: 5px;">
#     <h4 style="color: #7b1fa2; margin-top: 0;">💡 Try It Yourself</h4>
#     <p>Build your Git intuition with hands-on practice:</p>
#     <ul>
#         <li><strong>Create a practice repository:</strong> Make a new directory, run
#         <code>git init</code>, and create several files. Make 5-10 commits with descriptive
#         messages</li>
#         <li><strong>Visualize your history:</strong> Try <code>git log --graph --oneline --all</code>
#         to see your commit history as a visual graph</li>
#         <li><strong>Experiment with diffs:</strong> Modify a file, use <code>git diff</code> before
#         staging, then <code>git diff --staged</code> after adding it. Understand what each shows
#         you</li>
#     </ul>
# </div>

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

# %%
# Visualize Local vs Remote Repository workflow
fig, ax = plt.subplots(figsize=(12, 5))
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis('off')

# Local repository
local_box = FancyBboxPatch((0.5, 2), 3.5, 2.5,
                           boxstyle="round,pad=0.15",
                           edgecolor='#1976d2', linewidth=3,
                           facecolor='#e3f2fd')
ax.add_patch(local_box)
ax.text(2.25, 4, 'Your Computer', ha='center', fontsize=13, fontweight='bold')
ax.text(2.25, 3.4, 'Local Repository', ha='center', fontsize=11)
ax.text(2.25, 2.8, '(.git folder)', ha='center', fontsize=9, style='italic', color='#666')

# Remote repository (GitHub)
remote_box = FancyBboxPatch((6, 2), 3.5, 2.5,
                            boxstyle="round,pad=0.15",
                            edgecolor='#388e3c', linewidth=3,
                            facecolor='#e8f5e9')
ax.add_patch(remote_box)
ax.text(7.75, 4, 'GitHub', ha='center', fontsize=13, fontweight='bold')
ax.text(7.75, 3.4, 'Remote Repository', ha='center', fontsize=11)
ax.text(7.75, 2.8, '(Cloud backup)', ha='center', fontsize=9, style='italic', color='#666')

# Push arrow
push_arrow = FancyArrowPatch((4, 3.8), (6, 3.8),
                             arrowstyle='->', mutation_scale=25,
                             linewidth=2.5, color='#1976d2')
ax.add_patch(push_arrow)
ax.text(5, 4.2, 'git push', ha='center', fontsize=11,
        fontweight='bold', color='#1976d2')

# Pull arrow
pull_arrow = FancyArrowPatch((6, 2.7), (4, 2.7),
                             arrowstyle='->', mutation_scale=25,
                             linewidth=2.5, color='#388e3c')
ax.add_patch(pull_arrow)
ax.text(5, 2.3, 'git pull', ha='center', fontsize=11,
        fontweight='bold', color='#388e3c')

# Clone arrow
clone_arrow = FancyArrowPatch((7.75, 2), (2.25, 1.5),
                              arrowstyle='->', mutation_scale=25,
                              linewidth=2, color='#f57c00',
                              linestyle='dashed')
ax.add_patch(clone_arrow)
ax.text(5, 1, 'git clone (first time)', ha='center', fontsize=10,
        style='italic', color='#f57c00')

# Title
ax.text(5, 5.3, 'Git + GitHub Workflow', ha='center',
        fontsize=15, fontweight='bold')

plt.tight_layout()
plt.show()

# %% [markdown]
# This diagram shows the relationship between your local repository and GitHub:
# 
# - **git clone**: Copy a repository from GitHub to your computer (do this once)
# - **git push**: Send your local commits to GitHub (share your work)
# - **git pull**: Get new commits from GitHub to your computer (get others' work)
# 
# Think of GitHub as a shared backup and collaboration hub for your code!
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
# <div style="background-color: #f3e5f5; border-left: 5px solid #9c27b0; padding: 15px; margin: 10px 0; border-radius: 5px;">
#     <h4 style="color: #7b1fa2; margin-top: 0;">💡 Try It Yourself</h4>
#     <p>Experience the power of GitHub collaboration:</p>
#     <ul>
#         <li><strong>Fork and explore this course:</strong> Fork the RSE_course_JuRSE repository, clone
#         your fork locally, and browse the code structure</li>
#         <li><strong>Practice the PR workflow:</strong> Make a small change (e.g., fix a typo in a
#         README), commit it, push to your fork, and create a draft pull request (you can close it
#         without merging)</li>
#         <li><strong>Explore a real project:</strong> Find an interesting research software project on
#         GitHub, read its documentation, look at recent pull requests, and understand how the community
#         collaborates</li>
#     </ul>
# </div>

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
