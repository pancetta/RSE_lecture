.PHONY: help install install-micromamba install-lecture1 install-lecture2 install-lecture3 convert clean notebooks build-website serve-website clean-website

help:
	@echo "Research Software Engineering Lectures - Makefile"
	@echo ""
	@echo "Available targets:"
	@echo "  install              - Install required dependencies using pip"
	@echo "  install-micromamba   - Create micromamba environment for all lectures"
	@echo "  install-lecture1     - Create micromamba environment for lecture 1"
	@echo "  install-lecture2     - Create micromamba environment for lecture 2"
	@echo "  install-lecture3     - Create micromamba environment for lecture 3"
	@echo "  convert              - Convert all Python lectures to Jupyter notebooks"
	@echo "  notebooks            - Alias for convert"
	@echo "  build-website        - Build the Jupyter Book website"
	@echo "  serve-website        - Build and serve the website locally"
	@echo "  clean                - Remove generated notebook files"
	@echo "  clean-website        - Remove generated website files"
	@echo "  help                 - Show this help message"

install:
	pip install -r requirements.txt

install-micromamba:
	micromamba env create -f environment.yml -y
	@echo "Environment created. Activate with: micromamba activate rse_lecture"

install-lecture1:
	micromamba env create -f lecture_01/environment.yml -y
	@echo "Environment created. Activate with: micromamba activate rse_lecture_01"

install-lecture2:
	micromamba env create -f lecture_02/environment.yml -y
	@echo "Environment created. Activate with: micromamba activate rse_lecture_02"

install-lecture3:
	micromamba env create -f lecture_03/environment.yml -y
	@echo "Environment created. Activate with: micromamba activate rse_lecture_03"

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
