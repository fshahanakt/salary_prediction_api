from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.schemas import SalaryRequest, SalaryResponse
import pandas as pd
import joblib

app = FastAPI()

model = joblib.load("app/model/salary_prediction_model.pkl")

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


@app.post("/predict", response_model=SalaryResponse)
async def predict_salary(request: SalaryRequest):

    input_data = pd.DataFrame({
        "YearsExperience": [request.years_experience]
    })

    prediction = model.predict(input_data)

    return SalaryResponse(
        predicted_salary=float(prediction[0])
    )