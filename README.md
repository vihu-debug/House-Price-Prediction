# House Price Prediction

## Project Overview

This project predicts house prices in Bengaluru using machine learning.

The project uses property-related information such as location, total square feet, number of bathrooms, balcony availability, and number of bedrooms (BHK) to estimate house prices.

## Dataset

The dataset contains Bengaluru house property information.

Initial dataset:
- Records: 13,320
- Features: 9

After data preprocessing and outlier removal:
- Records: 12,362
- Features used for prediction: 6

## Features Used

- Location
- Total Square Feet
- Bathroom
- Balcony
- BHK

## Data Preprocessing

The following preprocessing steps were performed:

1. Loaded the Bengaluru house price dataset.
2. Handled missing values.
3. Converted `total_sqft` into numerical values.
4. Extracted BHK values from the `size` column.
5. Removed unrealistic BHK values.
6. Created a `price_per_sqft` feature.
7. Removed price-per-square-foot outliers.
8. Grouped rare locations into `other`.
9. Removed unnecessary columns.
10. Converted location into numerical features.
11. Split the dataset into training and testing sets.

## Machine Learning Models

### Linear Regression

- R² Score: 0.7284
- MAE: 29.51 lakhs
- RMSE: 51.17 lakhs

### Random Forest Regression

- R² Score: 0.6724
- MAE: 25.20 lakhs
- RMSE: 56.19 lakhs

Linear Regression performed better overall based on R² and RMSE.

## Visualizations

The project contains the following visualizations:

1. House Price Distribution
2. BHK Distribution
3. House Area vs Price
4. Actual Price vs Predicted Price
5. Prediction Error Distribution

## Example Prediction

For one test example:

- Actual Price: 75.00 lakhs
- Predicted Price: 66.13 lakhs

## Model Saving

The trained Linear Regression model was saved as:

`model/house_price_model.pkl`

The saved model was successfully loaded and tested.

## Project Structure

```text
HOUSE-PRICE-PREDICTION/
│
├── data/
│   └── Bengaluru_House_Data.csv
│
├── images/
│
├── model/
│   └── house_price_model.pkl
│
├── notebook/
│   └── house_price_prediction.ipynb
│
└── README.md
