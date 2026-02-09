#!/usr/bin/env python3
"""
Sync requirements.txt files from environment.yml files.

This script converts conda environment.yml files to pip requirements.txt files
to enable Dependabot tracking. It should be run whenever environment.yml files
are updated.
"""

import yaml
import os
from pathlib import Path


def extract_pip_dependencies(env_file):
    """
    Extract pip-installable dependencies from a conda environment.yml file.
    
    Args:
        env_file: Path to environment.yml file
        
    Returns:
        List of dependency strings
    """
    with open(env_file, 'r') as f:
        env_data = yaml.safe_load(f)
    
    dependencies = env_data.get('dependencies', [])
    pip_deps = []
    
    for dep in dependencies:
        if isinstance(dep, str):
            # Simple dependency like "numpy>=1.21.0"
            # Remove conda-specific syntax if any
            pip_deps.append(dep)
        elif isinstance(dep, dict) and 'pip' in dep:
            # Pip dependencies specified in conda file
            pip_deps.extend(dep['pip'])
    
    return pip_deps


def write_requirements_file(deps, output_file, header_comment):
    """
    Write dependencies to a requirements.txt file.
    
    Args:
        deps: List of dependency strings
        output_file: Path to output requirements.txt file
        header_comment: Comment describing this file
    """
    with open(output_file, 'w') as f:
        f.write(header_comment)
        if deps:
            f.write('\n')
            for dep in deps:
                f.write(f"{dep}\n")


def sync_requirements():
    """Sync all requirements.txt files from environment.yml files."""
    base_dir = Path(__file__).parent
    
    # Base environment
    print("Syncing base requirements.txt...")
    deps = extract_pip_dependencies(base_dir / 'environment.yml')
    header = (
        "# Base requirements for RSE lecture series\n"
        "# Auto-generated from environment.yml - DO NOT EDIT MANUALLY\n"
        "# To update: modify environment.yml and run 'make sync-requirements'\n"
    )
    write_requirements_file(deps, base_dir / 'requirements.txt', header)
    print(f"  ✓ Created requirements.txt with {len(deps)} dependencies")
    
    # Development environment
    print("Syncing development requirements.txt...")
    deps = extract_pip_dependencies(base_dir / 'environment-dev.yml')
    header = (
        "# Development requirements for RSE lecture series\n"
        "# Auto-generated from environment-dev.yml - DO NOT EDIT MANUALLY\n"
        "# To update: modify environment-dev.yml and run 'make sync-requirements'\n"
    )
    write_requirements_file(deps, base_dir / 'requirements-dev.txt', header)
    print(f"  ✓ Created requirements-dev.txt with {len(deps)} dependencies")
    
    # Lecture-specific environments
    for i in range(1, 5):
        lecture_dir = base_dir / f'lecture_{i:02d}'
        env_file = lecture_dir / 'environment.yml'
        req_file = lecture_dir / 'requirements.txt'
        
        print(f"Syncing lecture {i} requirements.txt...")
        deps = extract_pip_dependencies(env_file)
        header = (
            f"# Additional requirements for Lecture {i}\n"
            "# Auto-generated from environment.yml - DO NOT EDIT MANUALLY\n"
            "# To update: modify environment.yml and run 'make sync-requirements'\n"
        )
        if not deps:
            header += f"# Lecture {i} uses only base dependencies (no additions needed)\n"
        write_requirements_file(deps, req_file, header)
        print(f"  ✓ Created lecture_{i:02d}/requirements.txt with {len(deps)} dependencies")
    
    print("\n✅ All requirements.txt files synced successfully!")
    print("\nNext steps:")
    print("  1. Review the generated requirements.txt files")
    print("  2. Commit them to git: git add requirements*.txt lecture_*/requirements.txt")
    print("  3. Dependabot will now track these dependencies weekly")


if __name__ == '__main__':
    sync_requirements()
