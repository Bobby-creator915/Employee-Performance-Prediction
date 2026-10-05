# 👨‍💼 Employee Performance Prediction System

A Machine Learning application that predicts an employee's performance rating based on employee, job, satisfaction, experience, and career-related information.

The project uses a trained Scikit-learn machine learning pipeline, a FastAPI backend, and a Streamlit frontend.

---

## 🚀 Live Demo

### Streamlit Application

https://employee-performance-prediction-sg7pwkwen9wbkpvi7lnbgn.streamlit.app/

### FastAPI Backend

https://employee-performance-prediction-ou48.onrender.com

---

## 🎯 Project Objective

The objective of this project is to build a Machine Learning system that can predict an employee's performance rating.

The system accepts employee information through an interactive web application and sends the information to a FastAPI backend, where the trained Machine Learning model generates the prediction.

---

## 🧠 Machine Learning

### Target Variable

`PerformanceRating`

The model predicts employee performance ratings such as:

- `2` — Needs Improvement
- `3` — Meets Expectations
- `4` — Exceeds Expectations

### Dataset

- 1,200 employee records
- 28 original columns
- Employee demographic, job, satisfaction, experience, and career-related features

---

## 📊 Features Used

The deployed model uses the following features:

1. Age
2. Gender
3. EducationBackground
4. MaritalStatus
5. EmpDepartment
6. EmpJobRole
7. BusinessTravelFrequency
8. DistanceFromHome
9. EmpEducationLevel
10. EmpEnvironmentSatisfaction
11. EmpHourlyRate
12. EmpJobInvolvement
13. EmpJobLevel
14. EmpJobSatisfaction
15. NumCompaniesWorked
16. OverTime
17. EmpLastSalaryHikePercent
18. EmpRelationshipSatisfaction
19. TotalWorkExperienceInYears
20. TrainingTimesLastYear
21. EmpWorkLifeBalance
22. ExperienceYearsAtThisCompany
23. ExperienceYearsInCurrentRole
24. YearsSinceLastPromotion
25. YearsWithCurrManager
26. Attrition

---

## 🏗️ System Architecture

The project follows this architecture:

User
↓
Streamlit Frontend
↓
FastAPI Backend
↓
Scikit-learn Machine Learning Pipeline
↓
Performance Rating Prediction

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- FastAPI
- Uvicorn
- Streamlit
- Requests
- Git & GitHub
- Render

---

## 📁 Project Structure

```text
Employee-Performance-Prediction/
│
├── model/
│   └── INX_employee_performance_model.pkl
│
├── app.py
├── api.py
├── requirements.txt
├── runtime.txt
├── README.md
└── .gitignore