# Research Software Engineering Lectures

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
- pip (Python package manager)

### Installation

1. Clone this repository:
```bash
git clone https://github.com/pancetta/RSE_lecture.git
cd RSE_lecture
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Building the Website

This repository can generate a beautiful static website from the lectures using [Jupyter Book](https://jupyterbook.org/).

#### Build the website:
```bash
make build-website
```

This will:
1. Convert all Python lecture files to Jupyter notebooks
2. Build a static website in the `_build/html` directory

#### Serve the website locally:
```bash
make serve-website
```

This will build the website and start a local web server at `http://localhost:8000`.

You can then view the website in your browser to see all lectures rendered with:
- Interactive navigation
- Formatted code cells
- Rendered plots and outputs
- Cross-references between lectures
- Responsive design for mobile and desktop

#### Deploy to GitHub Pages:

The repository includes a GitHub Actions workflow that automatically builds and deploys the website to GitHub Pages whenever changes are pushed to the main branch.

To enable GitHub Pages:
1. Go to your repository's Settings
2. Navigate to Pages
3. Under "Build and deployment", select "GitHub Actions" as the source
4. The website will be automatically deployed on every push to main

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

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Additional Resources

- [Jupytext Documentation](https://jupytext.readthedocs.io/)
- [Jupyter Documentation](https://jupyter.org/documentation)
- [Research Software Engineering Community](https://society-rse.org/)

## Contact

For questions or suggestions, please open an issue on GitHub.