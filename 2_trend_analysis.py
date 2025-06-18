import pandas as pd
import plotly.express as px
import os

# --- Configuration ---
DATA_FILE_PATH = os.path.join('data', 'covid_19_clean_complete.csv')
OUTPUT_DIR = 'output'
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

# --- Analysis ---
print("Running Step 2: Trend Analysis (Full Version)...")

df = pd.read_csv(DATA_FILE_PATH)
df['Date'] = pd.to_datetime(df['Date'])
global_trends = df.groupby('Date')[['Confirmed', 'Deaths', 'Recovered']].sum().reset_index()
latest_df = df.sort_values('Date').groupby('Country/Region').last().reset_index()

# Daily Global Trends
fig = px.bar(global_trends,
             x='Date',
             y=['Confirmed', 'Deaths', 'Recovered'],
             title='Daily Global COVID-19 Cases',
             template='plotly_white',
             labels={'value': 'Number of Cases', 'variable': 'Metric'})
fig.write_html(os.path.join(OUTPUT_DIR, 'daily_global_trends.html'))

# Cumulative Global Trends
fig = px.line(global_trends,
              x='Date',
              y=['Confirmed', 'Deaths', 'Recovered'],
              title='Cumulative Global COVID-19 Cases',
              template='plotly_white',
              labels={'value': 'Number of Cases', 'variable': 'Metric'})
fig.write_html(os.path.join(OUTPUT_DIR, 'cumulative_global_trends.html'))

# Country-Specific Trends for Top 5
top_5_countries = latest_df.sort_values(by='Confirmed', ascending=False).head(5)['Country/Region'].tolist()
top_5_df = df[df['Country/Region'].isin(top_5_countries)]
top_5_grouped = top_5_df.groupby(['Date', 'Country/Region']).sum().reset_index()

fig = px.line(top_5_grouped, x='Date', y='Confirmed', color='Country/Region',
              title='Cumulative Confirmed Cases in Top 5 Countries', template='plotly_white')
fig.write_html(os.path.join(OUTPUT_DIR, 'top5_confirmed_trends.html'))

fig = px.line(top_5_grouped, x='Date', y='Deaths', color='Country/Region',
              title='Cumulative Deaths in Top 5 Countries', template='plotly_white')
fig.write_html(os.path.join(OUTPUT_DIR, 'top5_deaths_trends.html'))

fig = px.line(top_5_grouped, x='Date', y='Recovered', color='Country/Region',
              title='Cumulative Recovered Cases in Top 5 Countries', template='plotly_white')
fig.write_html(os.path.join(OUTPUT_DIR, 'top5_recovered_trends.html'))

print("Trend analysis complete. All 5 interactive HTML files saved to 'output' folder.")