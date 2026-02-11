#!/usr/bin/env python3
"""
Convert all lecture Python files to Jupyter notebooks using Jupytext.

This script finds all lecture .py files and converts them to .ipynb format.
It also generates QR codes for the course website and each lecture.
"""

import os
import subprocess
from pathlib import Path


def generate_qr_codes():
    """Generate QR codes for course and lectures."""
    try:
        import qrcode
    except ImportError:
        print("Warning: qrcode library not found. Skipping QR code generation.")
        print("Install with: pip install qrcode[pil]")
        return False

    base_dir = Path(__file__).parent
    course_url = "https://pancetta.github.io/RSE_course_JuRSE"

    # Create QR code for the main course website
    course_qr_path = base_dir / "course_qr_code.png"
    if not course_qr_path.exists():
        print(f"Generating QR code for course website: {course_url}")
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(course_url)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(course_qr_path)

    # Find all lecture directories
    lecture_dirs = sorted([d for d in base_dir.glob('lecture_*') if d.is_dir()])

    for lecture_dir in lecture_dirs:
        lecture_name = lecture_dir.name
        lecture_number = lecture_name.split('_')[1]

        # Generate URL for this lecture
        lecture_url = f"{course_url}/{lecture_name}/lecture_{lecture_number}.html"

        # Output path for QR code
        qr_path = lecture_dir / f"lecture_{lecture_number}_qr_code.png"

        if not qr_path.exists():
            print(f"Generating QR code for {lecture_name}: {lecture_url}")
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(lecture_url)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")
            img.save(qr_path)

    return True


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
        print(f"  [OK] Created {notebook_file}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"  [ERROR] Error converting {lecture_file}: {e}")
        return False
    except FileNotFoundError:
        print("  [ERROR] Error: jupytext not found. Please install it with: pip install jupytext")
        return False


def main():
    """Find and convert all lecture files."""
    # Get the directory where this script is located
    base_dir = Path(__file__).parent

    # Generate QR codes first
    print("Generating QR codes...\n")
    generate_qr_codes()
    print()

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
