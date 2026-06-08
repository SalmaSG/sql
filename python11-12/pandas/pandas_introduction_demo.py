"""Pandas introduction demo.

This demo shows the basics of pandas using a class-based example.
It covers Series, DataFrame creation, selection, filtering, grouping,
aggregation, and CSV I/O.
"""

import os

try:
    import pandas as pd
except ImportError:
    raise ImportError(
        "pandas is required to run this demo. Install it with: pip install pandas"
    )


class PandasIntroductionDemo:
    """A simple pandas introduction class with multiple demo methods."""

    def __init__(self):
        self.data = {
            "name": ["Alice", "Bob", "Charlie", "Diana", "Evan"],
            "age": [25, 30, 35, 28, 22],
            "city": ["New York", "London", "Paris", "Tokyo", "Berlin"],
            "score": [88.5, 92.0, 79.5, 85.0, 90.0],
        }
        self.df = pd.DataFrame(self.data)

    def show_series(self):
        print("=== Series Demo ===")
        series = pd.Series([10, 20, 30, 40], index=["a", "b", "c", "d"])
        print(series)
        print("Type:", type(series))
        print("Index:", series.index.tolist())
        print("Values:", series.values.tolist())
        print()

    def show_dataframe(self):
        print("=== DataFrame Demo ===")
        print(self.df)
        print("Type:", type(self.df))
        print("Columns:", self.df.columns.tolist())
        print("Shape:", self.df.shape)
        print()

    def selection_and_filtering(self):
        print("=== Selection and Filtering ===")
        print("First two rows:")
        print(self.df.head(2))
        print()

        print("Select only the 'name' and 'score' columns:")
        print(self.df[["name", "score"]])
        print()

        print("Filter rows where age is greater than 25:")
        filtered = self.df[self.df["age"] > 25]
        print(filtered)
        print()

    def group_and_aggregate(self):
        print("=== Grouping and Aggregation ===")
        self.df["age_group"] = pd.cut(
            self.df["age"], bins=[0, 25, 30, 40], labels=["Young", "Adult", "Senior"]
        )
        grouped = self.df.groupby("age_group")["score"].mean()
        print("Average score by age group:")
        print(grouped)
        print()

    def sort_values(self):
        print("=== Sorting ===")
        sorted_df = self.df.sort_values(by="score", ascending=False)
        print(sorted_df)
        print()

    def csv_io_demo(self):
        print("=== CSV Read / Write Demo ===")
        filename = "pandas_demo_data.csv"
        self.df.to_csv(filename, index=False)
        print(f"Saved DataFrame to {filename}")
        read_back = pd.read_csv(filename)
        print("Read from CSV:")
        print(read_back)
        print()

        if os.path.exists(filename):
            os.remove(filename)
            print(f"Removed temporary file {filename}")
            print()

    def run_all(self):
        self.show_series()
        self.show_dataframe()
        self.selection_and_filtering()
        self.group_and_aggregate()
        self.sort_values()
        self.csv_io_demo()


def main():
    demo = PandasIntroductionDemo()
    demo.run_all()


if __name__ == "__main__":
    main()
