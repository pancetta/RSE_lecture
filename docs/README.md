# Documentation

This directory contains detailed documentation for various aspects of the RSE Course.

## Quick Links

### Dependency Management
- **[QUICKSTART.md](QUICKSTART.md)** - Quick reference guide for common tasks
- **[DEPENDENCY_MANAGEMENT.md](DEPENDENCY_MANAGEMENT.md)** - Complete system guide
- **[TESTING_DEPENDENCIES.md](TESTING_DEPENDENCIES.md)** - Testing procedures
- **[SOLUTION_SUMMARY.md](SOLUTION_SUMMARY.md)** - Technical overview

### Publishing and Citation
- **[PUBLISHING.md](PUBLISHING.md)** - Guide for publishing the course and obtaining a DOI

## Getting Started

### For Contributors
If you're new to the dependency management system, start with [QUICKSTART.md](QUICKSTART.md).

For detailed information on how the system works, see [DEPENDENCY_MANAGEMENT.md](DEPENDENCY_MANAGEMENT.md).

### For Course Adopters
If you're using this course material, see [PUBLISHING.md](PUBLISHING.md) for:
- How to cite the course properly
- Understanding the dual licensing (CC BY 4.0 for content, MIT for code)
- How we maintain citability through Zenodo

## Overview

### Dependency Management
The automated dependency management system:
- Tests dependency updates weekly
- Creates lock files for reproducible environments  
- Automatically creates PRs when updates work
- Maintains current versions when updates fail
- Works with conda/micromamba (no pip migration needed)

### License and Citation
The course uses dual licensing:
- **Educational content**: CC BY 4.0 (Attribution required)
- **Code examples**: MIT License

This ensures the course is open and accessible while requiring proper attribution.

See the main [README.md](../README.md) for usage examples.
