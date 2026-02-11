# Research Software Engineering Lectures

[![CI - Lecture Scripts](https://github.com/pancetta/RSE_course_JuRSE/workflows/CI%20-%20Lecture%20Scripts/badge.svg)](https://github.com/pancetta/RSE_course_JuRSE/actions)

Welcome to the Research Software Engineering (RSE) lecture series! This repository contains materials for learning best practices in developing high-quality research software.

## Overview

This lecture series covers fundamental concepts and practices in Research Software Engineering, including:

- **Lecture 1**: Introduction to RSE, Shell Basics, and Git Fundamentals (~90 minutes)
- **Lecture 2**: Advanced Git, GitHub & GitLab Collaboration, and Python Basics (~90 minutes)
- **Lecture 3**: Python Fundamentals and Advanced Concepts (including Error Handling) (~90 minutes)
- **Lecture 4**: Python Project Structure and Working with Libraries (NumPy, Matplotlib) (~90 minutes)
- **Lecture 5**: Testing Research Software (~90 minutes)
- **Lecture 6**: Automation and Continuous Integration (~90 minutes)
- **Lecture 7**: Debugging and Profiling Research Software (~90 minutes)
- **Lecture 8**: Documenting and Publishing Research Software (~90 minutes)
- **Lecture 9**: Containerization and Reproducibility (~90 minutes)
- **Lecture 10**: Collaboration and Code Review in Research Software (~90 minutes)
- **Lecture 11**: Working with Research Data - File Formats and Databases (~90 minutes)
- **Lecture 12**: AI-Assisted Coding for Research Software (~90 minutes)

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
git clone https://github.com/pancetta/RSE_course_JuRSE.git
cd RSE_course_JuRSE
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

# Lecture 5 (adds pytest, pytest-cov)
make install-lecture5

# Lecture 6
make install-lecture6

# Lecture 7
make install-lecture7

# Lecture 8
make install-lecture8

# Lecture 9
make install-lecture9

# Lecture 10
make install-lecture10

# Lecture 11 (adds h5py, netCDF4, pandas)
make install-lecture11

# Lecture 12
make install-lecture12
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
- Lectures 1-3 have empty dependency lists (use base only).
- Lecture 4 adds matplotlib.
- Lecture 5 adds pytest and pytest-cov for testing.
- Lecture 6 has no additional dependencies (uses base only).
- Lecture 7 has no additional dependencies (uses base only for pdb, logging, cProfile).
- Lecture 8 has no additional dependencies (documentation tools covered conceptually).
- Lecture 9 has no additional dependencies (containerization tools covered conceptually).
- Lecture 10 has no additional dependencies (collaboration tools covered conceptually).
- Lecture 11 adds h5py, netCDF4, and pandas for working with research data formats.
- Lecture 12 has no additional dependencies (AI coding tools are IDE extensions, not Python packages).
- The `environment-dev.yml` includes all dependencies plus development tools (flake8, nbconvert).
- Installation pattern is **harmonized**: all lectures follow the same two-step process (base + additions).
- Lecture 1 introduces the course and essential tools (shell, git, GitHub).
- Lecture 2 introduces Python basics (uses standard library only).
- Lecture 3 focuses on advanced Python using the standard library.
- Lecture 4 covers NumPy, matplotlib, and project structure.
- Lecture 5 covers testing with pytest and achieving full test coverage.
- Lecture 6 covers automation and continuous integration with GitHub Actions and GitLab CI.
- Lecture 7 covers debugging with pdb and profiling with cProfile.
- Lecture 8 covers documenting and publishing research software (Sphinx, PyPI, Zenodo).
- Lecture 9 covers containerization and reproducibility (Docker, Podman, Apptainer).
- Lecture 10 covers collaboration and code review in research software teams.
- Lecture 11 covers working with research data, file formats (HDF5, NetCDF), and databases.
- Lecture 12 covers AI-assisted coding tools, best practices, and privacy considerations.

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

This repository uses a multi-environment approach for clean dependency separation:

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

### Benefits

- **Harmonized structure**: All lectures follow the same pattern (base + lecture file)
- **Clear separation**: Each lecture's dependencies are explicit and documented
- **True inheritance**: Lecture-specific files only contain additional dependencies, avoiding duplication
- **No duplication**: Base dependencies defined once in `environment.yml`
- **Dependabot compatible**: All `environment.yml` files are automatically tracked for security updates
- **Scalable**: Easy to add new lectures with different dependency requirements
- **Educational**: Students see exactly what each lecture adds beyond the base
- **Simplified Makefile**: All `install-lectureX` targets follow identical pattern

### Automated Dependency Updates

This repository includes an automated system for testing and updating conda dependencies:

**How it works:**
- A GitHub Actions workflow runs weekly (every Monday at 9:00 UTC)
- Tests all dependencies with the current lecture materials
- Creates conda-lock files for reproducible environments
- Automatically creates a PR if updates are available and tests pass
- If tests fail, maintains the current working versions

**Manual dependency testing:**
```bash
# Test current dependencies (without creating lock files)
make test-deps

# Test dependencies and create lock files
make update-deps

# Just create lock files (no testing)
make create-locks
```

**Using lock files for reproducible environments:**
```bash
# Install from lock file (exact versions)
micromamba create -n rse_lecture --file environment-dev-linux-64.lock

# Platform-specific lock files available:
# - linux-64
# - osx-64 (macOS Intel)
# - osx-arm64 (macOS Apple Silicon)
# - win-64
```

**When dependency updates fail:**
The automated system will NOT create a PR if tests fail. Instead:
1. The workflow logs will show which package caused the failure
2. Maintainers can pin the problematic version in `environment.yml` or `environment-dev.yml`
3. Example pinning:
   ```yaml
   dependencies:
     - matplotlib>=3.5.0,<3.9.0  # Exclude breaking version
     - numpy==1.24.0  # Pin to specific working version
   ```
4. The next weekly run will test with the pinned versions

This ensures the repository always contains executable versions of the lectures with compatible dependencies.

**For more details, see the [dependency management documentation](docs/).**

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

## Acknowledgements

This course has been developed drawing on best practices and content from several excellent resources in the Research Software Engineering community:

### Primary Influences

- **Research Software Engineering with Python** by The Alan Turing Institute  
  <https://alan-turing-institute.github.io/rse-course/html/>  
  This comprehensive RSE course has significantly influenced our pedagogical approach, course structure, and content organization.

- **Research Software Engineering with Python** by Damien Irving, Kate Hertweck, Luke Johnston, Joel Ostblom, Charlotte Wickham, and Greg Wilson (2022)  
  <https://third-bit.com/py-rse/>  
  This excellent textbook informed our treatment of research software engineering principles, testing practices, and project organization.

### Platform Documentation

Our lectures on Git, GitHub, GitLab, and CI/CD reference and build upon official documentation:

- **Git Documentation & Pro Git Book** by Scott Chacon and Ben Straub  
  <https://git-scm.com/book/en/v2>

- **GitHub Documentation**  
  <https://docs.github.com/>

- **GitLab Documentation**  
  <https://docs.gitlab.com/>

### Scientific Python Ecosystem

Our coverage of Python libraries builds on official documentation and community resources:

- **NumPy Documentation**: <https://numpy.org/doc/>
- **Matplotlib Documentation**: <https://matplotlib.org/stable/>
- **pytest Documentation**: <https://docs.pytest.org/>
- **Python Documentation**: <https://docs.python.org/3/>

### Additional Resources

- **Software Carpentry**: Shell and Git lessons  
  <https://software-carpentry.org/>

- **Society of Research Software Engineering**  
  <https://society-rse.org/>

### Notes

While this course draws inspiration and ideas from these sources, all lecture content, examples, and exercises have been developed independently for this specific educational context. Each lecture includes detailed acknowledgements and references to specific sources used.

For complete bibliographic information, see [`references.bib`](references.bib).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

We welcome contributions! Before submitting changes:

1. **Run local CI checks** to catch issues before pushing:
   ```bash
   make ci-local
   ```

2. See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines on:
   - Running flake8 linting locally
   - Checking Python syntax
   - Converting and testing notebooks
   - Common flake8 errors and how to fix them
   - Setting up pre-commit hooks

**Running `make ci-local` before committing prevents CI failures!**

## Additional Resources

- [Jupytext Documentation](https://jupytext.readthedocs.io/)
- [Jupyter Documentation](https://jupyter.org/documentation)
- [Research Software Engineering Community](https://society-rse.org/)

## Contact

For questions or suggestions, please open an issue on GitHub.