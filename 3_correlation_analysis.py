import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# --- Configuration ---
DATA_FILE_PATH = os.path.join('data', 'covid_19_clean_complete.csv')
OUTPUT_DIR = 'output'
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

# --- Analysis ---
print("Running Step 3: Correlation Analysis...")
df = pd.read_csv(DATA_FILE_PATH)

# Heatmap
correlation_matrix = df[['Confirmed', 'Deaths', 'Recovered']].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix of Confirmed, Deaths, and Recovered Cases')
plt.savefig(os.path.join(OUTPUT_DIR, 'correlation_heatmap.png'))
plt.close()

# Scatter Plots
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Confirmed', y='Deaths', data=df)
plt.title('Confirmed Cases vs. Deaths')
plt.grid(True)
plt.savefig(os.path.join(OUTPUT_DIR, 'confirmed_vs_deaths_scatter.png'))
plt.close()

plt.figure(figsize=(10, 6))
sns.scatterplot(x='Confirmed', y='Recovered', data=df)
plt.title('Confirmed Cases vs. Recovered Cases')
plt.grid(True)
plt.savefig(os.path.join(OUTPUT_DIR, 'confirmed_vs_recovered_scatter.png'))
plt.close()

print("Correlation analysis complete. 3 plots saved to 'output' folder.")