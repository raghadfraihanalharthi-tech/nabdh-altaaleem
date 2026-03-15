Nabdh Al-Taaleem

Mapping the Female Technical Talent Pipeline in Saudi Arabia

Nabdh Al-Taaleem is a data visualization and analytics project that examines the relationship between technical education, skills development, and employment opportunities for women in Saudi Arabia.

The project explores a central question:

How aligned is the output of technical education with the actual demand of the labor market?

Using real government datasets, the platform analyzes the pipeline from education to employment and highlights the gap between female technical graduates and sector demand, particularly in energy and technology industries.

This project aims to transform fragmented public datasets into a clear and accessible analytical dashboard that helps reveal trends in female workforce participation and supports discussions around workforce development aligned with national transformation goals.

The Problem

In many economies, education systems produce graduates faster than labor markets can absorb them.

Understanding whether this imbalance exists within technical education for women in Saudi Arabia is important for evaluating workforce readiness and policy direction.

Key questions explored in this project include

How many women graduate from technical programs each year
Which industries show the strongest demand for technical talent
Where gaps exist between available skills and sector demand
How female workforce participation has evolved over time

By analyzing these questions together, the project attempts to visualize the full pipeline from education to employment.

Project Goals

The project was designed with three primary objectives

First, to map the relationship between technical education output and employment demand in key sectors.

Second, to explore trends in female workforce participation and identify areas of growth or mismatch.

Third, to present these insights through an interactive visualization platform that makes complex data easier to understand.

Rather than presenting isolated statistics, the dashboard connects multiple datasets to tell a cohesive data story about education and labor market alignment.

Data Sources

The analysis uses publicly available government datasets related to education, workforce participation, and sector employment.

Primary sources include

Saudi government open data platforms
Technical and Vocational Training Corporation datasets
Labor market and workforce participation statistics
Public economic and workforce indicators related to Vision 2030

All datasets were cleaned, structured, and integrated to support comparative analysis between education output and labor market demand.

Methodology

The project follows a simple but structured data science workflow.

Data Collection
Public datasets related to technical education and workforce participation were gathered from official government sources.

Data Cleaning
Raw data was standardized, missing values were addressed, and datasets were prepared for analysis.

Data Transformation
Indicators were created to compare graduate output with employment demand across sectors.

Exploratory Data Analysis
Initial analysis was conducted to identify patterns, correlations, and trends.

Visualization and Dashboard Development
The final insights were presented through an interactive dashboard designed to communicate the education-to-employment pipeline.

Dashboard Features

The interactive platform presents several analytical views

Education Output
Visualizations showing the number of female graduates from technical training programs.

Sector Demand
Charts illustrating employment demand across key industries such as technology and energy.

Workforce Participation Trends
Time-series analysis showing changes in female workforce participation.

Regional Insights
Geographic visualizations highlighting workforce patterns across different regions.

Gap Analysis
Comparisons between education supply and employment demand to identify potential mismatches.

The goal of these visualizations is to present a clear picture of how education and employment systems interact.

Key Insights

Initial exploration of the data reveals several interesting trends.

Female workforce participation has increased significantly over recent years, reflecting structural changes in the labor market.

Technical education programs continue to expand, increasing the number of qualified female graduates.

However, some sectors show stronger alignment between education output and employment demand than others.

These patterns highlight the importance of understanding the full education-to-employment pipeline when evaluating workforce development strategies.

Technology Stack

The project combines data analysis tools with modern visualization techniques.

Python was used for data processing and analysis.
Pandas was used for data manipulation and transformation.
Visualization tools were used to create interactive charts and dashboards.
GitHub Pages was used to publish the interactive platform.

The goal was to build a lightweight but clear analytical environment capable of communicating insights effectively.

Project Structure

The repository follows a simple data science structure.

data
Contains raw and processed datasets used in the analysis.

notebooks
Exploratory analysis and data investigation.

scripts
Data cleaning and transformation logic.

dashboard
Files used to generate the interactive visualizations.

docs
Project documentation and additional notes.


## Repository Structure

```
nabdh-altaaleem/
├── dataset/
│   ├── women_participation_ICT.csv       Raw data — women's ICT participation rate 2020-2024
│   └── male_female_ratio_2024.csv        Raw data — gender ratio in ICT workforce 2024
│
├── notebooks/
│   ├── analysis.py                       Data cleaning, analysis, and chart generation
│   └── generate_report.py               PDF report generator
│
├── dashboard/
│   └── index.html                        Interactive web dashboard
│
└── report/
    ├── findings_report.pdf               Full analytical report with findings and recommendations
    └── charts/
        ├── chart1_participation_trend.png
        ├── chart2_gender_ratio.png
        └── chart3_comparison.png
```

## How to Run

Install dependencies:

```
pip install pandas matplotlib seaborn fpdf2
```

Run the analysis and generate charts:

```
python notebooks/analysis.py
```

Generate the PDF report:

```
python notebooks/generate_report.py
```

Project Motivation

This project was developed as an independent exploration of how public datasets can be used to understand workforce development trends.

Rather than focusing solely on software development, the aim was to combine data analysis, visualization, and storytelling to highlight patterns within national education and employment systems.

Live Dashboard

The interactive version of the project can be explored here

https://raghadfraihanalharthi-tech.github.io/nabdh-altaaleem/

Author

Raghad F. AL-blahdi
Computer Science Student
Interested in data analysis, technology policy, and workforce analytics.
