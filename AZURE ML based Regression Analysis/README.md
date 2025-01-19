#### Azure-ML-US-Wage-Regression-Analysis


# US State Wise Wages Analysis using Azure Machine Learning

## Table of Contents
- [Overview](#overview-of-the-study)
- [Data](#data-assets)
- [Feature Engineering Analysis](#feature-engineering-analysis)
- [Model Performance Metrics](#model-performance-metrics)
- [Results](#results)
- [Installation](#installation)
- [Challenges and Limitations](#challenges-and-limitations)
- [Contributing](#contributing)
- [License](#license)
- [Citation](#citation)
- [Technologies Used](#technologies-used)
- [Next Steps](#next-steps)
- [Support](#support)

## Overview of the Study
This project performs the regression analysis of the Wages of the employees all around US considering different features like the employee industry, area, state, ... etc to find out how the wages are being affected with different features. Which are most critical factors contributing to the variation in wages are also studied. 

The entire study is done in the cloud environment utilizing the "Azure ML studio" and the models are deploiyment in the cloud environment itself. 

This project was inspired by recent concerns and changes pertaining to employment in the United States along with its impact in business intelligence.

## Data Assets

The data is collected from the "US Beaureau of Labor Statistics" sourced from the "State and Metro Area Employment" and "Hours and Earnings Data". More such information about the data can be found by navigating to the following URL.
https://learn.microsoft.com/en-us/azure/open-datasets/dataset-us-state-employment-earnings?tabs=azure-storage#data-access

The dataset can also be obtained from the azure ml opne datasets. There are around 64 lakh+ records in the data .
## Feature Engineering Analysis
We analyze the importance of different features in our models to understand which factors contribute most to customer churn.
- Variable Importances for Random Forest and LightGBM:
  ``` sh
  ifrom sklearn.pipeline import FeatureUnion
    
    column_group_1 = ['state_code', 'data_type_code', 'supersector_code', 'period', 'footnote_codes', 'supersector_name', 'data_type_text', 'state_name']
    
    column_group_2 = ['seasonal']
    
    column_group_0 = ['area_code', 'industry_code', 'industry_name', 'area_name']
    
    column_group_3 = [['year']]
    
    feature_union = FeatureUnion([
        ('mapper_0', get_mapper_0(column_group_0)),
        ('mapper_1', get_mapper_1(column_group_1)),
        ('mapper_2', get_mapper_2(column_group_2)),
        ('mapper_3', get_mapper_3(column_group_3)),
    ])
    return feature_union
    
  ```
  
## Model Performance Metrics

- Regression Metrics
  The following are some of the regression metrics have been used in the study:
  1. Variance
  2. Mean Absolute Percentage Error
  3. Mean Absulute Error
  4. Normalized Mean Absolute Error
  5. R2_Score
  6. Root Mean Squared Error
  7. Normalized Root Mean Sqaured Error
     ... etc.
     
 - Code Snippet for Metrics Analysis
  ``` sh
  from azureml.training.tabular.preprocessing._dataset_binning import make_dataset_bins
    from azureml.training.tabular.score.scoring import score_regression
    
    y_pred = model.predict(X_test)
    y_min = np.min(y)
    y_max = np.max(y)
    y_std = np.std(y)
    
    bin_info = make_dataset_bins(X_test.shape[0], y_test)
    metrics = score_regression(
        y_test, y_pred, get_metrics_names(), y_max, y_min, y_std, sample_weights, bin_info)
    return metrics
  ```

## Results
The results revealted other than the experience of the employees, the industry and espectially the area of the employees also matters a lot for the high or low variation in wages.

* <img width="1514" alt="image" src="https://github.com/user-attachments/assets/3b3c2907-6254-482c-8c5b-149f0ba0efcb">
* <img width="1485" alt="image" src="https://github.com/user-attachments/assets/dc0e897b-51a3-44d0-9888-460590ae1bae">


## Installation
To set up the project environment:

1. Clone the repository:
   ``` sh
   git clone https://github.com/GaneshKotaSLU/Azure-ML---US-Wage-Regression-Analysis.git
   ```
2. Navigate to the Project Directory:
   ``` sh
   cd Azure-ML---US-Wage-Regression-Analysis
   ```

## Challenges and Limitations

* Data quality and completeness varied across different employee segments.
* Since it is hosted in azure, once the subscription gets finished or the resource utlization is full, the application cannot be accessible.
* Rewuired to Have the Azure subscription if you would like to deploy the model to the server.
* Due to high volume of the available data and so the data processing and model building will take a lot of time.
## Contributing
Welcome contributions to this project. Please follow these steps:

## Fork the repository
- Create a new branch (git checkout -b feature/AmazingFeature)
- Commit your changes (git commit -m 'Add some AmazingFeature')
- Push to the branch (git push origin feature/AmazingFeature)
- Open a Pull Request

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.

## Citation
If you use this work in your research, please cite:
``` sh
Kota, G. (2023). Regression analysis of US employee wages using Azure ML. GitHub repository, https://github.com/GaneshKotaSLU/Azure-ML---US-Wage-Regression-Analysis
```
## Technologies Used
The below are few of the technologies used in this project.
* Python 3.8+
* Azure Machine Learning Studio
* LightGBM
* Tree Based Models
* Pandas
* Scikit-learn
* Matplotlib
* LightGBM


## Next Steps
This project can further be enahced by incorporating some more valuable information like the employees' domain, country, ... etc and can be fully hosted on live data if the cloud subscruption is active.

## Support
Support our work by starring our GitHub repository. For any questions or suggestions, please open an issue in the repository.

``` sh
This comprehensive README provides a detailed overview of your project, its methodology, results, and future directions. It includes all the sections we discussed earlier, with placeholders for specific results and findings that you can fill in with your actual data. The structure is designed to be informative for both technical and non-technical readers, making your project more accessible and encouraging collaboration.
```
