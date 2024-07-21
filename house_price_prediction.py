import streamlit as st
import pandas as pd
import joblib

# Load the saved model
model_path = 'E:\Bootcampp\\house_price_prediction\\ML_MODEL\\decision_tree_regression.pkl'
model_reg = joblib.load(model_path)
modell_path = 'E:\Bootcampp\\house_price_prediction\\ML_MODEL\\random_forest_model.pkl' 
model_class = joblib.load(modell_path)

# Extract features names from the mdoel if they are available
try:
    expected_columns = model_reg.feature_names_in_
except AttributeError:
    st.error("The model does not contain feature names. Please ensure the model is trained with feature names.")

def main():
    # Set the title oof the web page
    st.title("House Price Prediction")

    # Add a description
    st.write('Please provide the information related to the house for price prediction')

    # Create columns for layout
    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader('House Information')

        # Add input fields for features
        no_of_bedrooms = st.slider("Number of Bedrooms", 0, 40, 3)
        no_of_bathrooms = st.slider("Number of Bathrooms", 1, 4, 1)
        sqft_living = st.slider("Square Ft living Area", 500, 15000, 1180)
        sqft_lot = st.slider("Square Loft", 500, 1500000, 5650)
        floors = st.slider("Floors", 1, 5, 1)
        water_front = st.selectbox("Water Front",['0', '1'])
        view = st.selectbox("View (0-5)", ['0', '1', '2', '3', '4', '5'])
        condition = st.selectbox("Condition (1-5)", ['1', '2', '3', '4', '5'])        
        grade = st.slider("Grade (1-15)", 1, 15, 7)
        sqft_above = st.slider("Sqaure Above ",200, 10000, 1180)
        sqft_basement = st.slider("Square Basement", 0, 5000, 0)       
        yr_built = st.slider("Built Year", 1900, 2024, 1995)
        yr_renovated = st.slider("Renovated Year", 0, 2024, 0)
        zipcode = st.slider("Zipcode", 98000, 99000, 98178) 
        lat = st.slider("Latitude", 0, 90, 0)  
        lon = st.slider("Longitude", 0, 180, 0)             
        sqft_living15 = st.slider("Square Living 15", 400, 7000, 1340)
        sqft_lot15 = st.slider("Square Living 15", 650, 900000, 5650)
        untrained_column = st.text_input('Additional Information (not used in prediction process)')

    # Absence of Ctaegorical columns in the dataset

    # Prepare input data as a Dataframe
    input_data = pd.DataFrame({
        'bedrooms': [no_of_bedrooms],
        'bathrooms': [no_of_bathrooms],
        'sqft_living': [sqft_living],
        'sqft_lot': [sqft_lot],
        'floors': [floors],
        'waterfront': [water_front],
        'view': [view],
        'condition': [condition],
        'grade': [grade],
        'sqft_above': [sqft_above],
        'sqft_basement': [sqft_basement],
        'yr_built': [yr_built],
        'yr_renovated': [yr_renovated],
        'zipcode': [zipcode],
        'lat': [lat],
        'long': [lon],
        'sqft_living15': [sqft_living15],
        'sqft_lot15': [sqft_lot15]
    })

    # Ensure columns are in the same order as during model training
    input_data = input_data[expected_columns]

    # Prediction and results section
    with col2:
        st.subheader('Prediction of the Price')
        if st.button('Predict'):
            prediction = model_reg.predict(input_data)
            prediction1 = model_class.predict(input_data)
            probability = model_class.predict_proba(input_data)[0][1]
            
            st.write(f"Prediction according to the data is around $ {int(prediction)}k.")
            ans = "High" if prediction1[0] == 1 else "Low"
            if ans == "High":
                st.success(f"The price is {ans}")
            else:
                st.error(f"The price is {ans}")
            st.write(f"Probability of High Value: {probability:.2f}")

            # Provide recommendations
            if prediction1 == 0:
                st.error("Your budget is too low. Consider improving the specifications.")
            else:
                st.success("The specifications in this price range is awesome. Increase the specs if budget can be expanded more.")

if __name__ == '__main__':
    main()