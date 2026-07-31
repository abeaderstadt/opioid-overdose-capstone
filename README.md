# Understanding the Opioid Crisis
## An Analysis of U.S. Opioid Overdose Trends Using CDC WONDER Data

![Python](https://img.shields.io/badge/Python-3.14-blue)
![Status](https://img.shields.io/badge/Status-Complete-success)
![License](https://img.shields.io/badge/License-MIT-green)

---

## Project Overview

The opioid epidemic continues to be one of the most significant public health challenges in the United States. This project analyzes national opioid overdose mortality trends using publicly available data from the CDC WONDER Multiple Cause of Death database.

The goal of this project is to identify geographic and demographic patterns in opioid overdose deaths, examine how different opioid categories have changed over time, and evaluate whether historical trends can be used to predict future overdose death rates using machine learning models.

This project was completed as the capstone project for the Master of Science in Data Analytics program at Northwest Missouri State University.

---

## Objectives

- Analyze national opioid overdose trends from **1999–2020**
- Examine differences across U.S. states
- Explore demographic trends by:
  - Age
  - Sex
  - Race/Ethnicity
- Compare overdose trends across opioid categories:
  - Heroin
  - Prescription opioids
  - Methadone
  - Synthetic opioids
  - Other narcotics
- Build predictive models to estimate opioid overdose death rates

---

## Data Source

**CDC WONDER Multiple Cause of Death Database**

Years Included:

- 1999–2020

Primary datasets include:

- Opioid overdose deaths by state and year
- Opioid deaths by age
- Opioid deaths by sex
- Opioid deaths by race/ethnicity

Additional drug-specific datasets:

- Heroin
- Prescription opioids
- Methadone
- Synthetic opioids
- Other narcotics

---

## Project Workflow

```text
CDC WONDER
        │
        ▼
Data Cleaning & Validation
        │
        ▼
Merge Drug-Specific Datasets
        │
        ▼
Exploratory Data Analysis
        │
        ▼
Visualization
        │
        ▼
Predictive Modeling
        │
        ▼
Interpretation & Conclusions
```

---

# Repository Structure

```text
opioid-overdose-capstone/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── figures/
│
├── notebooks/
│   ├── eda.ipynb
│   └── predictive_modeling.ipynb
│
├── reports/
│
├── src/
│   └── data_processing/
│
├── README.md
├── pyproject.toml
└── uv.lock
```

The preprocessing pipeline is implemented as reusable Python scripts in src/data_processing/. Exploratory data analysis, visualization, and predictive modeling were performed in Jupyter notebooks to support an interactive analytical workflow.

---

# Exploratory Data Analysis

## National Opioid Death Rate

The national opioid overdose death rate increased dramatically between 1999 and 2020, with especially rapid growth occurring after 2013.

<p align="center">
<img src="figures/national_opioid_death_rate.png" width="800">
</p>

---

## Geographic Distribution

States in Appalachia, the Ohio Valley, and portions of the Northeast experienced the highest opioid overdose death rates in 2020.

<p align="center">
<img src="figures/opioid_death_rates_by_state_2020.pdf" width="800">
</p>

---

## Drug Category Trends

Different opioid categories followed distinct patterns over time. Synthetic opioids showed the most dramatic increase during the final years of the study period.

<p align="center">
<img src="figures/opioid_deaths_by_drug_type.png" width="800">
</p>

---

## Demographic Trends

The project also examined overdose mortality by age, sex, and race/ethnicity to identify populations experiencing the greatest increases over time.

<p align="center">
<img src="figures/opioid_death_rates_age_year_heatmap.png" width="800">
</p>

---

# Predictive Modeling

Three regression models were evaluated for predicting opioid overdose death rates.

| Model | Purpose |
|--------|----------|
| Linear Regression | Baseline predictive model |
| Random Forest | Ensemble tree model |
| Gradient Boosting | Boosted decision tree model |

Model performance was compared using:

- MAE
- RMSE
- R²

Linear Regression produced the strongest overall performance on this dataset.

---

# Technologies Used

- Python
- Pandas
- NumPy
- Plotly
- Matplotlib
- Scikit-learn
- Jupyter Notebook
- CDC WONDER

---

# Reproducing the Project

Clone the repository

```bash
git clone https://github.com/abeaderstadt/opioid-overdose-capstone.git
```

Create the environment

```bash
uv sync
```

Launch Jupyter

```bash
uv run jupyter lab
```

---

# Key Findings

- Opioid overdose mortality increased substantially between 1999 and 2020.
- Synthetic opioids became the dominant driver of overdose deaths during the later years of the study period.
- Geographic differences revealed particularly high mortality rates in several eastern states.
- Clear demographic differences were observed across age, sex, and race/ethnicity.
- Linear Regression provided the best predictive performance among the evaluated models.

---

# Future Work

Potential future improvements include:

- Incorporating socioeconomic indicators
- Adding county-level analyses
- Forecasting future overdose mortality beyond 2020
- Exploring additional machine learning models
- Building an interactive dashboard

---

# Author

**Alissa Beaderstadt**

M.S. Data Analytics
Northwest Missouri State University

GitHub:

https://github.com/abeaderstadt

---

## License

This project is provided for educational and research purposes.
