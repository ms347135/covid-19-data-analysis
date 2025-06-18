# COVID-19 Data Analysis Project

## Overview

This project provides a comprehensive analysis of a COVID-19 dataset, originally from Kaggle. The analysis is broken down into modular scripts that explore the data to uncover trends, geographical distributions, and correlations related to the pandemic. The scripts perform data cleaning, exploratory data analysis (EDA), and generate a wide range of visualizations.

## Features

This project is organized into five main analysis steps:

1.  **Geographical Analysis:** Identifies and visualizes the top 20 most affected countries (Confirmed Cases, Deaths, Recoveries).
2.  **Trend Analysis:** Plots daily and cumulative trends of cases globally and for the top 5 most affected countries.
3.  **Correlation Analysis:** Creates a heatmap and scatter plots to show the relationships between key metrics.
4.  **Calculated Metrics:** Analyzes and visualizes mortality rates, recovery rates, and active cases over time.
5.  **Advanced Visualizations:** Generates an interactive world map and a stacked area chart for a global overview.

## How to Run This Project

1.  **Clone the repository:**
    ```bash
    git clone <your-github-repo-url>
    cd covid-19-data-analysis
    ```

2.  **Create a virtual environment and install dependencies:**
    ```bash
    # For Windows
    python -m venv venv
    venv\Scripts\activate
    
    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    
    # Install required libraries
    pip install -r requirements.txt
    ```

3.  **Run the analysis scripts:**
    Run the Python scripts in order from your terminal or directly from your IDE (like PyCharm).

    ```bash
    python 1_geographical_analysis.py
    python 2_trend_analysis.py
    python 3_correlation_analysis.py
    python 4_calculated_metrics.py
    python 5_advanced_visualizations.py
    ```

4.  **Check the output:**
    All 13 generated charts and the interactive map will be saved in the `output/` directory.

## Dataset

The dataset used is `covid_19_clean_complete.csv`, which is included in the `data/` directory.