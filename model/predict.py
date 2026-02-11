import pickle
import pandas as pd

with open('model/model.pkl','rb') as f:

    model = pickle.load(f)


MODEL_VERSION = "1.0.0"


# Getting class labels from model(importing for mathcing probabilities to class names)

class_labels = model.classes_.tolist()


def predict_output(user_input:dict):
    input_df = pd.DataFrame([user_input])

    #Predict the class
    predicted_class = model.predict(input_df)[0]

    #Get Probabilities for all classes
    
    probabilities = model.predict_proba(input_df)[0]
    confidence = max(probabilities)

    # create mapping : {classs_name: probabilities}
    class_prob = dict(zip(class_labels,map(lambda p: round(p,4), probabilities)))

    return {
        "preidcted_category": predicted_class,
        "confidence": round(confidence,4),
        "class_probabilities":class_prob
    }