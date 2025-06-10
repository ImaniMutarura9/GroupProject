# Adding the streamlit library and assigning it an alias for reference
import streamlit as st
import datetime
#Title of the web app
st.title("Famous Five Job Application")

# brief subtitle like description that describes the app
st.write( "This is a the famous five web app.")

# brief subtitle like description that describes the app
st.write( "This is a the famous five web app.")

# Include a text box that takes in first and last name as text parameters
first_name = st.text_input("First Name")
last_name = st.text_input("Last Name")

# Selection box with male/female option
gender= st.selectbox("Gender", ["Male", "Female"])

# Text box that takes in number parameters between 0 and 100 with 30 being the default
age = st.number_input("Your age", 0, 100, 30, 1)

# Allow selecting birthdays as far back as Jan 1, 1900
dob = st.date_input(
    "Your Birthday",
    value = datetime.date(2000,1,1), #default value shown
    min_value = datetime.date(1900,1,1),
    max_value = datetime.date.today()
    )

# Radio buttons for marital status
marital_status = st.radio("Marital status", ["Single", "Married"])

# Sliding bar for experience period in years, between 0 and 40
years_of_experience = st.slider("Years of experience", 0, 40)

#Define the job list and get user input
job_list = ["Software Engineer", "Data Scientist", "Computer Scientist", "Accountant", "Teacher"]
job = st.selectbox("Job Role", job_list)

#Define the education list and get user in[ut
education_list = ["High School", "Bachelor's Degree", "Master's", "PhD"]
education = st.selectbox("Education Level", education_list)

#gender list undes for prediction indexing
gen_list = ['Male', 'Female']

#Create 5 empty columns to center the Predict Salary button
col10, col11, col12, col13, col14 = st.columns(5)
with col10:
    st.write('')
with col11:
    st.write('')
with col12:
    predict_btn = st.button('Predict Salary')
with col13:
    st.write('')
with col14:
    st.write('')

#Define a Model class that simulates predictions
class TestModel:
    def predict(self, X):
        results = []
        for x in X:
            age, experience, job_idx, education_idx, gender_idx = X
            base = 100000 #base salary for all

            #Multiplier based on job type
            job_multiplier = [1.0, 1.2, 1.5, 1.1][job_idx]

            #Education bonuses
            education_bonus = [0, 5000, 10000, 15000][education_idx]

            #experience bonus per year
            experience_bonus = experience * 1500

            #total estimated salary
            salary = base + education_bonus + experience_bonus
            salary *= job_multiplier

            results.append(salary)

        return results
    
#create an instance of the model
model = TestModel()

#run prediction logic when the button is clicked

if (predict_btn):
    #prepare input values
    inp1 = int(age)
    inp2 = float(years_of_experience)
    inp3 = int(job_list.index(job))
    inp4 = int(education_list.index(education))
    inp5 = int(gen_list.index(gender))

    #combine all inputs into a list(as a row)
    X = [inp1, inp2, inp3, inp4, inp5] #2D list for model

    #get salary prediction
    salary = model.predict(X)

    #center the result in the middle of the screen
    col15, col16, col17 = st.columns(3)
    with col15:
        st.write('')
    with col16:
        st.text(f"Estimated salary: ${int(salary[0])}")
    with col17:
        st.write('')