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
print("Running Step 2: Trend Analysis...")

df = pd.read_csv(DATA_FILE_PATH)
df['Date'] = pd.to_datetime(df['Date'])
global_trends = df.groupby('Date').sum()
latest_df = df.sort_values('Date').groupby('Country/Region').last().reset_index()

# Daily Global Trends
plt.figure(figsize=(15, 8))
plt.plot(global_trends.index, global_trends['Confirmed'], label='Confirmed', color='blue')
plt.plot(global_trends.index, global_trends['Deaths'], label='Deaths', color='red')
plt.plot(global_trends.index, global_trends['Recovered'], label='Recovered', color='green')
plt.title('Daily Global COVID-19 Cases')
plt.xlabel('Date')
plt.ylabel('Number of Cases')
plt.legend()
plt.grid(True)
plt.savefig(os.path.join(OUTPUT_DIR, 'daily_global_trends.png'))
plt.close()

# Cumulative Global Trends
plt.figure(figsize=(15, 8))
plt.plot(global_trends.index, global_trends['Confirmed'].cumsum(), label='Confirmed', color='blue')
plt.plot(global_trends.index, global_trends['Deaths'].cumsum(), label='Deaths', color='red')
plt.plot(global_trends.index, global_trends['Recovered'].cumsum(), label='Recovered', color='green')
plt.title('Cumulative Global COVID-19 Cases')
plt.xlabel('Date')
plt.ylabel('Number of Cases')
plt.legend()
plt.grid(True)
plt.savefig(os.path.join(OUTPUT_DIR, 'cumulative_global_trends.png'))
plt.close()

# Country-Specific Trends
top_5_countries = latest_df.sort_values(by='Confirmed', ascending=False).head(5)['Country/Region'].tolist()
top_5_df = df[df['Country/Region'].isin(top_5_countries)]

plt.figure(figsize=(15, 8))
sns.lineplot(x='Date', y='Confirmed', hue='Country/Region', data=top_5_df)
plt.title('Cumulative Confirmed Cases in Top 5 Countries')
plt.grid(True)
plt.savefig(os.path.join(OUTPUT_DIR, 'top5_confirmed_trends.png'))
plt.close()

plt.figure(figsize=(15, 8))
sns.lineplot(x='Date', y='Deaths', hue='Country/Region', data=top_5_df)
plt.title('Cumulative Deaths in Top 5 Countries')
plt.grid(True)
plt.savefig(os.path.join(OUTPUT_DIR, 'top5_deaths_trends.png'))
plt.close()

plt.figure(figsize=(15, 8))
sns.lineplot(x='Date', y='Recovered', hue='Country/Region', data=top_5_df)
plt.title('Cumulative Recovered Cases in Top 5 Countries')
plt.grid(True)
plt.savefig(os.path.join(OUTPUT_DIR, 'top5_recovered_trends.png'))
plt.close()

print("Trend analysis complete. 5 plots saved to 'output' folder.")