import os
import main
from fastapi import HTTPException
import pandas as pd
from joblib import load

def modelo(wine, model):
    if not os.path.isfile(model+'_model.joblib'):
            raise HTTPException(status_code=500, detail="Unkown model: "+ model+" Try to train model first.")
    model_loaded = load(model+'_model.joblib')
    return int(model_loaded.predict(pd.DataFrame([wine.dict()]))[0])