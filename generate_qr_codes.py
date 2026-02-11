#!/usr/bin/env python3
"""
Generate QR codes for the course website and individual lectures.

This script creates QR code images for:
- The main course website
- Each individual lecture page
"""

import os
from pathlib import Path


def generate_qr_code(url, output_path):
    """
    Generate a QR code for the given URL and save it to output_path.
    
    Args:
        url: The URL to encode in the QR code
        output_path: Path where the QR code image will be saved
    """
    try:
        import qrcode
    except ImportError:
        print("Error: qrcode library not found.")
        print("Please install it with: pip install qrcode[pil]")
        return False
    
    # Create QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    # Create an image
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save the image
    img.save(output_path)
    print(f"Generated QR code: {output_path}")
    return True


def main():
    """Generate all QR codes for the course."""
    base_dir = Path(__file__).parent
    
    # Course website URL
    course_url = "https://pancetta.github.io/RSE_course_JuRSE"
    
    # Create QR code for the main course website
    course_qr_path = base_dir / "course_qr_code.png"
    print(f"Generating QR code for course website: {course_url}")
    generate_qr_code(course_url, course_qr_path)
    
    # Find all lecture directories
    lecture_dirs = sorted([d for d in base_dir.glob('lecture_*') if d.is_dir()])
    
    print(f"\nFound {len(lecture_dirs)} lecture directories")
    
    for lecture_dir in lecture_dirs:
        lecture_name = lecture_dir.name
        lecture_number = lecture_name.split('_')[1]
        
        # Generate URL for this lecture
        lecture_url = f"{course_url}/{lecture_name}/lecture_{lecture_number}.html"
        
        # Output path for QR code
        qr_path = lecture_dir / f"lecture_{lecture_number}_qr_code.png"
        
        print(f"Generating QR code for {lecture_name}: {lecture_url}")
        generate_qr_code(lecture_url, qr_path)
    
    print("\nQR code generation complete!")


if __name__ == '__main__':
    main()
