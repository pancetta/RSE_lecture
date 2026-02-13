# Summary: Using Figures from Licensed Publications

## What We Accomplished

This PR demonstrates how to effectively use high-quality figures from cited publications and open educational resources in the RSE course, with proper licensing and attribution.

## Two-Part Solution

### Part 1: Comprehensive Documentation (commits 6c21cea)

Created three detailed guides:

1. **`FIGURES_FROM_PUBLICATIONS.md`** - Main reference
   - License verification process
   - Approved sources with attribution templates
   - Legal compliance requirements
   - Contact information for permissions

2. **`EXAMPLE_ADDING_FIGURE.md`** - Practical tutorial
   - Complete step-by-step walkthrough
   - Real example using FAIR principles figure
   - Troubleshooting common issues
   - Implementation checklist

3. **`RECOMMENDED_FIGURES.md`** - Strategic roadmap
   - Lecture-by-lecture recommendations
   - Priority list (Top 5 highest-impact figures)
   - Where to find each figure
   - License compatibility matrix

### Part 2: Actual Implementation (commit 4a3630b)

Added real figures to lectures:

**Lecture 11: FAIR Principles**
- Embedded official figure from Wilkinson et al. (2016)
- Source: Scientific Data (Nature), CC BY 4.0
- Shows complete FAIR principles hierarchy
- Full academic attribution with DOI

**Lecture 1: Git Workflow**
- Visual diagram of Git's three-stage process
- Based on py-rse book content (CC BY 4.0)
- Clear ASCII visualization
- Practical workflow examples

## Key Verified Sources

All sources checked and approved for educational use:

### 1. Research Software Engineering with Python (py-rse)
- **License**: CC BY 4.0
- **Authors**: Irving, Hertweck, Johnston, Ostblom, Wickham, Wilson
- **URL**: https://third-bit.com/py-rse/
- **Available Figures**: Git workflows, testing pyramids, documentation hierarchy, Make DAGs
- **Already Cited**: ✅ Yes (references.bib entry: wilson2022py_rse)

### 2. Alan Turing Institute RSE Course
- **License**: CC BY 3.0
- **Authors**: Turing Research Engineering Group
- **URL**: https://alan-turing-institute.github.io/rse-course/html/
- **Available Figures**: Module diagrams, code visualizations, architecture examples
- **Already Cited**: ✅ Yes (references.bib entry: turing_rse_course)

### 3. FAIR Principles Papers
- **Wilkinson et al. (2016)**: CC BY 4.0 - DOI: 10.1038/sdata.2016.18
- **Barker et al. (2022)**: CC BY 4.0 - DOI: 10.1038/s41597-022-01710-x
- **Publisher**: Scientific Data (Nature Publishing Group)
- **Already Cited**: ✅ Yes (both in references.bib)

### 4. Official Documentation
- **GitHub Docs**: CC BY 4.0 - https://docs.github.com/
- **Docker Docs**: Apache 2.0 - https://docs.docker.com/
- **Already Cited**: ✅ Yes (both in references.bib)

## Benefits of This Approach

### Academic Benefits
- ✅ **Peer-reviewed content** from authoritative sources
- ✅ **Proper attribution** teaches students citation practices
- ✅ **Academic credibility** through published research figures
- ✅ **Current with field** using latest scholarly work

### Practical Benefits
- ✅ **No rendering issues** (professionally designed)
- ✅ **High quality** (publication-grade figures)
- ✅ **Legally compliant** (all licenses verified)
- ✅ **Zero maintenance** for embedded figures (source maintains them)
- ✅ **Quick to implement** (just add markdown with attribution)

### Educational Benefits
- ✅ **Demonstrates best practices** for using others' work
- ✅ **Models proper attribution** for students
- ✅ **Connects to broader literature** via DOIs and citations
- ✅ **Supports open science** by using and citing open resources

## How to Use These Materials

### For Course Maintainers

To add more figures:

1. **Choose a lecture** that would benefit from visualization
2. **Check `RECOMMENDED_FIGURES.md`** for specific suggestions
3. **Follow `EXAMPLE_ADDING_FIGURE.md`** for step-by-step process
4. **Verify license** in `FIGURES_FROM_PUBLICATIONS.md`
5. **Add with full attribution** using provided templates

### For Contributors

The documentation makes it easy to:
- Find appropriate figures for each lecture
- Understand licensing requirements
- Implement with proper attribution
- Avoid legal/copyright issues

### For Instructors

Use the figures to:
- Enhance lecture presentations
- Reference authoritative sources
- Teach citation practices
- Connect to broader RSE community

## Next Steps - Highest Priority Additions

Based on `RECOMMENDED_FIGURES.md`, the top priority figures to add next:

1. **Testing Pyramid** (Lecture 5)
   - Source: py-rse Chapter 10
   - Shows test types hierarchy
   - Very high pedagogical value

2. **Container vs VM Architecture** (Lecture 9)
   - Source: Docker documentation
   - Clarifies key architectural concepts
   - Frequently confusing topic for students

3. **Git Merge Strategies** (Lecture 2)
   - Source: py-rse Chapter 7 or GitHub docs
   - Visualizes fast-forward vs three-way merge
   - Complements existing Git coverage

4. **Workflow DAG Example** (Lecture 12)
   - Source: Snakemake documentation
   - Shows dependency graph concept
   - Makes abstract workflows concrete

5. **Documentation Hierarchy** (Lecture 8)
   - Source: py-rse documentation chapter
   - Shows different doc types and audiences
   - Guides doc strategy decisions

## Files Changed

### Documentation Added
- `docs/FIGURES_FROM_PUBLICATIONS.md` (6,047 chars)
- `docs/EXAMPLE_ADDING_FIGURE.md` (5,052 chars)
- `docs/RECOMMENDED_FIGURES.md` (6,650 chars)

### Lectures Enhanced
- `lecture_01/lecture_01.py` - Added Git workflow visualization
- `lecture_11/lecture_11.py` - Added FAIR principles figure

### Configuration Updated
- `README.md` - Added documentation links and license note

**Total Impact**: ~18KB of documentation + 2 enhanced lectures

## Conclusion

This PR provides:
1. **Complete framework** for using licensed figures
2. **Practical examples** of implementation
3. **Clear roadmap** for future additions
4. **Legal compliance** through verified licenses
5. **Academic credibility** through proper attribution

The approach is **sustainable**, **legally sound**, and **pedagogically effective**.

---

**For questions or to add more figures**, see the detailed documentation in the `docs/` directory.
