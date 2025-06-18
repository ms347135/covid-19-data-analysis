import pandas as pd
import plotly.express as px
import os

# --- Configuration ---
DATA_FILE_PATH = os.path.join('data', 'covid_19_clean_complete.csv')
OUTPUT_DIR = 'output'
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

# --- Analysis ---
print("Running Step 1: Geographical Analysis (Interactive)...")

df = pd.read_csv(DATA_FILE_PATH)
df['Date'] = pd.to_datetime(df['Date'])
latest_df = df.sort_values('Date').groupby('Country/Region').last().reset_index()

# Top 20 Confirmed
top_20_confirmed = latest_df.sort_values(by='Confirmed', ascending=False).head(20)
fig = px.bar(top_20_confirmed,
             x='Confirmed',
             y='Country/Region',
             orientation='h',
             title='Top 20 Countries with Highest Confirmed Cases',
             template='plotly_white',
             color='Confirmed',
             color_continuous_scale=px.colors.sequential.Viridis)
fig.update_layout(yaxis={'categoryorder':'total ascending'})
fig.write_html(os.path.join(OUTPUT_DIR, 'top_20_confirmed.html'))

# Top 20 Deaths
top_20_deaths = latest_df.sort_values(by='Deaths', ascending=False).head(20)
fig = px.bar(top_20_deaths,
             x='Deaths',
             y='Country/Region',
             orientation='h',
             title='Top 20 Countries with Highest Deaths',
             template='plotly_white',
             color='Deaths',
             color_continuous_scale=px.colors.sequential.Reds)
fig.update_layout(yaxis={'categoryorder':'total ascending'})
fig.write_html(os.path.join(OUTPUT_DIR, 'top_20_deaths.html'))

# Top 20 Recovered
top_20_recovered = latest_df.sort_values(by='Recovered', ascending=False).head(20)
fig = px.bar(top_20_recovered,
             x='Recovered',
             y='Country/Region',
             orientation='h',
             title='Top 20 Countries with Highest Recovered Cases',
             template='plotly_white',
             color='Recovered',
             color_continuous_scale=px.colors.sequential.Greens)
fig.update_layout(yaxis={'categoryorder':'total ascending'})
fig.write_html(os.path.join(OUTPUT_DIR, 'top_20_recovered.html'))

print("Geographical analysis complete. 3 interactive HTML files saved to 'output' folder.")