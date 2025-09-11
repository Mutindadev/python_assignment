import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv("sales_data.csv")

# 1. Calculate total revenue
total_revenue = df["Revenue (ksh)"].sum()

# 2. Find best-selling product
best_selling = df.groupby("Product")["Quantity Sold"].sum().idxmax()
best_selling_qty = df.groupby("Product")["Quantity Sold"].sum().max()

# 3. Find highest sales day (by revenue)
highest_sales_day = df.groupby("Date")["Revenue (ksh)"].sum().idxmax()
highest_sales_value = df.groupby("Date")["Revenue (ksh)"].sum().max()

# 4. Save results to sales_summary.txt
with open("sales_summary.txt", "w") as f:
    f.write(f"Total Revenue: ksh{total_revenue:,}\n")
    f.write(f"Best-Selling Product: {best_selling} ({best_selling_qty} units sold)\n")
    f.write(f"Highest Sales Day: {highest_sales_day} (ksh{highest_sales_value:,})\n")

# Print results in a friendly format
print("📊 Sales Analysis Results:")
print(f"Total Revenue: ksh{total_revenue:,}")
print(f"Best-Selling Product: {best_selling} ({best_selling_qty} units sold)")
print(f"Highest Sales Day: {highest_sales_day} (ksh{highest_sales_value:,})")

# 🎯 Bonus: Visualization (Revenue by Date)
df.groupby("Date")["Revenue (ksh)"].sum().plot(kind="bar", color="skyblue", figsize=(7,5))
plt.title("Revenue by Date")
plt.xlabel("Date")
plt.ylabel("Revenue (ksh)")
plt.tight_layout()
plt.savefig("sales_trends.png")  # Save chart as image
plt.show()
