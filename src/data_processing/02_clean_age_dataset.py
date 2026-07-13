"""Clean and process the age dataset.

Terminal command to run this file from the root project folder:

    uv run python src/data_processing/02_clean_age_dataset.py
"""

from pathlib import Path

import pandas as pd

RAW_DIR = Path("data/raw")
PROCESSED_DIR = Path("data/processed")


def clean_wonder_file(df: pd.DataFrame) -> pd.DataFrame:
    """Remove CDC WONDER notes rows and standardize data types."""
    # Remove CDC notes at the bottom of the file
    df = df.dropna(subset=["state", "year"]).copy()

    # Standardize column names
    df.columns = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("/", "_")
    )

    # Convert numeric columns
    numeric_columns = [
        "state_code",
        "year",
        "year_code",
        "age",
        "deaths",
        "population",
        "opioid_deaths",
        "opioid_death_rate",
    ]

    for col in numeric_columns:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    # Remove Notes column if present
    if "notes" in df.columns:
        df = df.drop(columns=["notes"])

    return df


# Read raw dataset
df = pd.read_csv(RAW_DIR / "age.csv")

# Clean dataset
df = clean_wonder_file(df)

# Create processed directory if needed
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

# Save cleaned dataset
output_file = PROCESSED_DIR / "age_processed.csv"
df.to_csv(output_file, index=False)

print(f"Saved cleaned dataset to: {output_file}")
print(df.head())
print(df.shape)
