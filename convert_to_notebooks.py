#!/usr/bin/env python3
"""
Convert all lecture Python files to Jupyter notebooks using Jupytext.

This script finds all lecture .py files and converts them to .ipynb format.
"""

import os
import subprocess
from pathlib import Path


def convert_lecture(lecture_file):
    """Convert a single lecture Python file to a Jupyter notebook."""
    print(f"Converting {lecture_file}...")
    try:
        result = subprocess.run(
            ['jupytext', '--to', 'notebook', str(lecture_file)],
            capture_output=True,
            text=True,
            check=True
        )
        notebook_file = lecture_file.with_suffix('.ipynb')
        print(f"  ✓ Created {notebook_file}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"  ✗ Error converting {lecture_file}: {e}")
        return False
    except FileNotFoundError:
        print("  ✗ Error: jupytext not found. Please install it with: pip install jupytext")
        return False


def main():
    """Find and convert all lecture files."""
    # Get the directory where this script is located
    base_dir = Path(__file__).parent
    
    # Find all lecture directories
    lecture_dirs = sorted([d for d in base_dir.glob('lecture_*') if d.is_dir()])
    
    if not lecture_dirs:
        print("No lecture directories found.")
        return
    
    print(f"Found {len(lecture_dirs)} lecture directories\n")
    
    converted = 0
    failed = 0
    
    for lecture_dir in lecture_dirs:
        # Find Python files in the lecture directory
        py_files = list(lecture_dir.glob('*.py'))
        
        for py_file in py_files:
            if convert_lecture(py_file):
                converted += 1
            else:
                failed += 1
    
    print(f"\n{'='*50}")
    print(f"Conversion complete!")
    print(f"Successfully converted: {converted}")
    print(f"Failed: {failed}")
    print(f"{'='*50}")


if __name__ == '__main__':
    main()
