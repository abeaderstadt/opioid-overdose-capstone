"""Merge opioid-related death datasets into a single table.

Terminal command to run this file from the root project folder:

    uv run python src/data_processing/01_build_opioid_master_dataset.py
"""

from pathlib import Path

import pandas as pd

RAW_DIR = Path("data/raw")
PROCESSED_DIR = Path("data/processed")


def clean_wonder_file(df: pd.DataFrame) -> pd.DataFrame:
    """Remove CDC WONDER notes rows and clean year."""
    df = df.dropna(subset=["state", "year"]).copy()
    df["year"] = df["year"].astype(int)

    for col in df.columns:
        if col.endswith("_deaths") or col.endswith("_death_rate"):
            df[col] = pd.to_numeric(df[col], errors="coerce")

    return df


def check_duplicates(name: str, df: pd.DataFrame) -> None:
    """Print duplicate state-year rows, if any."""
    dupes = df.duplicated(subset=["state", "year"]).sum()
    print(f"{name}: {dupes} duplicate state-year rows")


opioid = clean_wonder_file(pd.read_csv(RAW_DIR / "opioid_deaths.csv"))
heroin = clean_wonder_file(pd.read_csv(RAW_DIR / "heroin_deaths.csv"))
other_opioid = clean_wonder_file(pd.read_csv(RAW_DIR / "other_deaths.csv"))
methadone = clean_wonder_file(pd.read_csv(RAW_DIR / "methadone_deaths.csv"))
synthetic = clean_wonder_file(pd.read_csv(RAW_DIR / "synthetic_deaths.csv"))
prescription = clean_wonder_file(pd.read_csv(RAW_DIR / "prescription_deaths.csv"))

for name, data in {
    "opioid": opioid,
    "heroin": heroin,
    "other_opioid": other_opioid,
    "methadone": methadone,
    "synthetic": synthetic,
    "prescription": prescription,
}.items():
    check_duplicates(name, data)

df = opioid.merge(
    heroin[["state", "year", "heroin_deaths", "heroin_death_rate"]],
    on=["state", "year"],
    how="left",
)

df = df.merge(
    other_opioid[["state", "year", "other_deaths", "other_death_rate"]],
    on=["state", "year"],
    how="left",
)

df = df.merge(
    methadone[["state", "year", "methadone_deaths", "methadone_death_rate"]],
    on=["state", "year"],
    how="left",
)

df = df.merge(
    synthetic[["state", "year", "synthetic_deaths", "synthetic_death_rate"]],
    on=["state", "year"],
    how="left",
)

df = df.merge(
    prescription[["state", "year", "prescription_deaths", "prescription_death_rate"]],
    on=["state", "year"],
    how="left",
)

if "Notes" in df.columns:
    df = df.drop(columns=["Notes"])

PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

output_file = PROCESSED_DIR / "merged_opioid_deaths.csv"
df.to_csv(output_file, index=False)

print(f"\nMerged dataset saved to: {output_file}")
print(df.head())
print(df.shape)
