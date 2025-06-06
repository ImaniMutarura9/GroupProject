# Adding the streamlit library and assigning it an alias for reference
import streamlit as st

# main title of the application that appears at the very top
st.title("Title: Bio Data")

# brief subtitle like description that describes the app
st.write( "This is a sample web app.")

# Include a text box that takes in first and last name as text parameters
first_name = st.text_input("First Name")
last_name = st.text_input("Last Name")

# Selection box with male/female option
gender= st.selectbox("Gender", ["Male", "Female"])

# Text box that takes in number parameters between 0 and 100 with 30 being the default
age = st.number_input("Your age", 0, 100, 30, 1)

# Date input box 
dob = st.date_input("Your Birthday")

# Radio like selection for marital status- tick/select  where applicable
marital_status = st.radio("Marital status", ["Single", "Married"])

# Sliding bar for experience period in years, between 0 and 40
years_of_experience = st.slider("Years of experience", 0, 40)