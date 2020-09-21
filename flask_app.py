    #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 00:14:59 2020

@author: thunderbolt
"""


import pickle
import pandas as pd
from flask import Flask, request

app = Flask(__name__)

pickle_in = open("classifier.pkl", 'rb')
classifier = pickle.load(pickle_in)

@app.route('/')
def Welcome():
    return "Welcome Sir!"

@app.route('/predict')
def predict_note_authentication():
    variance=request.args.get('variance')
    skewness=request.args.get('skewness')
    curtosis=request.args.get('curtosis')
    entropy=request.args.get('entropy')
    prediction = classifier.predict([[variance,skewness,curtosis,entropy]])
    
    return "Predicted value is"+str(prediction)

@app.route('/predict_file', methods=["POST"])
def predict_note_file():
    df_test = pd.read_csv(request.args.get("file"))
    prediction=classifier.predict(df_test)
    return "Predicted value is"+str(list(prediction))

if __name__=='__main__':
    app.run(host='0.0.0.0')