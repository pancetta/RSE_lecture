#!/usr/bin/env python3
"""
Add QR code sections to all lecture Python files.

This script adds QR codes at the beginning of each lecture file
for quick access to the course website and the specific lecture.
"""

from pathlib import Path


def add_qr_codes_to_lecture(lecture_file, lecture_number):
    """
    Add QR codes section to a lecture Python file.
    
    Args:
        lecture_file: Path to the lecture .py file
        lecture_number: The lecture number (e.g., "01", "02", etc.)
    """
    # Read the file
    with open(lecture_file, 'r') as f:
        content = f.read()
    
    # Check if QR codes already exist
    if '## Quick Access' in content or 'course_qr_code.png' in content:
        print(f"QR codes already exist in {lecture_file}, skipping")
        return True
    
    lines = content.split('\n')
    
    # Find the line after the title (first # %% [markdown] followed by title)
    insert_index = None
    for i, line in enumerate(lines):
        if line.strip().startswith('# # Lecture'):
            # Found the title, insert right after the title line
            # Skip any empty comment lines after title
            j = i + 1
            while j < len(lines) and (lines[j].strip() == '#' or lines[j].strip() == ''):
                j += 1
            insert_index = j
            break
    
    if insert_index is None:
        print(f"Could not find appropriate insertion point in {lecture_file}")
        return False
    
    # Create QR code section
    qr_section = [
        '# ',
        '# ## Quick Access',
        '# ',
        '# Scan the QR codes below for quick access to course materials:',
        '# ',
        '# <div style="display: flex; gap: 20px; align-items: flex-start;">',
        '#   <div style="text-align: center;">',
        '#     <img src="../course_qr_code.png" alt="Course Website QR Code" width="150"/>',
        '#     <p><strong>Course Website</strong></p>',
        '#   </div>',
        '#   <div style="text-align: center;">',
        f'#     <img src="lecture_{lecture_number}_qr_code.png" alt="This Lecture QR Code" width="150"/>',
        '#     <p><strong>This Lecture</strong></p>',
        '#   </div>',
        '# </div>',
        '# ',
    ]
    
    # Insert the QR section
    lines[insert_index:insert_index] = qr_section
    
    # Write the file back
    with open(lecture_file, 'w') as f:
        f.write('\n'.join(lines))
    
    print(f"Added QR codes to {lecture_file}")
    return True


def main():
    """Add QR codes to all lecture files."""
    # Get repository root (parent of scripts directory)
    base_dir = Path(__file__).parent.parent
    
    # Find all lecture directories
    lecture_dirs = sorted([d for d in base_dir.glob('lecture_*') if d.is_dir()])
    
    print(f"Found {len(lecture_dirs)} lecture directories\n")
    
    success_count = 0
    for lecture_dir in lecture_dirs:
        lecture_name = lecture_dir.name
        lecture_number = lecture_name.split('_')[1]
        
        # Find the lecture Python file
        lecture_file = lecture_dir / f"lecture_{lecture_number}.py"
        
        if not lecture_file.exists():
            print(f"Lecture file not found: {lecture_file}")
            continue
        
        if add_qr_codes_to_lecture(lecture_file, lecture_number):
            success_count += 1
    
    print(f"\nSuccessfully updated {success_count} lecture files")


if __name__ == '__main__':
    main()
