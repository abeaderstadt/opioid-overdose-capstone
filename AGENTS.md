# AGENTS.md

## Purpose

This repository contains the code, notebooks, and supporting files for the
**Opioid Overdose Capstone Project**.

The project analyzes opioid overdose mortality trends in the United States
using publicly available CDC WONDER data. Development is managed using
**uv** and **pyproject.toml** to provide a reproducible Python environment.

---

## Development Requirements

- Use **uv** for environment management and package installation.
- Do not recommend `pip install` as the primary workflow.
- Target Python **3.14**.
- Commands should work on Windows, macOS, and Linux.
- When shell-specific commands are necessary, provide both:
  - PowerShell (Windows)
  - bash/zsh (macOS/Linux)

---

## Quick Start

```shell
uv self update
uv python pin 3.14
uv sync --extra dev --upgrade
uvx pre-commit install
```

---

## Common Tasks

### Run preprocessing

```shell
uv run python src/data_processing/<script_name>.py
```

### Launch Jupyter

```shell
uv run jupyter lab
```

or

```shell
uv run jupyter notebook
```

### Format and lint

```shell
uv run ruff format .
uv run ruff check . --fix
```

### Static type checking

```shell
uv run pyright
```

---

## Repository Structure

- `data/raw/` – Original CDC WONDER datasets
- `data/processed/` – Cleaned datasets used for analysis
- `figures/` – Generated visualizations
- `notebooks/` – Exploratory analysis and predictive modeling
- `src/data_processing/` – Data cleaning and preparation scripts
- `src/analysis/` – Statistical analysis and modeling
- `src/visualization/` – Visualization scripts

---

## Notes

- Keep raw datasets unchanged.
- Generate processed datasets using the scripts in `src/data_processing`.
- Commit source code and notebooks, but avoid committing unnecessary generated files or virtual environments.
