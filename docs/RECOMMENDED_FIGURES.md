# Recommended Figures from Cited Sources

This document maps specific figures from our cited sources (py-rse and Turing RSE course) to lectures where they would be most valuable.

## Lecture-by-Lecture Recommendations

### Lecture 1: Introduction to Git

**From py-rse (CC BY 4.0):**
- Figure from Chapter 6 (Git Cmdline): Git workflow diagram showing working directory, staging area, repository
- Figure showing local vs remote repositories
- Git commit history timeline

**From Turing RSE Course (CC BY 3.0):**
- Module 4 Git diagrams: Basic Git workflow
- Branching and merging visualizations

**URLs to check:**
- https://third-bit.com/py-rse/git-cmdline.html
- https://alan-turing-institute.github.io/rse-course/html/module04_version_control_with_git/

### Lecture 2: Advanced Git & Collaboration

**From py-rse:**
- Chapter 7 (Git Advanced): Merge conflict diagrams
- Pull request workflow illustrations
- Fork and pull request model

**From Turing RSE Course:**
- Module 4 advanced topics: Merge strategies
- Collaboration workflows

**URLs to check:**
- https://third-bit.com/py-rse/git-advanced.html
- https://alan-turing-institute.github.io/rse-course/html/module04_version_control_with_git/04_04_git_advanced.html

### Lecture 5: Testing Research Software

**From py-rse:**
- Chapter 10 (Testing): Testing pyramid
- Test coverage visualization
- Unit vs integration vs system test scope

**From Turing RSE Course:**
- Module 5: Test examples and patterns

**URLs to check:**
- https://third-bit.com/py-rse/testing.html
- https://alan-turing-institute.github.io/rse-course/html/module05_testing_your_code/

### Lecture 6: CI/CD

**From py-rse:**
- Chapter 11 (CI): Continuous integration workflow
- Automated testing pipeline

**From GitHub Docs (CC BY 4.0):**
- GitHub Actions workflow diagrams
- CI pipeline visualization

**URLs to check:**
- https://docs.github.com/en/actions
- https://third-bit.com/py-rse/ (check for CI chapter)

### Lecture 8: Documentation

**From py-rse:**
- Chapter 12 (Documentation): Documentation hierarchy/pyramid
- Sphinx documentation build flow
- README structure

**From Turing RSE Course:**
- Module 6 Software Projects: Documentation examples

**URLs to check:**
- https://third-bit.com/py-rse/
- https://alan-turing-institute.github.io/rse-course/html/module06_software_projects/

### Lecture 9: Containerization

**From Docker Docs (Apache 2.0):**
- Container vs VM architecture diagram
- Docker layer visualization
- Container lifecycle

**URLs to check:**
- https://docs.docker.com/get-started/overview/
- Official Docker documentation diagrams

### Lecture 11: FAIR Principles & Research Data

**From Scientific Papers (CC BY 4.0):**
- Wilkinson et al. (2016): FAIR principles figure
- Barker et al. (2022): FAIR4RS principles

**From py-rse:**
- Chapter on research data: Data organization
- File format comparison tables

**URLs to check:**
- https://www.nature.com/articles/sdata201618 (Open access)
- https://www.nature.com/articles/s41597-022-01710-x (Open access)
- https://third-bit.com/py-rse/

### Lecture 12: Workflows

**From Academic Papers:**
- Köster & Rahmann (2012): Snakemake DAG examples
- Di Tommaso et al. (2017): Nextflow workflow diagrams

**From py-rse:**
- Chapter 9 (Automation): Make workflow graphs
- Dependency graphs

**From Snakemake Docs:**
- Workflow DAG visualizations
- Rule dependency examples

**URLs to check:**
- https://third-bit.com/py-rse/automate.html
- https://snakemake.readthedocs.io/

## Priority List (Highest Impact)

### Top 5 Figures to Add First:

1. **FAIR Principles Diagram** (Lecture 11)
   - Source: Wilkinson et al. (2016) or Barker et al. (2022)
   - License: CC BY 4.0 (Scientific Data)
   - Impact: Core concept, peer-reviewed, authoritative

2. **Git Workflow Diagram** (Lecture 1)
   - Source: py-rse Chapter 6 or Turing Course Module 4
   - License: CC BY 4.0 or CC BY 3.0
   - Impact: Fundamental concept students struggle with

3. **Testing Pyramid** (Lecture 5)
   - Source: py-rse Chapter 10
   - License: CC BY 4.0
   - Impact: Clear visualization of testing strategy

4. **Container vs VM Architecture** (Lecture 9)
   - Source: Docker documentation
   - License: Apache 2.0
   - Impact: Clarifies key architectural difference

5. **Workflow DAG Example** (Lecture 12)
   - Source: Snakemake documentation or paper figures
   - License: Various (check specific source)
   - Impact: Makes abstract workflow concept concrete

## How to Find Figures

### py-rse Repository
```bash
git clone https://github.com/merely-useful/py-rse.git
cd py-rse/figures
ls *.png *.svg
```

All figures are in the `/figures` directory with descriptive names.

### Turing RSE Course
Browse the course materials at:
- https://alan-turing-institute.github.io/rse-course/html/

Or clone repository:
```bash
git clone https://github.com/alan-turing-institute/rse-course.git
```

Look for images in module directories.

### Scientific Papers (Open Access)

For papers published in Scientific Data:
1. Visit the DOI link
2. Scroll to figures section
3. Click "Download figure" or right-click to save
4. High-resolution versions usually available

## Implementation Workflow

For each figure you want to add:

1. **Verify License**
   - Check source license
   - Confirm educational use permitted
   - Note any specific attribution requirements

2. **Download/Obtain Figure**
   - Get highest quality available
   - Save with descriptive name: `{topic}_{source}{year}.{ext}`
   - Example: `fair_principles_wilkinson2016.png`

3. **Add Attribution**
   - Include full citation
   - Link to original source
   - State license clearly
   - Note any modifications

4. **Document**
   - Update `FIGURES_FROM_PUBLICATIONS.md`
   - Add reference to `references.bib` if needed

5. **Test**
   - Convert lecture to notebook
   - Verify figure displays correctly
   - Check all links work

## License Summary

✅ **Safe to Use with Proper Attribution:**
- CC BY 4.0 (py-rse, Scientific Data journals, GitHub Docs)
- CC BY 3.0 (Turing RSE Course)
- Apache 2.0 (Docker Docs)
- MIT (with attribution)

⚠️ **Check Specific Terms:**
- Academic papers from non-open journals
- Nature, Springer, Elsevier papers (may need permission even for educational use)

## Questions?

If unsure about any figure's licensing:
1. Check the publisher's copyright page
2. Look for explicit license statement
3. Use RightsLink or similar permission systems
4. When in doubt, err on side of caution

---

**Next Steps:**
1. Start with the Top 5 priority figures
2. Focus on CC BY licensed sources (easiest)
3. Add attribution as you go
4. Document everything in FIGURES_FROM_PUBLICATIONS.md
