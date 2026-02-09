# Dependency Management Documentation

This directory contains detailed documentation for the automated conda dependency management system.

## Quick Links

- **[QUICKSTART.md](QUICKSTART.md)** - Quick reference guide for common tasks
- **[DEPENDENCY_MANAGEMENT.md](DEPENDENCY_MANAGEMENT.md)** - Complete system guide
- **[TESTING_DEPENDENCIES.md](TESTING_DEPENDENCIES.md)** - Testing procedures
- **[SOLUTION_SUMMARY.md](SOLUTION_SUMMARY.md)** - Technical overview

## Getting Started

If you're new to the dependency management system, start with [QUICKSTART.md](QUICKSTART.md).

For detailed information on how the system works, see [DEPENDENCY_MANAGEMENT.md](DEPENDENCY_MANAGEMENT.md).

## Overview

The automated dependency management system:
- Tests dependency updates weekly
- Creates lock files for reproducible environments  
- Automatically creates PRs when updates work
- Maintains current versions when updates fail
- Works with conda/micromamba (no pip migration needed)

See the main [README.md](../README.md) for usage examples.
