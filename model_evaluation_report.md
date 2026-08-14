
# House Price Prediction — Model Evaluation Report

## 1. Project Overview

The House Price Prediction System is a machine learning project developed to predict residential property prices in Bengaluru based on property-related features.

The project includes data cleaning, preprocessing, exploratory data analysis, feature engineering, regression model development, model evaluation, and a Streamlit prediction interface.

## 2. Dataset

The project uses the Bengaluru House Price dataset.

After data cleaning and preprocessing, the dataset contained:

- **Rows:** 12,362
- **Columns:** 6

The main features used for prediction are:

- Location
- Total Area (sq ft)
- Number of Bathrooms
- Number of Balconies
- Number of Bedrooms (BHK)

The target variable is:

- Price (Lakhs)

## 3. Data Preprocessing

The following preprocessing steps were performed:

1. Missing values were handled.
2. The `total_sqft` column was converted into numerical values.
3. The `size` column was converted into a numerical BHK feature.
4. Unrealistic BHK values were removed.
5. Price per square foot was calculated.
6. Price outliers were removed.
7. Rare locations were grouped into an `other` category.
8. Unnecessary columns were removed.
9. Location was converted into numerical features using one-hot encoding.
10. The dataset was divided into training and testing sets.

## 4. Train-Test Split

The processed dataset was divided into training and testing data.

### Training Data

- Samples: 9,889
- Features: 226

### Testing Data

- Samples: 2,473
- Features: 226

## 5. Models Evaluated

Two regression models were evaluated:

### Linear Regression

Linear Regression was used as the primary regression model.

### Random Forest Regression

Random Forest Regression was also trained and evaluated for comparison.

## 6. Model Performance

### Linear Regression

| Metric | Score |
|---|---:|
| R² Score | 0.7284 |
| MAE | 29.51 Lakhs |
| RMSE | 51.17 Lakhs |

### Random Forest Regression

| Metric | Score |
|---|---:|
| R² Score | 0.6724 |
| MAE | 25.20 Lakhs |
| RMSE | 56.19 Lakhs |

## 7. Model Comparison

The two models were compared using R² Score, Mean Absolute Error (MAE), and Root Mean Squared Error (RMSE).

Linear Regression achieved a higher R² Score and a lower RMSE compared with Random Forest Regression.

Random Forest achieved a lower MAE, meaning its average absolute prediction error was lower on the test data.

Based on the overall evaluation, Linear Regression was selected as the final model because it achieved the better overall performance according to R² Score and RMSE.

## 8. Final Model

The final Linear Regression model was saved as:

`model/house_price_model.pkl`

The saved model was successfully loaded and tested after saving.

## 9. Example Prediction

An example test prediction was performed using a property with an actual price of:

**75.00 Lakhs**

The model predicted:

**66.13 Lakhs**

The difference between the actual and predicted price was approximately:

**8.87 Lakhs**

## 10. Prediction Interface

A Streamlit-based prediction interface was developed for the project.

The application allows users to enter:

- Location
- Total Area (sq ft)
- Number of Bathrooms
- Number of Balconies
- Number of Bedrooms (BHK)

The application then uses the trained Linear Regression model to estimate the property price.

Example application prediction:

**Estimated House Price: ₹68.33 Lakhs**

## 11. Visualizations

The project includes visualizations for:

1. House Price Distribution
2. BHK Distribution
3. House Area vs Price
4. Actual Price vs Predicted Price
5. Prediction Error Distribution

These visualizations were used to understand the dataset and evaluate model predictions.

## 12. Conclusion

The House Price Prediction System successfully demonstrates the use of machine learning for estimating Bengaluru residential property prices.

The project covers the complete machine learning workflow from data preprocessing and exploratory data analysis to model training, evaluation, model saving, and deployment through a Streamlit prediction interface.

The Linear Regression model was selected as the final model based on its overall evaluation performance.