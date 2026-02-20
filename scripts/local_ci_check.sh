#!/bin/bash
# Local CI check script - runs the same checks as CI before committing
# This helps catch issues before pushing to remote

set -e  # Exit on error

echo "=========================================="
echo "Running Local CI Checks"
echo "=========================================="
echo ""

# Check if we're in the right directory
if [ ! -f "scripts/convert_to_notebooks.py" ]; then
    echo "Error: Must be run from repository root"
    exit 1
fi

echo "1. Checking Python syntax errors..."
echo "-----------------------------------"
python -m py_compile scripts/convert_to_notebooks.py
for lecture_file in lecture_*/lecture_*.py; do
    echo "  Checking: $lecture_file"
    python -m py_compile "$lecture_file"
done
echo "✓ All Python syntax checks passed"
echo ""

echo "2. Running flake8 linting (strict)..."
echo "--------------------------------------"
if ! command -v flake8 &> /dev/null; then
    echo "❌ flake8 not found. Please install the environment:"
    echo "   make install"
    exit 1
fi
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
echo "✓ No critical flake8 errors"
echo ""

echo "3. Running flake8 linting (full)..."
echo "------------------------------------"
# Run and capture output
if flake8 . --count --statistics; then
    echo "✓ All flake8 checks passed"
else
    echo ""
    echo "❌ Flake8 found issues. Please fix them before committing."
    exit 1
fi
echo ""

echo "4. Converting lectures to notebooks..."
echo "---------------------------------------"
python scripts/convert_to_notebooks.py
echo "✓ Notebooks converted successfully"
echo ""

echo "5. Verifying notebooks were created..."
echo "---------------------------------------"
for lecture_file in lecture_*/lecture_*.py; do
    notebook_file="${lecture_file%.py}.ipynb"
    if [ ! -f "$notebook_file" ]; then
        echo "❌ Notebook not found: $notebook_file"
        exit 1
    fi
done
echo "✓ All notebooks verified"
echo ""

echo "=========================================="
echo "✓ All local CI checks passed!"
echo "=========================================="
echo ""
echo "Safe to commit and push. CI should pass."
echo ""
