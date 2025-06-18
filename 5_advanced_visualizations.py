import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import os

# --- Configuration ---
DATA_FILE_PATH = os.path.join('data', 'covid_19_clean_complete.csv')
OUTPUT_DIR = 'output'
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

# --- Analysis ---
print("Running Step 5: Advanced Visualizations...")
df = pd.read_csv(DATA_FILE_PATH)
df['Date'] = pd.to_datetime(df['Date'])

# World Map
latest_df = df.sort_values('Date').groupby('Country/Region').last().reset_index()
fig = px.choropleth(latest_df,
                    locations="Country/Region",
                    locationmode='country names',
                    color="Confirmed",
                    hover_name="Country/Region",
                    color_continuous_scale=px.colors.sequential.Plasma,
                    title='Total Confirmed COVID-19 Cases by Country')
fig.write_html(os.path.join(OUTPUT_DIR, "world_map_confirmed_cases.html"))

# Stacked Area Chart
global_trends = df.groupby('Date')[['Confirmed', 'Deaths', 'Recovered']].sum().reset_index()
plt.figure(figsize=(15, 8))
plt.stackplot(global_trends['Date'],
              global_trends['Deaths'],
              global_trends['Recovered'],
              global_trends['Confirmed'] - global_trends['Deaths'] - global_trends['Recovered'],
              labels=['Deaths', 'Recovered', 'Active'],
              colors=['#d62728', '#2ca02c', '#ff7f0e'])
plt.title('Global COVID-19 Cases: Active vs. Recovered vs. Deaths')
plt.xlabel('Date')
plt.ylabel('Number of Cases')
plt.legend(loc='upper left')
plt.grid(True)
plt.savefig(os.path.join(OUTPUT_DIR, 'global_stacked_area_chart.png'))
plt.close()

print("Advanced visualizations complete. 2 files saved to 'output' folder.")