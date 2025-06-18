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
print("Running Step 1: Geographical Analysis...")

df = pd.read_csv(DATA_FILE_PATH)
df['Date'] = pd.to_datetime(df['Date'])
latest_df = df.sort_values('Date').groupby('Country/Region').last().reset_index()

# Top 20 Confirmed
top_20_confirmed = latest_df.sort_values(by='Confirmed', ascending=False).head(20)
plt.figure(figsize=(12, 8))
sns.barplot(x='Confirmed', y='Country/Region', data=top_20_confirmed, palette='viridis')
plt.title('Top 20 Countries with Highest Confirmed Cases')
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, 'top_20_confirmed.png'))
plt.close()

# Top 20 Deaths
top_20_deaths = latest_df.sort_values(by='Deaths', ascending=False).head(20)
plt.figure(figsize=(12, 8))
sns.barplot(x='Deaths', y='Country/Region', data=top_20_deaths, palette='Reds_r')
plt.title('Top 20 Countries with Highest Deaths')
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, 'top_20_deaths.png'))
plt.close()

# Top 20 Recovered
top_20_recovered = latest_df.sort_values(by='Recovered', ascending=False).head(20)
plt.figure(figsize=(12, 8))
sns.barplot(x='Recovered', y='Country/Region', data=top_20_recovered, palette='Greens_r')
plt.title('Top 20 Countries with Highest Recovered Cases')
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, 'top_20_recovered.png'))
plt.close()

print("Geographical analysis complete. 3 plots saved to 'output' folder.")