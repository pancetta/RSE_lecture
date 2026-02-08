.PHONY: help install install-lecture1 install-lecture2 install-lecture3 convert clean notebooks build-website serve-website clean-website

help:
	@echo "Research Software Engineering Lectures - Makefile"
	@echo ""
	@echo "Available targets:"
	@echo "  install          - Create base micromamba environment for all lectures"
	@echo "  install-lecture1 - Create environment with lecture 1 additional dependencies"
	@echo "  install-lecture2 - Alias for install (lecture 2 uses base environment)"
	@echo "  install-lecture3 - Alias for install (lecture 3 uses base environment)"
	@echo "  convert          - Convert all Python lectures to Jupyter notebooks"
	@echo "  notebooks        - Alias for convert"
	@echo "  build-website    - Build the Jupyter Book website"
	@echo "  serve-website    - Build and serve the website locally"
	@echo "  clean            - Remove generated notebook files"
	@echo "  clean-website    - Remove generated website files"
	@echo "  help             - Show this help message"

install:
	micromamba env create -f environment.yml -y
	@echo "Base environment created. Activate with: micromamba activate rse_lecture"

install-lecture1:
	micromamba env create -f environment.yml -y
	micromamba install -n rse_lecture -c conda-forge matplotlib>=3.5.0 -y
	@echo "Environment created with lecture 1 dependencies. Activate with: micromamba activate rse_lecture"

install-lecture2: install
	@echo "Lecture 2 uses the base environment. Activate with: micromamba activate rse_lecture"

install-lecture3: install
	@echo "Lecture 3 uses the base environment. Activate with: micromamba activate rse_lecture"

convert: notebooks

notebooks:
	python convert_to_notebooks.py

build-website: notebooks
	@echo "Building Jupyter Book v2 static HTML site..."
	@jupyter-book build --html
	@echo "✅ Static HTML site built in _build/html/"

serve-website: notebooks
	@echo "Starting Jupyter Book development server..."
	@echo "Press Ctrl+C to stop the server"
	@jupyter-book start --port 8000

clean:
	find . -name "*.ipynb" -not -path "./.git/*" -not -path "./_build/*" -delete
	@echo "Cleaned all generated notebooks"

clean-website:
	jupyter-book clean .
	@echo "Cleaned website build files"
