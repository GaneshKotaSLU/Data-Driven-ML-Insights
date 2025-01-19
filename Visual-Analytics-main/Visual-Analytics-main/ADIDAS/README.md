# Data Visualization and Analytics Repository

## Overview

This repository showcases diverse data visualizations and analytics projects, including a comprehensive analysis of Adidas shoe data and other datasets. It aims to highlight trends, patterns, and insights across various domains using tools like Power BI and Python.

## About the Dataset

## Source:

The dataset was collected from Adidas Germany website using ethical web scraping techniques. The data represents approximately 3400 unique shoe models with multiple size-availability pairs updated daily for 12 days. Some countries (e.g., Germany) have multiple days of data, while others have fewer.

## Disclaimer:

Availability Column: The dataset contains a significant number of 'max' (15) values for availability. This likely indicates Adidas' restocking process, which may occur randomly. Users are encouraged to filter out these values and optionally exclude '0' values, depending on their use case.

The data was collected during the afternoon and late-night hours.

## Dataset Details:

## Files Used:

country_dim.csv: Country-level metadata

shoes_dim.csv: Dimension data related to shoes (e.g., name, SKU, and characteristics)

shoes_fact.csv: Fact table containing transactional and availability data

## Columns:

name: Shoe model name

id: SKU identifier

price: Price in EUR

category: Shoe style

color: Dominant and additional colors

best_for_wear: Intended occasion or use case (e.g., running, casual)

size: Size metrics (Europe, US, UK)

availability: Stock availability (0–15)

image_url: Link to shoe's image

gender: Gender category (U: Unisex, W: Woman, M: Male, K: Kid)

date: Collection date (dd/mm/yyyy)

country_code: Country identifier (US, DE, UK, BE)

## License:

This dataset is released under the CC0: Public Domain license and is freely available for educational and analytical purposes.

## Source Reference:

Tamas Nedo. (2025). Adidas Webstore Shoe Data [Data set]. Kaggle. https://doi.org/10.34740/KAGGLE/DSV/10499384

## Analysis Highlights

## Key Questions Addressed:

1. How does pricing vary across regions and categories?
2. What are the availability trends for different shoe models and sizes?
3. Which categories and sizes are most popular across genders?
4. What insights can be drawn from regional stock patterns?

## Dashboards:

* ## Dashboard 1: Regional Pricing, Category Trends, and Gender Preferences
    * ### Visuals:

      i. Average price by shoe metric (USA, EU, UK)
    
      ii. Category-wise price contributions
    
      iii. Gender distribution for various occasions (e.g., running, casual)

* ## Dashboard 2: Availability and Size-Based Insights
    * ### Visuals:

      i. Standard deviation of prices by size

      ii. Monthly availability trends

      iii. Average availability across sizes

* ## Dashboard 3: Regional Performance Analysis
    * ### Visuals:

      i. Waterfall chart for regional pricing trends
      ii. Geographic map of availability by country

## Tools Used:

1Power BI: For data visualization and interactive dashboards

Python: For data extraction and cleaning

Excel/CSV: For storing and organizing datasets

## Repository Structure


![image](https://github.com/user-attachments/assets/40961d34-4037-4e2a-a56d-3fe729cfdbc2)


## How to Use

### Prerequisites:

1. Install Power BI Desktop to open .pbix files.
2. Download Python and required libraries (if using the data_cleaning.ipynb notebook).

## Instructions:

Data Cleaning:

Firstly, run the summaries on the data to check for any inconcsistencies and clean them as per your requirements. 

## Load Dashboards:

Open the .pbix files in Power BI Desktop to explore the interactive dashboards.

## Interactive Filtering:

Use slicers in the dashboards to filter data by region, category, gender, etc.

## Key Insights

* Pricing Patterns: USA shoes have the highest average prices compared to EU and UK metrics.

* Category Leaders: Running shoes and outdoor shoes dominate in terms of total price contribution.

* Availability Trends: Stock levels fluctuate significantly by size and region, with restocking patterns visible in certain categories.

## Contribution

Contributions are welcome! If you would like to enhance the analysis or add new features, feel free to fork this repository and submit a pull request.

## Credits

Data Collector: Tamas Nedo (https://www.kaggle.com/tamsnd)

Analysis and Visualization: [Ganesh Kota]

## License

This project is licensed under the CC0: Public Domain license. Feel free to use it for personal or commercial projects.
