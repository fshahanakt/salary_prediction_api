from pydantic import BaseModel

class SalaryRequest(BaseModel):
    years_experience: float

class SalaryResponse(BaseModel):
    predicted_salary: float