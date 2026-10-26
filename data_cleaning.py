"""
Video Game Sales Data Cleaning Script
CSMODEL Group 5 Major Course Output (MCO)

This script cleans and preprocesses the Video Game Sales and Ratings dataset
by handling missing values, converting data types, and producing a sanitized
dataset ready for statistical modeling and exploratory data analysis.
"""

import os
import pandas as pd
import numpy as np


def load_dataset(filepath: str = "Video_Game_Sales.csv") -> pd.DataFrame:
    """Load the raw video game sales dataset."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Dataset not found at {filepath}")
    return pd.read_csv(filepath)


def inspect_dataset(df: pd.DataFrame) -> None:
    """Print key exploration summaries and null value counts."""
    print("=" * 60)
    print("DATASET OVERVIEW")
    print("=" * 60)
    print(f"Total Records: {df.shape[0]:,}")
    print(f"Total Columns: {df.shape[1]}")
    print(f"Unique Platforms: {df['Platform'].nunique()}")
    print(f"Unique Publishers: {df['Publisher'].nunique()}")
    print("\nTop 5 Publishers by Game Count:")
    print(df['Publisher'].value_counts().head(5))

    print("\nMissing Values per Feature:")
    null_counts = df.isnull().sum()
    print(null_counts[null_counts > 0])


def clean_dataset(df: pd.DataFrame, critical_features=None) -> pd.DataFrame:
    """
    Clean the dataset by dropping rows with missing values in key statistical features
    and casting data types appropriately.
    """
    if critical_features is None:
        critical_features = [
            'Year_of_Release',
            'Publisher',
            'Critic_Score',
            'Critic_Count',
            'User_Score',
            'User_Count',
            'Rating'
        ]

    df_cleaned = df.copy()

    # Drop rows where any of the critical variables are missing
    df_cleaned = df_cleaned.dropna(subset=critical_features).reset_index(drop=True)

    # Cast Year_of_Release to integer
    df_cleaned['Year_of_Release'] = df_cleaned['Year_of_Release'].astype(int)

    # Ensure User_Score and Critic_Score are numerical
    df_cleaned['User_Score'] = pd.to_numeric(df_cleaned['User_Score'], errors='coerce')
    df_cleaned['Critic_Score'] = pd.to_numeric(df_cleaned['Critic_Score'], errors='coerce')

    return df_cleaned


def main():
    raw_path = "Video_Game_Sales.csv"
    output_path = "Video_Game_Sales_Cleaned.csv"

    print("Loading raw video game sales dataset...")
    raw_df = load_dataset(raw_path)
    inspect_dataset(raw_df)

    print("\n" + "=" * 60)
    print("CLEANING DATASET")
    print("=" * 60)
    cleaned_df = clean_dataset(raw_df)

    print(f"Rows before cleaning: {len(raw_df):,}")
    print(f"Rows after cleaning:  {len(cleaned_df):,}")
    print(f"Retained data percentage: {(len(cleaned_df) / len(raw_df)) * 100:.2f}%")

    print("\nCleaned Dataset Column Info:")
    print(cleaned_df.info())

    print("\nRemaining Missing Values:")
    print(cleaned_df.isnull().sum())

    cleaned_df.to_csv(output_path, index=False)
    print(f"\nCleaned dataset successfully exported to '{output_path}'")


if __name__ == "__main__":
    main()
