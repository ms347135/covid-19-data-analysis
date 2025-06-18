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
print("Running Step 4: Calculated Metrics Analysis...")
df = pd.read_csv(DATA_FILE_PATH)
df['Date'] = pd.to_datetime(df['Date'])
latest_df = df.sort_values('Date').groupby('Country/Region').last().reset_index()

# Rates Calculation
latest_df['Mortality Rate'] = (latest_df['Deaths'] / latest_df['Confirmed']) * 100
latest_df['Recovery Rate'] = (latest_df['Recovered'] / latest_df['Confirmed']) * 100
latest_df.fillna(0, inplace=True)

# Top 10 Mortality Rate
top_10_mortality = latest_df[latest_df['Confirmed'] > 1000].sort_values(by='Mortality Rate', ascending=False).head(10)
plt.figure(figsize=(12, 8))
sns.barplot(x='Mortality Rate', y='Country/Region', data=top_10_mortality, palette='Reds_r')
plt.title('Top 10 Countries with Highest Mortality Rate (Confirmed > 1000)')
plt.savefig(os.path.join(OUTPUT_DIR, 'top_10_mortality_rate.png'))
plt.close()

# Top 10 Recovery Rate
top_10_recovery = latest_df[latest_df['Confirmed'] > 1000].sort_values(by='Recovery Rate', ascending=False).head(10)
plt.figure(figsize=(12, 8))
sns.barplot(x='Recovery Rate', y='Country/Region', data=top_10_recovery, palette='Greens_r')
plt.title('Top 10 Countries with Highest Recovery Rate (Confirmed > 1000)')
plt.savefig(os.path.join(OUTPUT_DIR, 'top_10_recovery_rate.png'))
plt.close()

# Active Cases Trend
global_trends = df.groupby('Date').sum()
plt.figure(figsize=(15, 8))
plt.plot(global_trends.index, global_trends['Active'], label='Active Cases', color='orange')
plt.title('Global Active COVID-19 Cases Over Time')
plt.grid(True)
plt.savefig(os.path.join(OUTPUT_DIR, 'global_active_cases_trend.png'))
plt.close()

# Active cases for Top 5 countries
top_5_countries = latest_df.sort_values(by='Confirmed', ascending=False).head(5)['Country/Region'].tolist()
top_5_df = df[df['Country/Region'].isin(top_5_countries)]
plt.figure(figsize=(15, 8))
sns.lineplot(x='Date', y='Active', hue='Country/Region', data=top_5_df)
plt.title('Active Cases in Top 5 Countries')
plt.grid(True)
plt.savefig(os.path.join(OUTPUT_DIR, 'top5_active_cases_trends.png'))
plt.close()

print("Calculated metrics analysis complete. 4 plots saved to 'output' folder.")