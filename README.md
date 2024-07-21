# House-Price_Prediction

This project implements the dataset kc_house_data, containing data from the house sales in King County, Washington State, USA, collected from kaggle.com, into a machine learning model to analyze and predict the prices of the houses according to various factors.

## Dataset
The dataset used in this project contains the following columns:

Data columns (total 19 columns):

            Column         Non-Null Count  Dtype  
     ---  | ------         --------------  -----  
     
      0   |  price          21613  non-null  float64
      1   |  bedrooms       21611  non-null  float64
      2   |  bathrooms      21613  non-null  float64
      3   |  sqft_living    21613  non-null  int64  
      4   |  sqft_lot       21610  non-null  float64
      5   |  floors         21613  non-null  float64
      6   |  waterfront     21613  non-null  int64  
      7   |  view           21613  non-null  int64  
      8   |  condition      21613  non-null  int64  
      9   |  grade          21610  non-null  float64
      10  |  sqft_above     21613  non-null  int64  
      11  |  sqft_basement  21613  non-null  int64  
      12  |  yr_built       21613  non-null  int64  
      13  |  yr_renovated   21613  non-null  int64  
      14  |  zipcode        21613  non-null  int64  
      15  |  lat            21613  non-null  float64
      16  |  long           21613  non-null  float64
      17  |  sqft_living15  21613  non-null  int64  
      18  |  sqft_lot15     21613  non-null  int64  

           dtypes: float64(8), int64(11)

## Installation
1. Clone the repository:

            git clone https://github.com/Ma-Ane/House-Price-Prediction.git

3. Enter the above folder

            cd House-Price-Prediction

4. Install the required packages listed below

            pip install package

## Required Packages
    numpy
    pandas
    streamlit
    seaborn
    matplotlib  
    scikit-learn
    scipy
    joblib

## Now to run the house_price_prediction.py, 
1. On the terminal command,

            streamlit run house_price_prediction.py
   
3. After executing, the app will open the local host in the browser and the user interface is seen.
