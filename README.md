# Research Software Engineering Lectures

[![CI - Lecture Scripts](https://github.com/pancetta/RSE_lecture/workflows/CI%20-%20Lecture%20Scripts/badge.svg)](https://github.com/pancetta/RSE_lecture/actions)

Welcome to the Research Software Engineering (RSE) lecture series! This repository contains materials for learning best practices in developing high-quality research software.

## Overview

This lecture series covers fundamental concepts and practices in Research Software Engineering, including:

- **Lecture 1**: Introduction to RSE, Shell Basics, and Git Fundamentals (~90 minutes)
- **Lecture 2**: Advanced Git, GitHub Collaboration, and Python Basics (~90 minutes)
- **Lecture 3**: Python Fundamentals and Advanced Concepts (including Error Handling) (~90 minutes)
- **Lecture 4**: Python Project Structure and Working with Libraries (NumPy, Matplotlib) (~90 minutes)

## Structure

Each lecture is organized in its own directory and consists of:
- A Python file (`.py`) that contains the lecture content in Jupytext format
- The file can be converted to a Jupyter notebook (`.ipynb`) using Jupytext

## Getting Started

### Prerequisites

- Python 3.7 or higher
- micromamba or conda/mamba

**Platform Support:**
- ✅ Linux (Ubuntu and other distributions)
- ✅ macOS 15 (Sequoia) and later
- ✅ macOS 26 (Tahoe)
- ✅ Windows 10/11 (with Git Bash)
- Note: All installation commands and scripts are compatible with Linux, macOS, and Windows

### Installation

1. Clone this repository:
```bash
git clone https://github.com/pancetta/RSE_lecture.git
cd RSE_lecture
```

2. Install [micromamba](https://mamba.readthedocs.io/en/latest/installation/micromamba-installation.html) if you haven't already.

3. Create and activate the environment:

**For all lectures (unified approach):**

Each lecture has its own environment file in its directory. To install for a specific lecture:

```bash
# Lecture 1
make install-lecture1

# Lecture 2
make install-lecture2

# Lecture 3
make install-lecture3

# Lecture 4 (adds matplotlib)
make install-lecture4
```

Then activate:
```bash
micromamba activate rse_lecture
```

**Manual installation (if not using Make):**
```bash
# Create base environment
micromamba env create -f environment.yml
# Add lecture-specific dependencies (example for lecture 4)
micromamba env update -f lecture_04/environment.yml
micromamba activate rse_lecture
```

**For development (includes all dependencies plus dev tools):**
```bash
micromamba env create -f environment-dev.yml
micromamba activate rse_lecture
```

Or using the Makefile:
```bash
make install-dev
micromamba activate rse_lecture
```

**Note:** 
- The base `environment.yml` contains common dependencies (Python, Jupyter, NumPy, Jupyter Book).
- Each lecture has an `environment.yml` file in its directory containing **only additional dependencies**.
- Lectures 1-3 have empty dependency lists (use base only); Lecture 4 adds matplotlib.
- The `environment-dev.yml` includes all dependencies plus development tools (flake8, nbconvert).
- Installation pattern is **harmonized**: all lectures follow the same two-step process (base + additions).
- Lecture 1 introduces the course and essential tools (shell, git, GitHub).
- Lecture 2 introduces Python basics (uses standard library only).
- Lecture 3 focuses on advanced Python using the standard library.
- Lecture 4 covers NumPy, matplotlib, and project structure (adds matplotlib to base environment).

## Usage

### Building and Serving the Website

This repository uses [Jupyter Book v2](https://jupyterbook.org/) (powered by MyST) to generate an interactive website from the lectures.

**Note:** Jupyter Book v2 creates a dynamic web application rather than static HTML. For local development, use the built-in server:

#### Serve the website locally (recommended):
```bash
make serve-website
```

This will:
1. Convert all Python lecture files to Jupyter notebooks
2. Build the MyST website
3. Start a local development server at `http://localhost:8000`

The website features:
- **Interactive navigation** with sidebar and search
- **Formatted code cells** with syntax highlighting  
- **Live content updates** during development
- **Modern MyST theme** with responsive design
- **Document outline** for easy navigation
- **GitHub integration** with edit and download buttons

#### Build the website:
```bash
make build-website
```

This builds the site content in the `_build/site/` directory.

### Deployment

**GitHub Pages Deployment:** Jupyter Book v2 is designed primarily as a dynamic web application. For GitHub Pages deployment (static HTML), the GitHub Actions workflow includes a conversion step. For production deployments, consider using:
- [Curvenote](https://curvenote.com) for MyST-native hosting
- [Vercel](https://vercel.com) or [Netlify](https://netlify.com) for static exports
- The built-in `jupyter-book start` server for self-hosted solutions

The repository includes a GitHub Actions workflow configured for GitHub Pages deployment.

### Converting Python Files to Jupyter Notebooks

This repository uses [Jupytext](https://jupytext.readthedocs.io/) to maintain lectures as Python files that can be easily version-controlled and converted to Jupyter notebooks.

#### Convert a single lecture:
```bash
jupytext --to notebook lecture_01/lecture_01.py
```

#### Convert all lectures at once:
```bash
python convert_to_notebooks.py
```

#### Open as notebook directly:
You can also pair the Python file with a notebook and keep them synchronized:
```bash
jupytext --set-formats py:percent,ipynb lecture_01/lecture_01.py
```

### Running the Lectures

After converting to notebooks, you can open them with Jupyter:
```bash
jupyter notebook
```

Navigate to the lecture directory and open the `.ipynb` file.

## Why Jupytext?

Jupytext allows us to:
- **Version control**: Python files are easier to track in Git than notebooks
- **Code review**: Easier to review changes in pull requests
- **Collaboration**: Multiple people can work on lectures without merge conflicts
- **Flexibility**: Edit lectures in your favorite Python IDE or as notebooks

## Dependency Management

This repository uses a multi-environment approach for clean dependency separation with automated dependency tracking.

**📖 For detailed dependency management instructions, see [DEPENDENCY_MANAGEMENT.md](DEPENDENCY_MANAGEMENT.md)**

### Environment Files

- **`environment.yml`**: Base environment with core dependencies (Python, Jupyter, NumPy, Jupyter Book)
  - Foundation for all lectures
  
- **`lecture_XX/environment.yml`**: Lecture-specific additional dependencies
  - **Harmonized structure**: Every lecture has this file
  - Contains **only additional dependencies** beyond the base
  - Lectures 1-3: Empty dependencies list (base is sufficient)
  - Lecture 4: Adds matplotlib for visualization
  - Installed via `micromamba env update` to add to existing base environment
  
- **`environment-dev.yml`**: Development environment with all dependencies plus dev tools
  - Includes flake8 for linting, nbconvert for notebook execution
  - Used by CI/CD pipeline
  - Recommended for contributors

### Automated Dependency Tracking

The repository uses a combination of **Dependabot** and **GitHub Actions** to track and update dependencies:

#### 1. GitHub Actions Workflows
- **Tracked by Dependabot**: Automatically monitors and updates GitHub Actions versions weekly
- **Schedule**: Every Monday at 09:00 UTC

#### 2. Python/Conda Dependencies  
- **Weekly automated checks**: GitHub Actions workflow runs every Monday to review conda environments
- **Creates issues**: When the workflow runs, it creates/updates an issue with current dependency status
- **Manual updates required**: Conda dependencies must be manually updated in `environment.yml` files
  
**Why not automated Python dependency updates?**
Dependabot doesn't natively support conda `environment.yml` files. While we maintain `requirements.txt` files for reference, conda environments are the source of truth and must be updated manually to ensure compatibility.

### Updating Dependencies

When you need to update dependencies:

1. **Edit the appropriate `environment.yml` file** with new version requirements
2. **Sync requirements files**: Run `make sync-requirements` to update `requirements.txt` files
3. **Test the changes**: 
   ```bash
   make install-dev
   micromamba activate rse_lecture
   # Run tests and verify notebooks execute
   ```
4. **Commit both files**: Always commit both `environment.yml` and `requirements.txt` together

### Version Pinning Strategy

To ensure a stable, reproducible environment:
- **Minimum versions**: Use `>=` for minimum required versions (e.g., `numpy>=1.21.0`)
- **Specific versions**: Pin to specific versions when needed for stability
- **Weekly reviews**: GitHub Actions reminds us to check for updates weekly
- **CI validation**: All changes are tested across multiple platforms before merge

### Benefits

- **Harmonized structure**: All lectures follow the same pattern (base + lecture file)
- **Clear separation**: Each lecture's dependencies are explicit and documented
- **True inheritance**: Lecture-specific files only contain additional dependencies, avoiding duplication
- **No duplication**: Base dependencies defined once in `environment.yml`
- **Automated tracking**: GitHub Actions monitors conda dependencies, Dependabot tracks Actions
- **Known working versions**: Dependencies are frozen and tested in CI before deployment
- **Scalable**: Easy to add new lectures with different dependency requirements
- **Educational**: Students see exactly what each lecture adds beyond the base
- **Simplified Makefile**: All `install-lectureX` targets follow identical pattern

## Contributing

Contributions are welcome! When adding or modifying lectures:

1. Edit the `.py` files directly (not the `.ipynb` files)
2. Use the Jupytext percent format for cells
3. Follow the existing structure and style
4. Test that your lecture converts properly to a notebook

The repository includes a continuous integration (CI) pipeline that automatically:
- Checks Python syntax for all lecture files
- Lints code with flake8 to maintain code quality
- Converts all lectures to notebooks to verify the conversion process
- Executes all notebooks to ensure they run without errors
- Runs on Linux (Ubuntu), macOS 15 (Sequoia), macOS 26 (Tahoe), and Windows to ensure cross-platform compatibility

All pull requests must pass the CI checks before merging.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Additional Resources

- [Jupytext Documentation](https://jupytext.readthedocs.io/)
- [Jupyter Documentation](https://jupyter.org/documentation)
- [Research Software Engineering Community](https://society-rse.org/)

## Contact

For questions or suggestions, please open an issue on GitHub.