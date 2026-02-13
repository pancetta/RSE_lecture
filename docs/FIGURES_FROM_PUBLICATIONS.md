# Using Figures from Cited Publications

## Overview

This document provides guidelines for incorporating figures from academic publications and documentation sources into the RSE course lectures, ensuring proper licensing compliance and attribution.

## General Principles

### License Verification
Before using any figure:
1. **Check the publication's license** (usually on publisher's website)
2. **Verify educational use is permitted**
3. **Note any attribution requirements**
4. **Document the license in this file**

### Attribution Requirements
For each figure used, provide:
- **Authors**: Original figure creators
- **Source**: Publication title, journal, year
- **DOI/URL**: Persistent identifier
- **License**: Type (e.g., CC BY 4.0)
- **Modifications**: Note if cropped, resized, or adapted

## Approved Sources

### 1. FAIR Principles (Lecture 11)

#### Wilkinson et al. (2016) - Original FAIR Principles
- **Publication**: "The FAIR Guiding Principles for scientific data management and stewardship"
- **Journal**: Scientific Data, Volume 3, Article 160018
- **DOI**: [10.1038/sdata.2016.18](https://doi.org/10.1038/sdata.2016.18)
- **License**: CC BY 4.0
- **Figures Available**:
  - Figure 1: The FAIR Guiding Principles diagram
  - Table 1: List of FAIR principles with descriptions

**Attribution Template**:
```markdown
![FAIR Principles](fair_principles_wilkinson2016.png)

**Figure**: The FAIR Guiding Principles.
**Source**: Wilkinson, M.D., Dumontier, M., Aalbersberg, I.J. et al. 
The FAIR Guiding Principles for scientific data management and stewardship. 
Sci Data 3, 160018 (2016). https://doi.org/10.1038/sdata.2016.18
**License**: CC BY 4.0
```

#### Barker et al. (2022) - FAIR4RS Principles
- **Publication**: "Introducing the FAIR Principles for research software"
- **Journal**: Scientific Data, Volume 9, Article 622
- **DOI**: [10.1038/s41597-022-01710-x](https://doi.org/10.1038/s41597-022-01710-x)
- **License**: CC BY 4.0
- **Figures Available**:
  - Figure 1: FAIR4RS principles overview
  - Figure 2: Comparison between FAIR data and FAIR4RS software principles

**Attribution Template**:
```markdown
![FAIR4RS Principles](fair4rs_barker2022.png)

**Figure**: FAIR principles for research software (FAIR4RS).
**Source**: Barker, M., Chue Hong, N.P., Katz, D.S. et al. 
Introducing the FAIR Principles for research software. 
Sci Data 9, 622 (2022). https://doi.org/10.1038/s41597-022-01710-x
**License**: CC BY 4.0
```

### 2. Workflow Management (Lecture 12)

#### Köster & Rahmann (2012) - Snakemake
- **Publication**: "Snakemake—a scalable bioinformatics workflow engine"
- **Journal**: Bioinformatics, Volume 28, Issue 19, Pages 2520–2522
- **DOI**: [10.1093/bioinformatics/bts480](https://doi.org/10.1093/bioinformatics/bts480)
- **License**: Oxford Academic allows figures for educational use with attribution
- **Figures Available**:
  - Figure 1: Example workflow DAG

**Note**: Oxford Academic journals typically allow educational use with proper citation.
Contact permissions team for confirmation if needed: https://academic.oup.com/journals/pages/access_purchase/rights_and_permissions

#### Di Tommaso et al. (2017) - Nextflow
- **Publication**: "Nextflow enables reproducible computational workflows"
- **Journal**: Nature Biotechnology, Volume 35, Pages 316–319
- **DOI**: [10.1038/nbt.3820](https://doi.org/10.1038/nbt.3820)
- **License**: Nature journals - check Springer Nature's RightsLink for educational permissions
- **Figures Available**:
  - Figure 1: Nextflow workflow example
  - Figure 2: Performance comparisons

**Note**: Nature journals often allow educational use but may require permission request.

### 3. Research Software Engineering Course Materials

#### Research Software Engineering with Python (py-rse)
- **Source**: https://third-bit.com/py-rse/
- **Repository**: https://github.com/merely-useful/py-rse
- **Authors**: Damien Irving, Kate Hertweck, Luke Johnston, Joel Ostblom, Charlotte Wickham, Greg Wilson
- **License**: CC BY 4.0
- **Figures Available**:
  - Figures from `/figures` directory in the repository
  - Workflow diagrams, project structure diagrams
  - Git branching diagrams
  - Testing pyramids
  - And many others throughout the book

**Attribution Template**:
```markdown
![Figure Description](figure_name.png)

**Figure**: [Caption from original book].
**Source**: Irving, D., Hertweck, K., Johnston, L., Ostblom, J., Wickham, C., & Wilson, G. (2022).
Research Software Engineering with Python. CRC Press.
https://third-bit.com/py-rse/
**License**: CC BY 4.0
```

**Note**: The online version is freely available, and all figures are in the GitHub repository under CC BY 4.0.

#### Alan Turing Institute RSE Course
- **Source**: https://alan-turing-institute.github.io/rse-course/html/
- **Repository**: https://github.com/alan-turing-institute/rse-course
- **Authors**: Turing Research Engineering Group and contributors
- **License**: CC BY 3.0 (Creative Commons Attribution)
- **Figures Available**:
  - Module-specific diagrams throughout course materials
  - Code examples and visualizations
  - Architecture diagrams

**Attribution Template**:
```markdown
![Figure Description](figure_name.png)

**Figure**: [Description].
**Source**: Alan Turing Institute Research Engineering Group. 
Research Software Engineering with Python.
https://alan-turing-institute.github.io/rse-course/html/
**License**: CC BY 3.0
```

**Note**: This is a derivative work of the UCL RSD course, also licensed under CC BY.

### 4. Documentation and Software Tools

#### GitHub Documentation
- **Source**: https://docs.github.com/
- **License**: CC BY 4.0 (GitHub's documentation)
- **Figures**: CI/CD pipeline diagrams, Git workflows, PR workflows
- **Location**: Lectures 1, 2, 6, 10

GitHub explicitly allows reuse of documentation content under CC BY 4.0.

#### Docker Documentation
- **Source**: https://docs.docker.com/
- **License**: Apache 2.0 (Docker documentation)
- **Figures**: Container architecture diagrams
- **Location**: Lecture 9

Docker documentation is Apache 2.0 licensed, which permits educational use.

## Implementation Checklist

When adding a figure from a publication:

- [ ] Verify the license permits educational use
- [ ] Download/obtain the figure in appropriate format (PNG, SVG preferred)
- [ ] Name file descriptively: `{topic}_{firstauthor}{year}.{ext}`
- [ ] Place in appropriate lecture directory
- [ ] Add attribution in lecture markdown cell immediately below figure
- [ ] Update this document with figure details
- [ ] Add entry to references.bib if not already present
- [ ] Test that figure displays correctly in converted notebook

## License Compliance Summary

### CC BY 4.0 (Most Permissive)
**Requires**:
- Attribution
- Link to license (https://creativecommons.org/licenses/by/4.0/)
- Indicate modifications

**Allows**:
- Commercial use
- Modifications
- Distribution

**Sources using CC BY 4.0**:
- Scientific Data articles (Wilkinson 2016, Barker 2022)
- GitHub Documentation
- Many open-access journals

### Educational Fair Use
Many academic publishers allow educational use even when not explicitly open access.
Always verify and document permission obtained.

## Contact Information

For questions about specific figures or permissions:
- Check publisher's permissions page
- Use RightsLink or similar services for automated permissions
- Contact course maintainers if unsure

## References

- Creative Commons: https://creativecommons.org/
- RightsLink (Springer Nature): https://www.nature.com/reprints-and-permissions
- Oxford Academic Permissions: https://academic.oup.com/journals/pages/access_purchase/rights_and_permissions
- GitHub Documentation License: https://docs.github.com/en/site-policy/github-terms/github-terms-of-service#5-license-grant-to-other-users

---

**Last Updated**: 2026-02-11
**Maintainer**: Course development team
