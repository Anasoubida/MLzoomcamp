# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 18:22:16 2022

@author: Anas
"""
import pickle
import os
from flask import Flask, request, jsonify


#### using the model and the dv of the course
# !wget https://raw.githubusercontent.com/alexeygrigorev/mlbookcamp-code/master/course-zoomcamp/cohorts/2022/05-deployment/homework/model1.bin
# !wget https://raw.githubusercontent.com/alexeygrigorev/mlbookcamp-code/master/course-zoomcamp/cohorts/2022/05-deployment/homework/dv.bin
# load the model from disk
filename = 'model1.bin'
loaded_model = pickle.load(open(filename, 'rb'))

filename = 'dv.bin'
loaded_dv=pickle.load(open(filename, 'rb'))

score_request={"reports": 0, "share": 0.001694, "expenditure": 0.12, "owner": "yes"}
def predict_single(request_data,loaded_dv,loaded_model):
   request_data=loaded_dv.transform(request_data) 
   result = loaded_model.predict_proba(request_data)[:,1]
   return result



app = Flask('churn')


@app.route('/predict', methods=['POST'])
def predict():
    customer = request.get_json()

    prediction = predict_single(customer, loaded_dv, loaded_model)
    churn = prediction >= 0.5
    
    result = {
        'churn_probability': float(prediction),
        'churn': bool(churn),
    }

    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)
