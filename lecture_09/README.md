# Lecture 9: Containerization and Reproducibility

This lecture covers containerization technologies (Docker, Podman, Apptainer) for achieving true reproducibility in research software.

## Topics Covered

- Limitations of virtual environments
- Container fundamentals
- Docker for research software
- Podman (rootless alternative)
- Apptainer/Singularity (HPC-focused)
- Cross-language containerization
- Best practices

## Installation

This lecture uses only base dependencies. No additional packages required.

```bash
make install-lecture9
micromamba activate rse_lecture
```

## Converting to Notebook

```bash
python convert_to_notebooks.py
jupyter notebook lecture_09/lecture_09.ipynb
```
