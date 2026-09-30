from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

app = FastAPI(
    title="Employee Performance Prediction API",
    description="API for predicting employee performance ratings",
    version="1.0"
)

MODEL_PATH = "model/INX_employee_performance_model.pkl"

model = joblib.load(MODEL_PATH)


class EmployeeData(BaseModel):
    Age: int
    Gender: str
    EducationBackground: str
    MaritalStatus: str
    EmpDepartment: str
    EmpJobRole: str
    BusinessTravelFrequency: str
    DistanceFromHome: int
    EmpEducationLevel: int
    EmpEnvironmentSatisfaction: int
    EmpHourlyRate: int
    EmpJobInvolvement: int
    EmpJobLevel: int
    EmpJobSatisfaction: int
    NumCompaniesWorked: int
    OverTime: str
    EmpLastSalaryHikePercent: int
    EmpRelationshipSatisfaction: int
    TotalWorkExperienceInYears: int
    TrainingTimesLastYear: int
    EmpWorkLifeBalance: int
    ExperienceYearsAtThisCompany: int
    ExperienceYearsInCurrentRole: int
    YearsSinceLastPromotion: int
    YearsWithCurrManager: int
    Attrition: str


@app.get("/")
def home():
    return {
        "message": "Employee Performance Prediction API is running"
    }


@app.post("/predict")
def predict_performance(employee: EmployeeData):

    input_data = pd.DataFrame([employee.model_dump()])

    prediction = model.predict(input_data)[0]

    return {
        "predicted_performance_rating": int(prediction)
    }