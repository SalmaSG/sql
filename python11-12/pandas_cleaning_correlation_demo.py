"""Pandas cleaning and correlation demo.

This demo shows how to clean tabular data with pandas and how to compute
correlation statistics for numeric features.
"""

import os

try:
    import pandas as pd
    import numpy as np
except ImportError:
    raise ImportError(
        "pandas and numpy are required to run this demo. Install them with: pip install pandas numpy"
    )


class PandasCleaningCorrelationDemo:
    """A pandas demo covering data cleaning and correlation analysis."""

    def __init__(self):
        self.raw_data = {
            "customer_id": [101, 102, 103, 104, 105, 106, 107, 107],
            "age": [25, 38, np.nan, 45, 29, 34, 34, 34],
            "annual_income": [52000, 64000, 58000, 72000, np.nan, 61000, 61000, 61000],
            "purchase_count": [5, 8, 7, 12, 6, 9, 9, 9],
            "average_order_value": [120.5, 150.0, 135.0, np.nan, 98.0, 130.0, 130.0, 130.0],
            "region": ["North", "South", "East", "West", "North", "East", "East", "East"],
        }
        self.df = pd.DataFrame(self.raw_data)

    def show_raw_data(self):
        print("=== Raw Data ===")
        print(self.df)
        print("\nData types:\n", self.df.dtypes)
        print("\nMissing values:\n", self.df.isna().sum())
        print()

    def clean_missing_values(self):
        print("=== Cleaning Missing Values ===")
        # Fill missing numeric values using the median of each column.
        numeric_columns = ["age", "annual_income", "average_order_value"]
        medians = self.df[numeric_columns].median()
        cleaned_df = self.df.copy()
        cleaned_df[numeric_columns] = cleaned_df[numeric_columns].fillna(medians)

        print("Median values used for fill:")
        print(medians)
        print()
        print(cleaned_df)
        self.df = cleaned_df
        print()

    def drop_duplicate_rows(self):
        print("=== Dropping Duplicate Rows ===")
        before = len(self.df)
        self.df = self.df.drop_duplicates()
        after = len(self.df)
        print(f"Rows before: {before}, rows after: {after}")
        print(self.df)
        print()

    def convert_data_types(self):
        print("=== Converting Data Types ===")
        self.df["customer_id"] = self.df["customer_id"].astype(int)
        self.df["purchase_count"] = self.df["purchase_count"].astype(int)
        print(self.df.dtypes)
        print()

    def remove_outliers(self):
        print("=== Removing Outliers ===")
        # Use interquartile range to filter out extreme values.
        numeric = self.df[["age", "annual_income", "purchase_count", "average_order_value"]]
        q1 = numeric.quantile(0.25)
        q3 = numeric.quantile(0.75)
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr

        print("IQR lower bounds:\n", lower_bound)
        print("IQR upper bounds:\n", upper_bound)
        print()

        filtered = self.df[
            (numeric >= lower_bound) & (numeric <= upper_bound)
        ].dropna()

        print(f"Rows before filtering: {len(self.df)}")
        print(f"Rows after filtering: {len(filtered)}")
        print(filtered)
        self.df = filtered
        print()

    def correlation_analysis(self):
        print("=== Correlation Analysis ===")
        numeric_df = self.df.select_dtypes(include=[np.number])
        correlation_matrix = numeric_df.corr()
        print("Numeric feature correlation matrix:")
        print(correlation_matrix)
        print()

        if "purchase_count" in numeric_df.columns and "average_order_value" in numeric_df.columns:
            corr_val = numeric_df["purchase_count"].corr(numeric_df["average_order_value"])
            print(
                f"Correlation between purchase_count and average_order_value: {corr_val:.3f}"
            )
        print()

    def save_cleaned_csv(self):
        print("=== Save Cleaned Data ===")
        filename = "pandas_cleaned_correlation_data.csv"
        self.df.to_csv(filename, index=False)
        print(f"Saved cleaned dataset to {filename}")
        if os.path.exists(filename):
            print(f"File size: {os.path.getsize(filename)} bytes")
        print()

    def run_all(self):
        self.show_raw_data()
        self.clean_missing_values()
        self.drop_duplicate_rows()
        self.convert_data_types()
        self.remove_outliers()
        self.correlation_analysis()
        self.save_cleaned_csv()


def main():
    demo = PandasCleaningCorrelationDemo()
    demo.run_all()


if __name__ == "__main__":
    main()
