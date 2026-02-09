# Repository Overview

This repository contains lecture materials for a Research Software Engineering (RSE) course. The lectures are written in Python files using Jupytext format and can be converted to Jupyter notebooks for interactive learning.

# Project Structure

- **Lecture Files**: Located in `lecture_01/`, `lecture_02/`, `lecture_03/`, `lecture_04/` directories
- **Format**: Python files (`.py`) in Jupytext percent format that convert to Jupyter notebooks (`.ipynb`)
- **Documentation**: `README.md` contains comprehensive documentation
- **Build System**: `Makefile` contains all build, install, and deployment commands
- **CI/CD**: GitHub Actions workflows in `.github/workflows/`

# Critical Requirements

## 1. Lecture Duration - STRICTLY ENFORCED
**Each lecture MUST be exactly 90 minutes - not more, not less.**

When creating or modifying lectures:
- Plan content to fit within 90 minutes
- Include timing estimates in lecture sections
- Consider time for:
  - Introduction and overview (~5 minutes)
  - Main content presentation
  - Hands-on exercises
  - Q&A and wrap-up (~5 minutes)
- If a lecture exceeds 90 minutes, content must be removed or moved to another lecture
- If a lecture is under 90 minutes, add more exercises, examples, or depth

## 2. Always Run CI Pipeline locally Before Finishing
**Before marking any task as complete, ALWAYS run the CI pipeline.**

Required steps:
1. Make your changes
2. Commit your changes
3. Run the CI checks locally or wait for GitHub Actions:
   ```bash
   # Run linting
   flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
   flake8 . --count --statistics
   
   # Check Python syntax
   python -m py_compile convert_to_notebooks.py
   for lecture_file in lecture_*/lecture_*.py; do
     python -m py_compile "$lecture_file"
   done
   
   # Convert and test notebooks
   python convert_to_notebooks.py
   for notebook in lecture_*/*.ipynb; do
     jupyter nbconvert --to notebook --execute --inplace "$notebook"
   done
   ```
4. Make sure notebooks are executed without failure
5. Verify all checks pass
6. Only then mark the task as complete

## 3. Keep Makefile Up-to-Date
**The Makefile is a critical component - always keep it synchronized with any changes.**

When you:
- Add new dependencies → Update relevant install targets
- Add new build steps → Add new targets or update existing ones
- Change file structure → Update clean targets
- Add new lecture directories → Update conversion targets if needed

Always test Makefile changes:
```bash
make help  # Verify help text is current
make <target>  # Test the specific target you modified
```

## 4. Keep Documentation Up-to-Date
**Documentation must always reflect the current state of the repository.**

When you make changes, update:
- `README.md` - Main documentation file
  - Installation instructions
  - Usage examples
  - Project structure
  - Contributing guidelines
- Individual lecture docstrings and markdown cells
- Inline code comments (when they add value)

Documentation changes should be part of the same commit as code changes.

# Development Guidelines

## Working with Jupytext Files

- **Always edit** the `.py` files, never the `.ipynb` files directly
- Use Jupytext percent format (`# %%`) for cell markers
- Add markdown cells with `# %% [markdown]`
- Test conversion works: `python convert_to_notebooks.py`

## Code Quality Standards

- **Linting**: All code must pass flake8 checks
- **Style**: Follow PEP 8 conventions (enforced by `.flake8` config)
- **Syntax**: All Python files must have valid syntax
- **Execution**: All notebooks must execute without errors

## Testing Requirements

Before submitting changes:
1. Syntax check: `python -m py_compile <file>`
2. Lint check: `flake8 <file>`
3. Conversion test: `python convert_to_notebooks.py`
4. Execution test: `jupyter nbconvert --to notebook --execute --inplace <notebook>`

## Cross-Platform Compatibility

All code and scripts must work on:
- Linux (Ubuntu)
- macOS 15 (Sequoia) and later
- macOS 26 (Tahoe)
- Windows 10/11 (with Git Bash)

Test on multiple platforms or ensure code is platform-agnostic.

## Git Workflow

- Create feature branches for changes
- Write clear, descriptive commit messages
- Keep commits focused and atomic
- Pull request must pass all CI checks before merge

# Build and Development Commands

```bash
# Environment setup
make install                 # Create base environment
make install-lecture[1-4]   # Install specific lecture dependencies

# Development
make convert                 # Convert Python files to notebooks
make build-website          # Build static website
make serve-website          # Serve website locally (port 8000)

# Cleanup
make clean                  # Remove generated notebooks
make clean-website          # Remove website build artifacts
```

# CI/CD Pipeline

The repository uses GitHub Actions with workflows:
- **ci.yml**: Runs on every push and PR
  - Lints code with flake8
  - Checks Python syntax
  - Converts lectures to notebooks
  - Executes all notebooks to verify they run
  - Tests on multiple OS platforms

- **deploy.yml**: Deploys website to GitHub Pages

# Common Patterns

## Adding a New Lecture

1. Create new directory: `lecture_XX/`
2. Create lecture file: `lecture_XX/lecture_XX.py` in Jupytext format
3. Add metadata section at top (copy from existing lecture)
4. Structure content with clear sections
5. **Ensure content is exactly 90 minutes**
6. Update `README.md` with new lecture info
7. Test conversion: `python convert_to_notebooks.py`
8. Update `myst.yml` if using Jupyter Book
9. Run full CI pipeline

## Modifying Existing Lectures

1. Edit the `.py` file only
2. Test locally: syntax, lint, convert, execute
3. **Verify lecture duration remains 90 minutes**
4. Update related documentation if needed
5. Update `myst.yml` if using Jupyter Book
6. Run CI pipeline
7. Clean up generated files: `make clean`

## Adding Dependencies

1. Update `environment.yml` for base dependencies
2. Update specific lecture install targets in `Makefile` if needed
3. Update `README.md` prerequisites/installation sections
4. Test: `make install` and verify environment works
5. Update CI workflow if new tools are required

# Best Practices

1. **Keep it simple**: Lectures are for teaching, not showcasing advanced techniques
2. **Be explicit**: Clear, readable code is better than clever code
3. **Test thoroughly**: Every change should be tested on multiple platforms
4. **Document decisions**: Explain why, not just what
5. **Consistency**: Follow existing patterns in the codebase
6. **90-minute rule**: Never compromise on lecture duration - it's critical for course scheduling

# Questions?

- Check `README.md` for detailed documentation
- Review existing lectures for patterns and style
- Look at CI workflow files for testing requirements
- Open an issue for clarification on any point
