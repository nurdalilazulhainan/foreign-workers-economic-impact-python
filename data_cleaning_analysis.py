import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Simulate data for foreign workers and economic indicators (2010-2020)
years = range(2010, 2021)
countries = ["Bangladesh", "Indonesia", "Myanmar", "Nepal"]

# Create the foreign workers dataset
foreign_workers = {
    "Year": np.tile(years, len(countries)),
    "Country": np.repeat(countries, len(years)),
    "Workers": np.random.randint(1000, 10000, size=len(years) * len(countries))
}

# Create the economic dataset
economic_data = {
    "Year": years,
    "GDP": np.random.randint(300, 600, len(years)),
    "Unemployment_Rate": np.random.randint(3, 10, len(years))
}

# Convert to DataFrames
workers_df = pd.DataFrame(foreign_workers)
economic_df = pd.DataFrame(economic_data)

# Merge datasets
final_data = pd.merge(workers_df, economic_df, on="Year")

# Save cleaned data to CSV
final_data.to_csv('final_data.csv', index=False)

# Plot foreign workers over the years (line plot)
plt.figure(figsize=(10,6))
sns.lineplot(data=final_data, x='Year', y='Workers', hue='Country', marker='o')
plt.title("Total Foreign Workers in Malaysia by Country (2010-2020)")
plt.xlabel("Year")
plt.ylabel("Number of Foreign Workers")
plt.savefig("foreign_workers_plot.png")

# Plot GDP vs. Unemployment rate (scatter plot)
plt.figure(figsize=(10,6))
sns.scatterplot(data=final_data, x='GDP', y='Unemployment_Rate', hue='Year', palette="viridis")
plt.title("GDP vs. Unemployment Rate in Malaysia (2010-2020)")
plt.xlabel("GDP (in Billions)")
plt.ylabel("Unemployment Rate (%)")
plt.savefig("gdp_unemployment_plot.png")
