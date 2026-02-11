# Publishing and Citing the RSE Course

This guide explains how to formally publish the course materials and obtain a citable DOI.

## Overview

The RSE Course uses a dual licensing approach:
- **Educational content** (lectures, documentation): CC BY 4.0 (Attribution required)
- **Code examples**: MIT License

This ensures that:
1. Attribution is mandatory when using course materials
2. The course can be formally cited in academic contexts
3. The materials remain open and accessible

## Citation

### Using CITATION.cff

This repository includes a `CITATION.cff` file that provides machine-readable citation metadata. GitHub automatically displays a "Cite this repository" button that uses this file.

To cite the course:

**BibTeX format:**
```bibtex
@misc{speck2026rse,
  author       = {Speck, Robert},
  title        = {Research Software Engineering Lectures (JuRSE)},
  year         = {2026},
  publisher    = {GitHub},
  url          = {https://github.com/pancetta/RSE_course_JuRSE},
  note         = {Version 1.0.0}
}
```

**Text format:**
> Speck, Robert. (2026). Research Software Engineering Lectures (JuRSE). https://github.com/pancetta/RSE_course_JuRSE

## Obtaining a DOI with Zenodo

For a persistent, citable reference with a DOI, we recommend using Zenodo:

### Step 1: Link GitHub Repository to Zenodo

1. Go to [Zenodo](https://zenodo.org/) and sign in with your GitHub account
2. Navigate to your [GitHub settings on Zenodo](https://zenodo.org/account/settings/github/)
3. Find `pancetta/RSE_course_JuRSE` in the repository list
4. Toggle the switch to enable Zenodo integration

### Step 2: Create a Release

1. In the GitHub repository, go to "Releases"
2. Click "Create a new release"
3. Tag the release (e.g., `v1.0.0`)
4. Write release notes describing the course content
5. Publish the release

### Step 3: Zenodo Automatic Archive

Once you create a release:
- Zenodo automatically archives the release
- A DOI is assigned (e.g., `10.5281/zenodo.1234567`)
- The DOI badge can be added to the README

### Step 4: Update Repository with DOI

After getting the DOI, update:

1. **README.md** - Add DOI badge:
   ```markdown
   [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1234567.svg)](https://doi.org/10.5281/zenodo.1234567)
   ```

2. **CITATION.cff** - Add DOI field:
   ```yaml
   doi: 10.5281/zenodo.1234567
   ```

3. **Citation examples** - Include DOI in citations:
   ```bibtex
   @misc{speck2026rse,
     author       = {Speck, Robert},
     title        = {Research Software Engineering Lectures (JuRSE)},
     year         = {2026},
     publisher    = {Zenodo},
     doi          = {10.5281/zenodo.1234567},
     url          = {https://doi.org/10.5281/zenodo.1234567}
   }
   ```

## Benefits of Zenodo Integration

### For Authors
- **Persistent identifier**: DOIs never change, even if GitHub URLs change
- **Long-term preservation**: Content archived independently of GitHub
- **Academic recognition**: DOIs are recognized in academic contexts
- **Version tracking**: Each release gets its own DOI
- **Metrics**: Track citations and downloads

### For Users
- **Reliable citation**: Can cite specific versions with confidence
- **Accessibility**: Content remains accessible even if repository moves
- **Academic compliance**: DOIs satisfy citation requirements for grants/papers
- **Version clarity**: Can cite the exact version used in research

## Zenodo Metadata

This repository includes a `.zenodo.json` file that provides metadata for Zenodo:
- Title and description
- Authors and affiliations
- ORCID identifiers
- Keywords
- License information
- Related identifiers

This ensures consistent metadata across all releases.

## License Information for Citation

When citing this work, note that:
- The course content is licensed under **CC BY 4.0** (Attribution required)
- Code examples are licensed under **MIT License**
- Both licenses allow reuse with proper attribution

Always include attribution when using or adapting this material.

## Example Citations in Different Contexts

### In a Paper
> This research training program was based on materials from the RSE Course (Speck, 2026), adapted for our institutional context.

### In Course Materials
> These lectures are adapted from "Research Software Engineering Lectures (JuRSE)" by Robert Speck (https://github.com/pancetta/RSE_course_JuRSE), licensed under CC BY 4.0.

### In a Repository README
```markdown
## Acknowledgements
This project was developed using best practices learned from the 
[RSE Course](https://github.com/pancetta/RSE_course_JuRSE) by Robert Speck.
```

## Versioning Strategy

We recommend:
- **Major versions** (v1.0.0 → v2.0.0): Significant restructuring or major content changes
- **Minor versions** (v1.0.0 → v1.1.0): New lectures or substantial updates
- **Patch versions** (v1.0.0 → v1.0.1): Bug fixes, typos, minor improvements

Each version gets its own DOI through Zenodo, allowing users to cite the specific version they used.

## Additional Resources

- [CITATION.cff specification](https://citation-file-format.github.io/)
- [Zenodo documentation](https://help.zenodo.org/)
- [GitHub-Zenodo integration guide](https://docs.github.com/en/repositories/archiving-a-github-repository/referencing-and-citing-content)
- [Creative Commons BY 4.0 License](https://creativecommons.org/licenses/by/4.0/)
