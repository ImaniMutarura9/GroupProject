# Imports
import streamlit as st
import datetime
import pandas as pd
import numpy as np
import pickle

# Title
st.title("Famous Five Job Application")
st.write("This is the Famous Five web app.")

# Input fields
first_name = st.text_input("First Name")
last_name = st.text_input("Last Name")
gender = st.selectbox("Gender", ["Male", "Female"])
age = st.number_input("Your age", 0, 100, 30, 1)
dob = st.date_input(
    "Your Birthday",
    value=datetime.date(2000, 1, 1),
    min_value=datetime.date(1900, 1, 1),
    max_value=datetime.date.today()
)
marital_status = st.radio("Marital status", ["Single", "Married"])
years_of_experience = st.slider("Years of experience", 0, 40)
education_list = ["High School", "Bachelor's Degree", "Master's", "PhD"]
education = st.selectbox("Education Level", education_list)

# Load and preprocess dataset
df = pd.read_csv('salaryData.csv')
df = df.dropna()

# Filter job titles with at least 5 entries
df_edited = df.groupby('Job Title').filter(lambda x: len(x) > 4)

# Encode categorical variables
df_edited['Job Title'] = df_edited['Job Title'].astype('category')
df_edited['Education Level'] = df_edited['Education Level'].astype('category')
df_edited['Gender'] = df_edited['Gender'].astype('category')

df_edited['Job Title Encoded'] = df_edited['Job Title'].cat.codes
df_edited['Education Level Encoded'] = df_edited['Education Level'].cat.codes
df_edited['Gender Encoded'] = df_edited['Gender'].cat.codes

# Final dataset
df_final = df_edited.drop(['Gender', 'Education Level', 'Job Title'], axis=1)

# Load trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)


# Create job list from data
job_categories = df_edited['Job Title'].cat.categories.tolist()
job = st.selectbox("Job Role", job_categories)

# Button and prediction
if st.button("Predict Salary"):
    try:
        # Get encoded values
        job_code = df_edited['Job Title'].cat.categories.get_loc(job)
        education_code = df_edited['Education Level'].cat.categories.get_loc(education)
        gender_code = df_edited['Gender'].cat.categories.get_loc(gender)

        # Create feature array
        user_input = np.array([[age, years_of_experience, job_code, education_code, gender_code]])

        # Make prediction
        predicted_salary = model.predict(user_input)[0]

        # Display result
        st.success(f"Estimated salary: ${int(predicted_salary):,}")
    except Exception as e:
        st.error(f"Prediction failed: {e}")