
from fastapi import FastAPI
from fastapi.responses import JSONResponse

from typing import Literal , Annotated
from schema.user_input import UserInput
from model.predict import predict_output,MODEL_VERSION
from schema.prediction_response import PredictionResponse



app = FastAPI()

      
# human readable
@app.get('/')
def home():
    return {'message':'Insurance Premium Prediction API'}


#Machine Readable
@app.get('/health')
def health_check():
    return {
        'status':'Ok',
        'version': MODEL_VERSION
    }
    



            
# In prediction we use POST URL 


@app.post('/predict',response_model=PredictionResponse)   ## here response_model handles the output the validation from end poin automatically with PredictionResponse Pydantic Model
def predict_premium(data: UserInput):
    user_input = {
        ## These are the input feilds for our model for prediction thats why converting into Dataframe

        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation

    }

    try:

        prediction = predict_output(user_input)

        return JSONResponse(status_code=200, content={'predicted_category': prediction})
    except Exception as e :
        return JSONResponse(status_code=500,content=str(e))

    

        
    