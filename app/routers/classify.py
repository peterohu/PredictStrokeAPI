from fastapi import APIRouter, Request
from typing import Optional

from ..modules.KNN import predict_data

import time

router = APIRouter()

@router.get("/predict", tags = ["predict"])
def check_predict(gender: int = 0, age: int = 0, hypertenstion: int = 0, heart_disease: int = 0,ever_marries: int = 0, Residence_type: int = 0, avg_glucose_level: int = 0, bmi: int = 0, work_type_Govt_job: int = 0, work_type_Never_worked: int = 0, work_type_Private: int = 0, work_type_Self_employed: int = 0, work_type_children: int = 0, smoking_status_Unknown: int = 0, smoking_status_formerly_smoked: int = 0, smoking_status_never_smoked: int = 0, smoking_status_smokes: int = 0):
    start_time = time.time()
    try:
        
        if (gender or age or hypertenstion or heart_disease or ever_marries or Residence_type or avg_glucose_level or bmi or work_type_Govt_job or work_type_Never_worked or work_type_Private or work_type_Self_employed or work_type_children or smoking_status_Unknown or smoking_status_formerly_smoked or smoking_status_never_smoked or smoking_status_smokes):
            data = [gender, age, hypertenstion, heart_disease,ever_marries, Residence_type, avg_glucose_level, bmi, work_type_Govt_job, work_type_Never_worked, work_type_Private, work_type_Self_employed, work_type_children, smoking_status_Unknown, smoking_status_formerly_smoked, smoking_status_never_smoked, smoking_status_smokes]

            clasify = predict_data(data)
            # clasify = predict_data(data)

            if clasify:
                result = { "Predict_class:": int (clasify[0]),
                            "Status": "Success" }

            else:
                result = { "Status" : "Error" }
        else:
            result =  { "Status" : "Error",
                        "Message" : "Invalid get parameters" }
    except:
        result =  { "Status" : "Error",
                    "Message" : "Something went wrong" } 
    finally:
        end_time = time.time()
        result["Respone_time"] = end_time - start_time
        return result


