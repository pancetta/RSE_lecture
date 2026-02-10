.PHONY: help install install-dev install-lecture1 install-lecture2 install-lecture3 install-lecture4 install-lecture5 install-lecture6 install-lecture7 convert clean notebooks build-website serve-website clean-website update-deps test-deps create-locks

help:
	@echo "Research Software Engineering Lectures - Makefile"
	@echo ""
	@echo "Available targets:"
	@echo "  install          - Create base micromamba environment for all lectures"
	@echo "  install-dev      - Create development environment with all dependencies and dev tools"
	@echo "  install-lecture1 - Create environment with lecture 1 dependencies"
	@echo "  install-lecture2 - Create environment with lecture 2 dependencies"
	@echo "  install-lecture3 - Create environment with lecture 3 dependencies"
	@echo "  install-lecture4 - Create environment with lecture 4 dependencies (includes matplotlib)"
	@echo "  install-lecture5 - Create environment with lecture 5 dependencies (includes pytest, coverage)"
	@echo "  install-lecture6 - Create environment with lecture 6 dependencies"
	@echo "  install-lecture7 - Create environment with lecture 7 dependencies"
	@echo "  convert          - Convert all Python lectures to Jupyter notebooks"
	@echo "  notebooks        - Alias for convert"
	@echo "  build-website    - Build the Jupyter Book website"
	@echo "  serve-website    - Build and serve the website locally"
	@echo "  clean            - Remove generated notebook files"
	@echo "  clean-website    - Remove generated website files"
	@echo "  update-deps      - Test and update conda dependencies with lock files"
	@echo "  test-deps        - Test current dependencies without creating lock files"
	@echo "  create-locks     - Create conda-lock files for all platforms"
	@echo "  help             - Show this help message"

install:
	micromamba env create -f environment.yml -y
	@echo "Base environment created. Activate with: micromamba activate rse_lecture"

install-dev:
	micromamba env create -f environment-dev.yml -y
	@echo "Development environment created with all dependencies and dev tools."
	@echo "Activate with: micromamba activate rse_lecture"

install-lecture1:
	@echo "Creating base environment..."
	micromamba env create -f environment.yml -y
	@echo "Adding lecture 1 specific dependencies..."
	micromamba env update -f lecture_01/environment.yml -y
	@echo "Environment created for lecture 1."
	@echo "Activate with: micromamba activate rse_lecture"

install-lecture2:
	@echo "Creating base environment..."
	micromamba env create -f environment.yml -y
	@echo "Adding lecture 2 specific dependencies..."
	micromamba env update -f lecture_02/environment.yml -y
	@echo "Environment created for lecture 2."
	@echo "Activate with: micromamba activate rse_lecture"

install-lecture3:
	@echo "Creating base environment..."
	micromamba env create -f environment.yml -y
	@echo "Adding lecture 3 specific dependencies..."
	micromamba env update -f lecture_03/environment.yml -y
	@echo "Environment created for lecture 3."
	@echo "Activate with: micromamba activate rse_lecture"

install-lecture4:
	@echo "Creating base environment..."
	micromamba env create -f environment.yml -y
	@echo "Adding lecture 4 specific dependencies..."
	micromamba env update -f lecture_04/environment.yml -y
	@echo "Environment created for lecture 4 (base + matplotlib)."
	@echo "Activate with: micromamba activate rse_lecture"

install-lecture5:
	@echo "Creating base environment..."
	micromamba env create -f environment.yml -y
	@echo "Adding lecture 5 specific dependencies..."
	micromamba env update -f lecture_05/environment.yml -y
	@echo "Environment created for lecture 5 (base + pytest, pytest-cov)."
	@echo "Activate with: micromamba activate rse_lecture"

install-lecture6:
	@echo "Creating base environment..."
	micromamba env create -f environment.yml -y
	@echo "Adding lecture 6 specific dependencies..."
	micromamba env update -f lecture_06/environment.yml -y
	@echo "Environment created for lecture 6."
	@echo "Activate with: micromamba activate rse_lecture"

install-lecture7:
	@echo "Creating base environment..."
	micromamba env create -f environment.yml -y
	@echo "Adding lecture 7 specific dependencies..."
	micromamba env update -f lecture_07/environment.yml -y
	@echo "Environment created for lecture 7."
	@echo "Activate with: micromamba activate rse_lecture"

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

update-deps:
	python update_dependencies.py
	@echo "Dependencies tested and lock files updated"

test-deps:
	python update_dependencies.py --test-only
	@echo "Dependency testing complete"

create-locks:
	python update_dependencies.py --create-locks
	@echo "Lock files created for all platforms"
