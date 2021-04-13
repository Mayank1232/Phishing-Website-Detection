# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 15:37:09 2021

@author: hp
"""

import uvicorn
from fastapi import FastAPI
import joblib,os

app = FastAPI()

phish_model = open('phish.pkl','rb')
phish_model_ls = joblib.load(phish_model)

@app.get('/predict/{feature}')
async def predict(features):
    x_predict = []
    x_predict.append(str(features))
    y_predict = phish_model_ls.predict(x_predict)
    if y_predict == 'bad':
        result = "This is a phishing site"
    else:
        result = "This is not a Phishing Site"
        
    return(features,result)

if __name__ == '__main__':
    uvicorn.run(app,host='127.0.0.1',port=8000)