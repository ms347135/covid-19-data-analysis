import pandas as pd
import plotly.express as px
import os

# --- Configuration ---
DATA_FILE_PATH = os.path.join('data', 'covid_19_clean_complete.csv')
OUTPUT_DIR = 'output'
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

# --- Analysis ---
print("Running Step 3: Correlation Analysis (with 'by Country' scatter plot)...")
df = pd.read_csv(DATA_FILE_PATH)
df['Date'] = pd.to_datetime(df['Date'])

# --- Plot 1: Correlation Heatmap ---
df_daily_global = df.groupby('Date').sum().reset_index()
correlation_matrix = df_daily_global[['Confirmed', 'Deaths', 'Recovered']].corr()
fig_heatmap = px.imshow(correlation_matrix,
                        text_auto=True,
                        aspect="auto",
                        title='Correlation Matrix of Daily Global Totals',
                        color_continuous_scale='RdBu_r',
                        template='plotly_white')
fig_heatmap.write_html(os.path.join(OUTPUT_DIR, 'correlation_heatmap.html'))


# --- Plot 2: Scatter plot of Global Cumulative cases vs Deaths (by Day) ---
fig_global_scatter = px.scatter(df_daily_global,
                                x='Confirmed',
                                y='Deaths',
                                title='Cumulative Global Confirmed Cases vs. Deaths (by Day)',
                                template='plotly_white',
                                trendline='ols',
                                trendline_color_override='red')
fig_global_scatter.write_html(os.path.join(OUTPUT_DIR, 'global_confirmed_vs_deaths_scatter.html'))


# --- NEW, MORE INTUITIVE PLOT: Total Cases vs Deaths (by Country) ---
latest_df = df.sort_values('Date').groupby('Country/Region').last().reset_index()
# Filter out countries with very few cases for a cleaner plot
latest_df_filtered = latest_df[latest_df['Confirmed'] > 100]

fig_country_scatter = px.scatter(latest_df_filtered,
                                 x='Confirmed',
                                 y='Deaths',
                                 title='Total Confirmed Cases vs. Total Deaths (by Country)',
                                 hover_name='Country/Region',  # Hover to see country name
                                 size='Confirmed',             # Bubble size based on confirmed cases
                                 color='WHO Region',           # Color by WHO region
                                 template='plotly_white',
                                 log_x=True,                   # Use a log scale for better visualization
                                 log_y=True,
                                 labels={'Confirmed': 'Total Confirmed Cases (Log Scale)',
                                         'Deaths': 'Total Deaths (Log Scale)'})
fig_country_scatter.write_html(os.path.join(OUTPUT_DIR, 'country_confirmed_vs_deaths_scatter.html'))


print("Correlation analysis complete. 3 interactive HTML files saved to 'output' folder.")