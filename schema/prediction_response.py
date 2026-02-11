from pydantic import BaseModel , Field
from typing import Dict

class PredictionResponse(BaseModel):
    predicted_category :str = Field(
        ...,
        description="The predicted insurance premium category",
        example = "High"

    )

    confidence :str = Field(
        ...,
        description=" Models Confidence Score for the predicted class range 0 to 1",
        example = 0.8423
        
    )

    class_probabilities :Dict[str,float] = Field(
        ...,
        description="Probabilities distribution across all possible classes",
        example = {"low":0.01,"Medium":0.15,"High":0.84}
        
    )