# Research Software Engineering Lectures

[![CI - Lecture Scripts](https://github.com/pancetta/RSE_lecture/workflows/CI%20-%20Lecture%20Scripts/badge.svg)](https://github.com/pancetta/RSE_lecture/actions)

Welcome to the Research Software Engineering (RSE) lecture series! This repository contains materials for learning best practices in developing high-quality research software.

## Overview

This lecture series covers fundamental concepts and practices in Research Software Engineering, including:

- **Lecture 1**: Introduction to Research Software Engineering
- **Lecture 2**: Testing and Continuous Integration
- **Lecture 3**: Documentation and Code Quality

## Structure

Each lecture is organized in its own directory and consists of:
- A Python file (`.py`) that contains the lecture content in Jupytext format
- The file can be converted to a Jupyter notebook (`.ipynb`) using Jupytext

## Getting Started

### Prerequisites

- Python 3.7 or higher
- micromamba or conda/mamba

### Installation

1. Clone this repository:
```bash
git clone https://github.com/pancetta/RSE_lecture.git
cd RSE_lecture
```

2. Install [micromamba](https://mamba.readthedocs.io/en/latest/installation/micromamba-installation.html) if you haven't already.

3. Create and activate the environment:

**For all lectures:**
```bash
micromamba env create -f environment.yml
micromamba activate rse_lecture
```

Or using the Makefile:
```bash
make install
micromamba activate rse_lecture
```

**For lecture 1 (requires additional matplotlib dependency):**
```bash
micromamba env create -f environment.yml
micromamba install -n rse_lecture -f lecture_01/environment.yml
micromamba activate rse_lecture
```

Or using the Makefile:
```bash
make install-lecture1
micromamba activate rse_lecture
```

**For lectures 2 and 3 (use base environment):**
```bash
make install-lecture2  # or install-lecture3
micromamba activate rse_lecture
```

**Note:** The main `environment.yml` contains all common dependencies (Python, Jupyter, NumPy, etc.). Individual lectures may have additional dependencies specified in their own `environment.yml` files. If a lecture has no additional dependencies, it uses only the base environment.

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

All pull requests must pass the CI checks before merging.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Additional Resources

- [Jupytext Documentation](https://jupytext.readthedocs.io/)
- [Jupyter Documentation](https://jupyter.org/documentation)
- [Research Software Engineering Community](https://society-rse.org/)

## Contact

For questions or suggestions, please open an issue on GitHub.