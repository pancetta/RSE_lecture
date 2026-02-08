.PHONY: help install convert clean notebooks build-website serve-website clean-website

help:
	@echo "Research Software Engineering Lectures - Makefile"
	@echo ""
	@echo "Available targets:"
	@echo "  install        - Install required dependencies"
	@echo "  convert        - Convert all Python lectures to Jupyter notebooks"
	@echo "  notebooks      - Alias for convert"
	@echo "  build-website  - Build the Jupyter Book website"
	@echo "  serve-website  - Build and serve the website locally"
	@echo "  clean          - Remove generated notebook files"
	@echo "  clean-website  - Remove generated website files"
	@echo "  help           - Show this help message"

install:
	pip install -r requirements.txt

convert: notebooks

notebooks:
	python convert_to_notebooks.py

build-website: notebooks
	jupyter-book build --html .

serve-website: build-website
	@echo "Opening website in browser..."
	@echo "Website built at: _build/html/index.html"
	@python -m http.server --directory _build/html 8000

clean:
	find . -name "*.ipynb" -not -path "./.git/*" -not -path "./_build/*" -delete
	@echo "Cleaned all generated notebooks"

clean-website:
	jupyter-book clean .
	@echo "Cleaned website build files"
