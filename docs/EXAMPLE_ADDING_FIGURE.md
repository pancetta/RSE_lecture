# Example: Adding FAIR Principles Figure to Lecture 11

This document shows exactly how to add a figure from a cited publication to a lecture, with proper attribution and licensing compliance.

## Step-by-Step Example

### 1. Identify the Source

**Publication**: Wilkinson et al. (2016)  
**Title**: "The FAIR Guiding Principles for scientific data management and stewardship"  
**Journal**: Scientific Data, Volume 3, Article 160018  
**DOI**: https://doi.org/10.1038/sdata.2016.18  
**License**: CC BY 4.0 (all Scientific Data articles are open access)  

### 2. Verify License Allows Educational Use

✅ CC BY 4.0 permits:
- Sharing and redistribution
- Commercial and non-commercial use
- Modifications
- Educational use

**Requirements**:
- Provide attribution
- Link to license
- Indicate if changes were made

### 3. Obtain the Figure

Navigate to the publication: https://www.nature.com/articles/sdata201618

Download options:
- Right-click on Figure 1 → Save image
- Or use "Download figures" link on the page
- Save as: `fair_principles_wilkinson2016.png`

### 4. Add to Lecture Directory

```bash
# Place in lecture_11 directory
mv fair_principles_wilkinson2016.png lecture_11/
```

### 5. Add to Lecture with Proper Attribution

In `lecture_11/lecture_11.py`, add a markdown cell with the figure and attribution:

```python
# %% [markdown]
# ## The FAIR Principles
#
# The FAIR principles provide guidelines for making research data and software Findable, 
# Accessible, Interoperable, and Reusable.
#
# ![FAIR Principles](fair_principles_wilkinson2016.png)
#
# **Figure**: The FAIR Guiding Principles.  
# **Source**: Wilkinson, M.D., Dumontier, M., Aalbersberg, I.J. et al. (2016). 
# The FAIR Guiding Principles for scientific data management and stewardship. 
# *Scientific Data* 3, 160018.  
# **DOI**: [10.1038/sdata.2016.18](https://doi.org/10.1038/sdata.2016.18)  
# **License**: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
#
# The FAIR principles consist of:
#
# ### Findable
# - F1. (Meta)data are assigned a globally unique and persistent identifier
# - F2. Data are described with rich metadata
# - F3. Metadata clearly and explicitly include the identifier of the data they describe
# - F4. (Meta)data are registered or indexed in a searchable resource
#
# [rest of lecture content...]
```

### 6. Update Documentation

Add entry to `docs/FIGURES_FROM_PUBLICATIONS.md`:

```markdown
## Lecture 11 - FAIR Principles

### fair_principles_wilkinson2016.png
- **Source**: Wilkinson et al. (2016), Scientific Data
- **DOI**: 10.1038/sdata.2016.18
- **License**: CC BY 4.0
- **Added**: 2026-02-11
- **Attribution**: Included in lecture markdown cell
```

### 7. Verify Display

Convert and test:

```bash
python scripts/convert_to_notebooks.py
jupyter notebook lecture_11/lecture_11.ipynb
```

Check that:
- ✅ Figure displays correctly
- ✅ Attribution is visible below figure
- ✅ All links work
- ✅ License information is clear

## Full Markdown Cell Template

Copy and adapt this template for any CC BY 4.0 licensed figure:

```markdown
# %% [markdown]
# ![Figure Description](filename.png)
#
# **Figure**: [Descriptive caption from original paper].  
# **Source**: [Author list]. ([Year]). [Title]. *[Journal]* [Volume], [Article number].  
# **DOI**: [DOI link](https://doi.org/...)  
# **License**: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
```

## Best Practices

1. **Keep original filename convention**: `{topic}_{firstauthor}{year}.{ext}`
2. **Always cite in-text**: Mention the figure when discussing the concept
3. **Maintain figure quality**: Download highest resolution available
4. **Check accessibility**: Ensure alt text is descriptive
5. **Document modifications**: If you crop or resize, note it in attribution

## Common Issues and Solutions

### Issue: Figure is too large
**Solution**: Resize maintaining aspect ratio, note in attribution:
```markdown
(Figure resized to 800px width for display; original available at DOI link)
```

### Issue: Figure contains multiple panels
**Solution**: Either use full figure or extract relevant panel, noting:
```markdown
(Panel A from Figure 1 shown above; see original for complete figure)
```

### Issue: Unsure about license
**Solution**: 
1. Check publisher's website
2. Look for license statement in paper
3. For Scientific Data: always CC BY 4.0
4. For other Nature journals: check specific article
5. When in doubt, contact publisher

## Checklist

Before committing a figure from a publication:

- [ ] Verified license permits educational use
- [ ] Downloaded high-quality version
- [ ] Named file appropriately
- [ ] Added to correct lecture directory
- [ ] Included full attribution in lecture
- [ ] Linked to DOI and license
- [ ] Documented in FIGURES_FROM_PUBLICATIONS.md
- [ ] Tested display in converted notebook
- [ ] Added reference to references.bib (if not already present)

---

**Remember**: Proper attribution is not just legally required—it's academically ethical and helps students learn about citing sources correctly.
