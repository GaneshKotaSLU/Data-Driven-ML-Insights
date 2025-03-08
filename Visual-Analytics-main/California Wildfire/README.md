# California Wildfire Impact Analysis Dashboard

## Project Overview

This repository contains a comprehensive analytical dashboard focused on California wildfire incidents and their impacts from 2014-2023. The interactive Power BI visualization provides deep insights into wildfire damage patterns, financial losses, casualties, and geographical distribution, enabling data-driven decision making for disaster management and environmental policy planning.

### Report Preview
![19D317C8-8FA8-4992-AE20-303D3E6D139C_1_105_c](https://github.com/user-attachments/assets/41d46d0e-ad22-4eec-ac8f-a78f4765bbb7)


## Features

### Advanced Visualization Components

- **Comprehensive KPI Tracking**: Interactive cards displaying critical metrics (Total Financial Loss: $239.61K, Total Houses Destroyed: 94K, Total Fatalities: 993) with trend sparklines showing historical patterns
- **Temporal Pattern Analysis**: Time-series visualizations tracking damage metrics over a 10-year period with year-over-year comparisons
- **Geographical Impact Distribution**: Interactive donut chart visualization showing proportional area burned across California counties with detailed percentage breakdowns
- **Cause Attribution Analysis**: Hierarchical bar charts ranking wildfire causes by fatality count, enabling root cause assessment
- **Multi-dimensional Damage Assessment**: Specialized visualizations comparing injuries vs fatalities and business damage by location to provide comprehensive impact perspectives

### Interactive Filtering Capabilities

- Year-based filtering mechanism for temporal trend analysis
- Location-based filters for county-specific damage assessment
- Cause-based filtering to analyze impacts by wildfire origins
- Custom dynamic highlighting through cross-filtering interactions
- Responsive visualizations that update instantly based on selected filters

### Key Environmental Insights Revealed

- Lightning-caused wildfires resulted in the highest fatality count (365), followed by human activity (345)
- Shasta County experienced the highest percentage of area burned (13.42%, 356K acres)
- Sonoma County faced significant wildfire impacts with 12.13% (322K acres) of total burned area
- Injuries consistently outnumber fatalities across all wildfire incidents by approximately 5:1 ratio
- Business damage shows strong correlation with population density, particularly in coastal counties

## Data Architecture

The dashboard is powered by a structured data model with:

- **Primary Dataset**: Cleaned wildfire incident records with comprehensive damage metrics
- **Dimension Tables**: 
  - Temporal dimensions (year, date)
  - Geographical dimensions (counties, regions)
  - Damage metrics (financial, structural, human impact)
  - Cause attribution categories

The data model implements a star schema architecture for optimal query performance and analytical flexibility.

## Technical Implementation

### Tools & Technologies Used

- **Power BI Desktop**: Core development environment for data modeling and visualization
- **Python**: Data cleaning and preparation for advanced analysis
- **DAX (Data Analysis Expressions)**: Custom calculated measures for trend analysis
- **Power Query (M)**: ETL processes for data transformation
- **Color Psychology Principles**: Strategic color selection for intuitive data interpretation

### Advanced Techniques Applied

- Custom purple-themed color palette optimized for impact visualization
- Year-over-year trend analysis with sparklines showing temporal patterns
- Conditional formatting highlighting critical impact metrics
- Custom tooltips providing contextual insights on hover
- Optimized data model with appropriate relationship cardinality
- Shadow effects and visual hierarchy to enhance dashboard aesthetics

## Environmental Impact Assessment

This dashboard solution provides critical insights for disaster management:

- **Identifying High-Risk Areas**: Pinpoints counties with recurring wildfire patterns
- **Cause Attribution Analysis**: Supports targeted prevention strategies based on primary causes
- **Financial Impact Quantification**: Provides economic context to environmental damage
- **Human Impact Visualization**: Correlates structural damage with human casualties
- **Temporal Pattern Recognition**: Identifies seasonal and yearly trends for predictive planning

## Getting Started

### Prerequisites

1. Power BI Desktop (latest version recommended)
2. Access to the California wildfire dataset (included in repository)

### Installation

1. Clone this repository:
   git clone https://github.com/ganesh-kota/california-wildfire-analysis.git
2. Open the `california_wildfire_analysis.pbix` file in Power BI Desktop
3. Refresh the data connections if necessary

### Usage Guide

1. **Filtering**: Use the year, location, and cause slicers in the left panel to filter data
2. **Temporal Analysis**: Examine the sparkline trends in the KPI cards to identify patterns
3. **Geographical Exploration**: Study the donut chart to understand regional impact distribution
4. **Cause Investigation**: Analyze the fatalities vs cause bar chart to identify primary risk factors
5. **Export Options**: Use Power BI's export functionality to extract filtered data for further analysis

## Data Sources

This dashboard is based on the "California Wildfire Damage (2014-feb2025)" dataset from Kaggle:
- Dataset Source: [California Wildfire Damage Dataset](https://www.kaggle.com/datasets/vivekattri/california-wildfire-damage-2014-feb2025)
- Creator: Vivek Attri
- Last Updated: 2025

The data processing workflow:
1. Original raw data acquired from Kaggle ("California Wildfire Damage.csv")
2. Data cleaning performed using Python to produce enhanced dataset ("cleaned_wildfire_data.csv")
3. Final cleaned dataset integrated into Power BI for visualization

The dataset contains:
- Incident identification and dates
- Geographic locations
- Impact metrics (area burned, structures destroyed, casualties)
- Financial loss estimates
- Cause attribution

## Future Enhancements

- Integration with climate data to correlate weather patterns with wildfire incidents
- Predictive analytics for wildfire risk assessment using machine learning
- Interactive map visualization with geographical heat mapping
- Time-lapse visualization showing wildfire spread patterns
- Expanded cause analysis incorporating prevention effectiveness metrics

## About the Author

With multiple years of experience performing versatile data analysis across multiple industries including healthcare, finance, retail, manufacturing, and technology sectors, I specialize in transforming complex datasets into actionable insights. My expertise spans the entire data lifecycle from ETL development and statistical analysis to predictive modeling and interactive dashboard creation.

I leverage tools like Power BI, Python, SQL, and R to deliver data solutions that drive significant improvements in operational efficiency while supporting strategic objectives.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- Original dataset created by Vivek Attri on Kaggle
- Data cleaning and preparation methodology inspired by best practices in environmental data analysis
- Dashboard design principles based on effective disaster impact visualization techniques
- Color palette optimized for accessibility and visual impact
- Special thanks to the Power BI community for sharing optimization techniques

---

© 2025 Ganesh Kota | [LinkedIn](https://www.linkedin.com/in/ganesh-kota) | [Portfolio](https://ganeshkota.com)
