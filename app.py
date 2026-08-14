
import streamlit as st
import pickle
import numpy as np


# Load trained model
with open("model/house_price_model.pkl", "rb") as file:
    model = pickle.load(file)


# Page configuration
st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="centered"
)


# Title
st.title("🏠 Bengaluru House Price Prediction")
st.write("Enter the property details below to estimate the house price.")


# User inputs
location = st.text_input(
    "Location",
    value="Whitefield"
)

total_sqft = st.number_input(
    "Total Area (sq ft)",
    min_value=300.0,
    max_value=10000.0,
    value=1200.0
)

bath = st.number_input(
    "Number of Bathrooms",
    min_value=1,
    max_value=10,
    value=2
)

balcony = st.number_input(
    "Number of Balconies",
    min_value=0,
    max_value=5,
    value=1
)

bhk = st.number_input(
    "Number of Bedrooms (BHK)",
    min_value=1,
    max_value=10,
    value=2
)


# Prediction button
if st.button("Predict House Price"):

    # Location encoding
    locations = model.feature_names_in_

    input_data = np.zeros(len(locations))

    if location in locations:
        input_data[list(locations).index(location)] = 1

    # Find numerical feature positions
    input_features = np.zeros(len(locations))

    for i, feature in enumerate(locations):

        if feature == "total_sqft":
            input_features[i] = total_sqft

        elif feature == "bath":
            input_features[i] = bath

        elif feature == "balcony":
            input_features[i] = balcony

        elif feature == "bhk":
            input_features[i] = bhk

        elif feature == location:
            input_features[i] = 1

    # Make prediction
    prediction = model.predict([input_features])[0]

    st.success(
        f"Estimated House Price: ₹{prediction:.2f} Lakhs"
    )