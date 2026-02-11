# Documentation

This directory contains detailed documentation for various aspects of the RSE Course.

## For Students

- **[Main README](../README.md)** - Course overview and getting started

## For Contributors and Developers

- **[Contributing Guide](../CONTRIBUTING.md)** - How to contribute to the course
- **[Developer Guide](DEVELOPER_GUIDE.md)** - Complete development guide
  - Repository structure
  - Development workflow
  - Adding/modifying lectures
  - CI/CD pipeline details
  - Make targets reference

## For Course Adopters and Instructors

- **[Publishing Guide](PUBLISHING.md)** - Citation and publishing information
  - How to cite the course properly
  - Understanding dual licensing (CC BY 4.0 for content, MIT for code)
  - How to obtain a DOI through Zenodo

## For Maintainers

### Dependency Management
- **[Quick Start](QUICKSTART.md)** - Quick reference for common tasks
- **[Dependency Management](DEPENDENCY_MANAGEMENT.md)** - Complete system guide
- **[Testing Dependencies](TESTING_DEPENDENCIES.md)** - Testing procedures
- **[Solution Summary](SOLUTION_SUMMARY.md)** - Technical overview of the system

The automated dependency management system:
- Tests dependency updates weekly
- Creates lock files for reproducible environments  
- Automatically creates PRs when updates work
- Maintains current versions when updates fail

## Quick Links by Task

### I want to...

**...use the course materials:**
→ Start with the [main README](../README.md)

**...contribute to the course:**
→ Read [CONTRIBUTING.md](../CONTRIBUTING.md) and [DEVELOPER_GUIDE.md](DEVELOPER_GUIDE.md)

**...cite the course in my work:**
→ See [PUBLISHING.md](PUBLISHING.md)

**...manage dependencies:**
→ Check [QUICKSTART.md](QUICKSTART.md) for quick reference

**...understand how things work:**
→ Read [DEVELOPER_GUIDE.md](DEVELOPER_GUIDE.md) for technical details

**...teach this course:**
→ Review [main README](../README.md) and [PUBLISHING.md](PUBLISHING.md)

## Documentation Maintenance

When making changes to the repository, update the relevant documentation:

- Code changes → Update [DEVELOPER_GUIDE.md](DEVELOPER_GUIDE.md)
- Dependency changes → Update [DEPENDENCY_MANAGEMENT.md](DEPENDENCY_MANAGEMENT.md)
- Installation changes → Update [main README](../README.md) and [QUICKSTART.md](QUICKSTART.md)
- License/citation changes → Update [PUBLISHING.md](PUBLISHING.md)
- Contribution process → Update [CONTRIBUTING.md](../CONTRIBUTING.md)
