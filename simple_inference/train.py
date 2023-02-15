from sklearn.svm import SVC
from sklearn import metrics
from sklearn.model_selection import train_test_split
from fastapi import HTTPException
from joblib import dump
import pandas as pd
import datos
import os

def train(wine:str='wine'):
    if not os.path.isfile(wine+'.csv'):
            raise HTTPException(status_code=500, detail="Unkown dataset: "+ wine)
    df = pd.read_csv('wine.csv')
    df.columns = df.columns.str.replace(' ', '_')
    X = df.drop('quality', axis=1)
    y = df['quality']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)
    model = SVC()
    model.fit(X_train, y_train)
    expected_y  = y_test
    predicted_y = model.predict(X_test)
    model_metrics = metrics.classification_report(expected_y, predicted_y, output_dict=True,zero_division=1)
    dump(model, wine+'_model.joblib')
    return model_metrics