# Nabdh Al-Taaleem — Women in Saudi ICT

A complete data case study analyzing the participation of Saudi women in the Information and Communications Technology (ICT) sector, benchmarked against Vision 2030 targets and ITU global standards.

## Live Dashboard

https://raghadfraihanalharthi-tech.github.io/nabdh-altaaleem/

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

## Key Findings

Women's participation in Saudi ICT grew from 24.08% in 2020 to 34.50% in 2024, an increase of 10.42 percentage points over four years. Saudi Arabia has surpassed its Vision 2030 target of 30% and exceeds the ITU global benchmark of less than 33%. However, women still represent only 10% of the total ICT workforce, indicating that absolute workforce numbers require continued focus.

## Data Sources

All data points are fully cited and traceable to their original sources.

Saudi Open Data Platform (open.data.gov.sa) — Women's ICT participation rate 2020 to 2024

Saudi Open Data Platform (open.data.gov.sa) — Male and female ICT workforce ratio 2024

Vision 2030 Official Document (vision2030.gov.sa) — Women's labor market participation target

International Telecommunication Union ITU 2024 — Global share of women in technology roles

All government data is used under the Saudi Open Data License (CC BY 4.0).

## Author

Raghad Al-Blahdi
Computer Science Student
Data Analysis and UX Design
