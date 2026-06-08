"""
Simple Data Analysis Application

This app uses:
- NumPy for numerical calculations
- Pandas for storing and analyzing table data
- Matplotlib for creating charts
"""

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def create_sales_data():
    """Create sample sales data for a small shop."""
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
    products = ["Laptop", "Mobile", "Headphones", "Keyboard"]

    np.random.seed(7)
    sales = np.random.randint(20, 100, size=(len(months), len(products)))

    return pd.DataFrame(sales, index=months, columns=products)


def print_summary(data):
    """Print useful summaries in the terminal."""
    monthly_total = data.sum(axis=1)
    product_total = data.sum(axis=0)
    best_product = product_total.idxmax()
    best_month = monthly_total.idxmax()
    average_sales = np.mean(data.values)

    print("Sales Data")
    print(data)
    print()
    print("Monthly Total Sales")
    print(monthly_total)
    print()
    print("Product Total Sales")
    print(product_total)
    print()
    print(f"Best selling product: {best_product}")
    print(f"Best sales month: {best_month}")
    print(f"Average sales value: {average_sales:.2f}")


def create_charts(data):
    """Create and save charts from the sales data."""
    monthly_total = data.sum(axis=1)
    product_total = data.sum(axis=0)

    plt.figure(figsize=(10, 5))
    plt.plot(monthly_total.index, monthly_total.values, marker="o", color="green")
    plt.title("Monthly Total Sales")
    plt.xlabel("Month")
    plt.ylabel("Sales")
    plt.grid(True)
    plt.savefig("monthly_sales.png")
    plt.close()

    plt.figure(figsize=(10, 5))
    plt.bar(product_total.index, product_total.values, color=["blue", "orange", "purple", "red"])
    plt.title("Product Total Sales")
    plt.xlabel("Product")
    plt.ylabel("Sales")
    plt.savefig("product_sales.png")
    plt.close()

    plt.figure(figsize=(10, 5))
    plt.imshow(data, cmap="viridis")
    plt.title("Sales Heatmap")
    plt.xlabel("Product")
    plt.ylabel("Month")
    plt.xticks(range(len(data.columns)), data.columns)
    plt.yticks(range(len(data.index)), data.index)
    plt.colorbar(label="Sales")
    plt.savefig("sales_heatmap.png")
    plt.close()


def main():
    sales_data = create_sales_data()
    print_summary(sales_data)
    create_charts(sales_data)

    print()
    print("Charts saved:")
    print("- monthly_sales.png")
    print("- product_sales.png")
    print("- sales_heatmap.png")


if __name__ == "__main__":
    main()

