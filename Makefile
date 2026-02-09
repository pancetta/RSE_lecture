.PHONY: help install install-dev install-lecture1 install-lecture2 install-lecture3 install-lecture4 convert clean notebooks build-website serve-website clean-website

help:
	@echo "Research Software Engineering Lectures - Makefile"
	@echo ""
	@echo "Available targets:"
	@echo "  install          - Create base micromamba environment for all lectures"
	@echo "  install-dev      - Create development environment with all dependencies and dev tools"
	@echo "  install-lecture1 - Alias for install (lecture 1 uses base environment)"
	@echo "  install-lecture2 - Create environment with lecture 2 dependencies (includes matplotlib)"
	@echo "  install-lecture3 - Alias for install (lecture 3 uses base environment)"
	@echo "  install-lecture4 - Alias for install (lecture 4 uses base environment)"
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

install-dev:
	micromamba env create -f environment-dev.yml -y
	@echo "Development environment created with all dependencies and dev tools."
	@echo "Activate with: micromamba activate rse_lecture"

install-lecture1: install
	@echo "Lecture 1 uses the base environment. Activate with: micromamba activate rse_lecture"

install-lecture2:
	micromamba env create -f lecture_02/environment.yml -y
	@echo "Environment created with lecture 2 dependencies (includes matplotlib)."
	@echo "Activate with: micromamba activate rse_lecture"

install-lecture3: install
	@echo "Lecture 3 uses the base environment. Activate with: micromamba activate rse_lecture"

install-lecture4: install
	@echo "Lecture 4 uses the base environment. Activate with: micromamba activate rse_lecture"

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
