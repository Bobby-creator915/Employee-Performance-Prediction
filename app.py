import streamlit as st
import pandas as pd
import requests


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Employee Performance Prediction",
    page_icon="👨‍💼",
    layout="wide"
)


# --------------------------------------------------
# FastAPI Backend
# --------------------------------------------------

API_URL = "https://employee-performance-prediction-ou48.onrender.com/predict"


# --------------------------------------------------
# Title
# --------------------------------------------------

st.title("👨‍💼 Employee Performance Prediction System")

st.write(
    "Predict an employee's performance rating using a trained "
    "Machine Learning model."
)

st.divider()


# --------------------------------------------------
# Employee Information
# --------------------------------------------------

st.header("👤 Employee Information")

col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input(
        "Age",
        min_value=18,
        max_value=70,
        value=30
    )

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    education_background = st.selectbox(
        "Education Background",
        [
            "Life Sciences",
            "Medical",
            "Marketing",
            "Technical Degree",
            "Human Resources",
            "Other"
        ]
    )

with col2:
    marital_status = st.selectbox(
        "Marital Status",
        ["Single", "Married", "Divorced"]
    )

    distance_from_home = st.number_input(
        "Distance From Home",
        min_value=1,
        max_value=30,
        value=5
    )

    education_level = st.number_input(
        "Employee Education Level",
        min_value=1,
        max_value=5,
        value=3
    )

with col3:
    environment_satisfaction = st.slider(
        "Environment Satisfaction",
        1,
        4,
        4
    )

    job_satisfaction = st.slider(
        "Job Satisfaction",
        1,
        4,
        4
    )

    relationship_satisfaction = st.slider(
        "Relationship Satisfaction",
        1,
        4,
        4
    )


# --------------------------------------------------
# Job Information
# --------------------------------------------------

st.header("💼 Job Information")

col1, col2, col3 = st.columns(3)

with col1:
    department = st.selectbox(
        "Department",
        [
            "Development",
            "Sales",
            "Human Resources",
            "Finance",
            "Data Science",
            "Research & Development"
        ]
    )

    job_role = st.selectbox(
        "Job Role",
        [
            "Developer",
            "Sales Executive",
            "Manager",
            "Research Scientist",
            "Human Resources",
            "Data Scientist",
            "Other"
        ]
    )

with col2:
    business_travel = st.selectbox(
        "Business Travel Frequency",
        [
            "Travel_Rarely",
            "Travel_Frequently",
            "Non-Travel"
        ]
    )

    job_level = st.number_input(
        "Job Level",
        min_value=1,
        max_value=5,
        value=2
    )

    job_involvement = st.slider(
        "Job Involvement",
        1,
        4,
        3
    )

with col3:
    overtime = st.selectbox(
        "OverTime",
        ["No", "Yes"]
    )

    attrition = st.selectbox(
        "Attrition",
        ["No", "Yes"]
    )

    hourly_rate = st.number_input(
        "Hourly Rate",
        min_value=1,
        max_value=150,
        value=70
    )


# --------------------------------------------------
# Experience & Career Information
# --------------------------------------------------

st.header("📊 Experience & Career Information")

col1, col2, col3 = st.columns(3)

with col1:
    companies_worked = st.number_input(
        "Number of Companies Worked",
        min_value=0,
        max_value=20,
        value=2
    )

    salary_hike = st.number_input(
        "Last Salary Hike (%)",
        min_value=10,
        max_value=30,
        value=20
    )

    total_experience = st.number_input(
        "Total Work Experience (Years)",
        min_value=0,
        max_value=50,
        value=8
    )

with col2:
    training_times = st.number_input(
        "Training Times Last Year",
        min_value=0,
        max_value=10,
        value=3
    )

    work_life_balance = st.slider(
        "Work-Life Balance",
        1,
        4,
        3
    )

    experience_company = st.number_input(
        "Experience at Current Company (Years)",
        min_value=0,
        max_value=40,
        value=5
    )

with col3:
    current_role_experience = st.number_input(
        "Experience in Current Role (Years)",
        min_value=0,
        max_value=20,
        value=3
    )

    years_since_promotion = st.number_input(
        "Years Since Last Promotion",
        min_value=0,
        max_value=20,
        value=1
    )

    years_manager = st.number_input(
        "Years With Current Manager",
        min_value=0,
        max_value=20,
        value=2
    )


# --------------------------------------------------
# Prediction
# --------------------------------------------------

st.divider()

if st.button(
    "🔮 Predict Employee Performance",
    type="primary",
    use_container_width=True
):

    input_data = pd.DataFrame({
        "Age": [age],
        "Gender": [gender],
        "EducationBackground": [education_background],
        "MaritalStatus": [marital_status],
        "EmpDepartment": [department],
        "EmpJobRole": [job_role],
        "BusinessTravelFrequency": [business_travel],
        "DistanceFromHome": [distance_from_home],
        "EmpEducationLevel": [education_level],
        "EmpEnvironmentSatisfaction": [environment_satisfaction],
        "EmpHourlyRate": [hourly_rate],
        "EmpJobInvolvement": [job_involvement],
        "EmpJobLevel": [job_level],
        "EmpJobSatisfaction": [job_satisfaction],
        "NumCompaniesWorked": [companies_worked],
        "OverTime": [overtime],
        "EmpLastSalaryHikePercent": [salary_hike],
        "EmpRelationshipSatisfaction": [relationship_satisfaction],
        "TotalWorkExperienceInYears": [total_experience],
        "TrainingTimesLastYear": [training_times],
        "EmpWorkLifeBalance": [work_life_balance],
        "ExperienceYearsAtThisCompany": [experience_company],
        "ExperienceYearsInCurrentRole": [current_role_experience],
        "YearsSinceLastPromotion": [years_since_promotion],
        "YearsWithCurrManager": [years_manager],
        "Attrition": [attrition]
    })

    try:

        # Convert DataFrame to JSON-compatible dictionary
        employee_data = input_data.to_dict(
            orient="records"
        )[0]

        # Send employee data to FastAPI
        response = requests.post(
            API_URL,
            json=employee_data,
            timeout=60
        )

        # Raise an error if the API returns 4xx/5xx
        response.raise_for_status()

        # Read API response
        result = response.json()

        predicted_rating = int(
            result["predicted_performance_rating"]
        )

        # --------------------------------------------------
        # Display Prediction
        # --------------------------------------------------

        st.success("Prediction Completed Successfully!")

        st.subheader("🎯 Predicted Employee Performance")

        st.metric(
            label="Performance Rating",
            value=predicted_rating
        )

        if predicted_rating == 2:
            st.info("Performance Rating: 2")

        elif predicted_rating == 3:
            st.success("Performance Rating: 3")

        elif predicted_rating == 4:
            st.success("Performance Rating: 4")

    except requests.exceptions.RequestException as e:

        st.error(
            "Unable to connect to the Employee Performance API."
        )

        st.exception(e)

    except Exception as e:

        st.error("Unable to make prediction.")

        st.exception(e)