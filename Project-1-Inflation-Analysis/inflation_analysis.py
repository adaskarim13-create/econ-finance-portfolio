import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("Project-1-Inflation-Analysis/data/inflation_data.csv")

print("=" * 60)
print("ECONOMICS & FINANCE PORTFOLIO")
print("Project 1: The Cost of Living Crisis")
print("=" * 60)

print("\nInflation Data")
print(df)

# Statistics
average = df["Inflation"].mean()

highest = df.loc[df["Inflation"].idxmax()]
lowest = df.loc[df["Inflation"].idxmin()]

print("\nSummary Statistics")
print("-" * 30)
print(f"Average Inflation: {average:.2f}%")
print(f"Highest Inflation: {highest['Inflation']}% ({int(highest['Year'])})")
print(f"Lowest Inflation: {lowest['Inflation']}% ({int(lowest['Year'])})")

# Graph
plt.figure(figsize=(8,5))

plt.plot(
    df["Year"],
    df["Inflation"],
    marker="o",
    linewidth=2
)

plt.title("U.S. Inflation Rate (2020–2025)")
plt.xlabel("Year")
plt.ylabel("Inflation Rate (%)")

plt.grid(True)

plt.savefig("Project-1-Inflation-Analysis/inflation_graph.png")

plt.show()
