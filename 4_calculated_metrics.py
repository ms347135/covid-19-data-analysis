import pandas as pd
import plotly.express as px
import os

# --- Configuration ---
DATA_FILE_PATH = os.path.join('data', 'covid_19_clean_complete.csv')
OUTPUT_DIR = 'output'
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

# --- Analysis ---
print("Running Step 4: Calculated Metrics Analysis (Full Version)...")
df = pd.read_csv(DATA_FILE_PATH)
df['Date'] = pd.to_datetime(df['Date'])
latest_df = df.sort_values('Date').groupby('Country/Region').last().reset_index()

# Rates Calculation
latest_df['Mortality Rate'] = (latest_df['Deaths'] / latest_df['Confirmed']) * 100
latest_df['Recovery Rate'] = (latest_df['Recovered'] / latest_df['Confirmed']) * 100
latest_df.fillna(0, inplace=True)

# Top 10 Mortality Rate
top_10_mortality = latest_df[latest_df['Confirmed'] > 1000].sort_values(by='Mortality Rate', ascending=False).head(10)
fig = px.bar(top_10_mortality, x='Mortality Rate', y='Country/Region',
             title='Top 10 Countries by Mortality Rate (Confirmed > 1000)',
             template='plotly_white', orientation='h', color='Mortality Rate',
             color_continuous_scale=px.colors.sequential.OrRd)
fig.update_layout(yaxis={'categoryorder':'total ascending'})
fig.write_html(os.path.join(OUTPUT_DIR, 'top_10_mortality_rate.html'))

# Top 10 Recovery Rate
top_10_recovery = latest_df[latest_df['Confirmed'] > 1000].sort_values(by='Recovery Rate', ascending=False).head(10)
fig = px.bar(top_10_recovery, x='Recovery Rate', y='Country/Region',
             title='Top 10 Countries by Recovery Rate (Confirmed > 1000)',
             template='plotly_white', orientation='h', color='Recovery Rate',
             color_continuous_scale=px.colors.sequential.Greens)
fig.update_layout(yaxis={'categoryorder':'total ascending'})
fig.write_html(os.path.join(OUTPUT_DIR, 'top_10_recovery_rate.html'))


# Global Active Cases Trend
global_trends = df.groupby('Date').sum().reset_index()
fig = px.line(global_trends, x='Date', y='Active',
              title='Global Active COVID-19 Cases Over Time', template='plotly_white')
fig.update_traces(line_color='orange')
fig.write_html(os.path.join(OUTPUT_DIR, 'global_active_cases_trend.html'))

# Active cases for Top 5 countries
top_5_countries = latest_df.sort_values(by='Confirmed', ascending=False).head(5)['Country/Region'].tolist()
top_5_df = df[df['Country/Region'].isin(top_5_countries)]
fig = px.line(top_5_df, x='Date', y='Active', color='Country/Region',
              title='Active Cases in Top 5 Countries', template='plotly_white')
fig.write_html(os.path.join(OUTPUT_DIR, 'top5_active_cases_trends.html'))


print("Calculated metrics analysis complete. All 4 interactive HTML files saved to 'output' folder.")