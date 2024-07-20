from fastapi import FastAPI,Query
from pydantic import BaseModel

class tahabasmodel(BaseModel):
    bmi:float
    message:str

app = FastAPI()
@app.get("/")
def read_root():
    return {"Hello": "World nnn"}

@app.get("/rockpaperscissors")
def rockpaperscissors(weight:float=Query(...,gt=20,lt=100,description="Weigh in Kelogrames")
                      , hight:float=Query(...,gt=20,lt=100,description="Hight in centemeters")):
    bmi=weight/(hight**2)
    if bmi<1:
        message = "your bmi less than 1, eat more"
    elif 1<=bmi<10:
        message = "your bmi less than 10 enta keda tmam"
    elif bmi>10:
        message = "your bmi more than 10, batal akl"

    return tahabasmodel(bmi=bmi, message= message)

