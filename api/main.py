from DataModel import DataModel
import joblib
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
   return {"Hello": "World"}

@app.post("/predict")
def make_predictions(dataModel: DataModel):
   data = [dataModel.text]
   model = joblib.load('assets/BayesCount.joblib')
   result = model.predict(data)
   retorno = {"stars": int(result[0])}
   print(retorno)
   return retorno