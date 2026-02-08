.PHONY: help install convert clean notebooks

help:
	@echo "Research Software Engineering Lectures - Makefile"
	@echo ""
	@echo "Available targets:"
	@echo "  install    - Install required dependencies"
	@echo "  convert    - Convert all Python lectures to Jupyter notebooks"
	@echo "  notebooks  - Alias for convert"
	@echo "  clean      - Remove generated notebook files"
	@echo "  help       - Show this help message"

install:
	pip install -r requirements.txt

convert: notebooks

notebooks:
	python convert_to_notebooks.py

clean:
	find . -name "*.ipynb" -not -path "./.git/*" -delete
	@echo "Cleaned all generated notebooks"
