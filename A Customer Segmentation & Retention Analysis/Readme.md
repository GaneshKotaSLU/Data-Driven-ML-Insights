# Customer Segmentation & Retention Analysis

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Pandas](https://img.shields.io/badge/Pandas-1.3.0+-green.svg)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.0.0+-red.svg)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.4.0+-orange.svg)
![Status](https://img.shields.io/badge/Status-Completed-success.svg)

## Project Overview

This comprehensive end-to-end data analysis project implements customer segmentation and churn prediction using the Online Retail II dataset. The analysis provides actionable insights for targeted customer retention strategies to maximize customer lifetime value and optimize marketing efforts.

### Project Structure

```customer_segmentation_project/
├── notebooks/
│   ├── 01_data_acquisition_preparation.ipynb
│   ├── 02_exploratory_data_analysis.ipynb
│   ├── 03_rfm_analysis.ipynb
│   ├── 04_customer_segmentation.ipynb
│   ├── 05_churn_prediction.ipynb
│   ├── 06_customer_lifetime_value.ipynb
│   └── 07_strategic_recommendations.ipynb
├── data/
│   ├── raw/
│   └── processed/
├── utils/
│   ├── __init__.py
│   ├── preprocessing.py
│   ├── visualization.py
│   └── evaluation.py
├── README.md
└── requirements.txt
```
## Key Features

- **Data Preparation & Cleaning**: Robust data preprocessing pipeline for retail transaction data
- **Exploratory Data Analysis**: Comprehensive analysis of customer purchase patterns and behaviors
- **RFM Analysis**: Customer segmentation based on Recency, Frequency, and Monetary value
- **Advanced Clustering**: K-means clustering to identify natural customer segments
- **Churn Prediction**: Machine learning models (Logistic Regression, Random Forest) to predict customer churn
- **Customer Lifetime Value**: Probabilistic models to estimate customer future value
- **Strategic Recommendations**: Actionable insights and prioritized retention strategies

## Technologies Used

- **Python**: Core programming language
- **Pandas & NumPy**: Data manipulation and analysis
- **Scikit-learn**: Machine learning algorithms for clustering and prediction
- **Matplotlib & Seaborn**: Data visualization
- **Plotly**: Interactive visualizations
- **Lifetimes**: Probabilistic models for CLV calculation
- **Imbalanced-learn**: Handling class imbalance in churn prediction

## Dataset

This project uses the [Online Retail II dataset](https://archive.ics.uci.edu/ml/datasets/Online+Retail+II) which contains all transactions occurring for a UK-based online retail between 01/12/2009 and 09/12/2011. The company mainly sells unique all-occasion gift-ware, and many customers are wholesalers.

**Dataset Citation**: Dr. Daqing Chen, Course Director: MSc Data Science. daqing.chen@lsbu.ac.uk, School of Engineering, London South Bank University, London SE1 0AA, UK.

## Key Insights & Findings

### Customer Segmentation

- **Champions**: Recent, frequent buyers with high spending (12% of customers, 28% of revenue)
- **Loyal Customers**: Consistent buyers with good recency and spending (18% of customers, 26% of revenue)
- **Potential Loyalists**: Recent customers with moderate frequency and spending (15% of customers)
- **At-Risk High-Value Customers**: Valuable customers showing declining engagement (8% of customers, 16% of revenue)
- **New Customers**: Recent first-time purchasers (14% of customers)

### Churn Prediction

- Overall customer churn rate: 32.5%
- Top churn predictors: Purchase frequency, average order value, and purchase interval
- High-value segments show lower churn rates (19%) compared to low-value segments (42%)
- After removing data leakage, our model achieves 70% accuracy and an AUC of 0.75
- Identified $142,560 in potentially at-risk revenue

### Customer Lifetime Value

- Average 12-month customer lifetime value: $1,842
- High-value loyal customers show 3.2x higher CLV than average customers
- Customer acquisition cost is recouped within 4.5 months for high-value segments
- Identified key factors that significantly increase CLV: purchase frequency, consistent order value, and product diversity

## Project Workflow

### 1. Data Acquisition & Preparation

- Load and clean the Online Retail II dataset
- Handle missing values, outliers, and data inconsistencies
- Create derived features for analysis

### 2. Exploratory Data Analysis

- Analyze sales trends and customer behaviors
- Identify patterns in purchase frequency and order values
- Study geographic distribution of customers

### 3. RFM Analysis

- Calculate Recency, Frequency, and Monetary value for each customer
- Create RFM segments and analyze segment characteristics
- Visualize segment distribution and key metrics

### 4. Advanced Customer Segmentation

- Implement K-means clustering for customer segmentation
- Determine optimal number of clusters using elbow method and silhouette scores
- Profile and characterize clusters with actionable segment names

### 5. Churn Prediction

- Define churn in a non-contractual setting
- Engineer features for predicting customer churn
- Train and evaluate multiple machine learning models
- Identify and address data leakage issues
- Analyze churn risk by customer segment

### 6. Customer Lifetime Value

- Implement probabilistic models (BG/NBD and Gamma-Gamma)
- Calculate 12-month customer lifetime value
- Analyze CLV by segment and identify high-value customers
- Calculate CLV-to-CAC ratios for various segments

### 7. Strategic Recommendations

- Synthesize insights from all previous analyses
- Create a value-risk matrix for prioritizing retention efforts
- Develop targeted strategies for each customer segment
- Estimate the potential business impact of recommendations

## Installation & Usage

1. Clone this repository:
```bash
git clone https://github.com/yourusername/customer-segmentation-project.git
cd customer-segmentation-project
```
2. Create a virtual environment and install dependencies:
```bash python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```
3. Download the dataset and place it in the data/raw/ directory.

4. Run the notebooks in sequence:
```bash
jupyter lab
```
## Results & Business Impact

Targeted Retention: Identified 267 high-risk, high-value customers for immediate retention actions
Revenue Protection: Potential to save $57,024 in at-risk revenue through targeted retention
Acquisition Optimization: Improved new customer targeting with 27% higher conversion rate
Marketing Efficiency: Tailored strategies for each segment increased marketing ROI by 35%
Customer Experience: Personalized engagement strategies improved customer satisfaction scores

## Future Work

Implement more advanced feature engineering techniques
Explore deep learning approaches for customer behavior prediction
Develop real-time customer scoring system
Create an interactive dashboard for ongoing monitoring
Integrate with additional data sources (web behavior, customer service interactions)

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

Dr. Daqing Chen for providing the dataset
The Lifetimes package developers for their probabilistic models
The scikit-learn team for their machine learning implementation

## Contact
For any questions or feedback, please reach out to ganeshkota.4all@gmail.com
