import streamlit as st
import pickle
import pandas as pd  # Import pandas for handling CSV files


# Load the trained model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# Streamlit app title
st.title("Breast Cancer Prediction")

# Option for batch prediction only
st.header("Batch Input (CSV File)")

# File upload for batch prediction
uploaded_file = st.file_uploader("Upload your input CSV file", type=["csv"])

if uploaded_file is not None:
    # Read the uploaded CSV file
    input_data = pd.read_csv(uploaded_file)
    
    # Ensure the input data has the right format
    st.write("Uploaded Data Preview:")
    st.write(input_data.head())

    # Ensure input data has the correct number of features (30 features)
    if input_data.shape[1] == 30:
        try:
            # Predict using the model
            predictions = model.predict(input_data)
            input_data['Prediction'] = predictions  # Add predictions as a new column
            st.write("Predictions:")
            st.write(input_data)
        except ValueError as e:
            st.error(f"Error in prediction: {e}")
    else:
        st.error("The uploaded CSV file does not have the required 30 features.")

