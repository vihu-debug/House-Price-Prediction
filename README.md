
# 🏠 Bengaluru House Price Prediction

A Machine Learning project that predicts **house prices in Bengaluru** based on property details such as location, total area, number of bathrooms, balconies, and BHK.

The project includes complete data analysis, visualization, model training, evaluation, and a deployed Streamlit web application.

## 🚀 Live Demo

Try the deployed application:

👉 [Bengaluru House Price Prediction](https://bengaluru-house-price-prediction-vanshika.streamlit.app)

## 📌 Project Overview

The goal of this project is to build a machine learning model that can estimate the price of a residential property in Bengaluru.

The project follows a complete Machine Learning workflow:

- Data collection
- Data cleaning
- Exploratory Data Analysis (EDA)
- Data preprocessing
- Feature engineering
- Data visualization
- Model training
- Model evaluation
- Model saving
- Streamlit application development
- Cloud deployment

## 📊 Dataset

The dataset contains Bengaluru residential property information including:

- Location
- Total square feet
- Number of bathrooms
- Number of balconies
- BHK
- Price

Dataset file:

```text
data/Bengaluru_House_Data.csv
```

## 📈 Exploratory Data Analysis

The dataset was explored using different visualizations to understand the distribution and relationships between the variables.

### Graph 1 — House Price Distribution

The distribution of house prices was visualized using a histogram to understand the spread of property prices.

### Graph 2 — BHK Distribution

The distribution of the number of bedrooms (BHK) was analyzed to understand the common property configurations.

### Graph 3 — Area vs Price

A scatter plot was used to analyze the relationship between total property area and house price.

## 🤖 Machine Learning Model

The project uses **Linear Regression** to predict house prices.

The trained model is saved as:

```text
model/house_price_model.pkl
```

## 📋 Model Evaluation

Model evaluation and performance details are documented in:

```text
model_evaluation_report.md
```

The evaluation report contains information about the model performance and prediction results.

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Streamlit
- Joblib
- Jupyter Notebook
- Git
- GitHub

## 🧠 Project Workflow

```text
Dataset
   ↓
Data Cleaning
   ↓
Exploratory Data Analysis
   ↓
Data Preprocessing
   ↓
Feature Engineering
   ↓
Model Training
   ↓
Model Evaluation
   ↓
Model Saving
   ↓
Streamlit Application
   ↓
Deployment
```

## 💻 Running the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/vihu-debug/House-Price-Prediction.git
```

### 2. Navigate to the project folder

```bash
cd House-Price-Prediction
```

### 3. Install the required dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
streamlit run app.py
```

The application will open in your browser.

## 🌐 Deployment

The application is deployed using **Streamlit Community Cloud**.

### Live Application

👉 [Bengaluru House Price Prediction](https://bengaluru-house-price-prediction-vanshika.streamlit.app)

### GitHub Repository

👉 [House Price Prediction](https://github.com/vihu-debug/House-Price-Prediction)

## 📓 Jupyter Notebook

The complete data analysis, preprocessing, visualization, model training, and evaluation workflow is available in:

```text
notebook/house_price_prediction.ipynb
```

## 📦 Requirements

The required Python libraries are listed in:

```text
requirements.txt
```

Main dependencies include:

- Streamlit
- NumPy
- Scikit-learn
- Pandas
- Matplotlib
- Joblib

## 🎯 Features of the Application

The Streamlit application allows users to enter:

- Location
- Total Area (sq ft)
- Number of Bathrooms
- Number of Balconies
- Number of Bedrooms (BHK)

After entering the property details, the application predicts the estimated house price.

## 📌 Future Improvements

Possible improvements for the project include:

- Trying additional machine learning algorithms
- Hyperparameter tuning
- Improving model accuracy
- Adding more advanced feature engineering
- Adding interactive visualizations
- Expanding the application with additional property analysis features

## 👩‍💻 Author

**Vanshika Chaudhary**

GitHub:

👉 [vihu-debug](https://github.com/vihu-debug)

## ⭐ Project

If you find this project useful, consider giving the repository a ⭐ on GitHub.