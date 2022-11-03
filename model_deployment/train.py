# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 17:11:12 2022

@author: Anas
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression, Ridge
from sklearn.metrics import recall_score, precision_score, roc_auc_score
import os
from sklearn.feature_extraction import DictVectorizer
import pickle

os.chdir("data")
df=pd.read_csv("evaluation metrics/AER_credit_card_data.csv")

features = ['reports', 'share', 'expenditure', 'owner']
dicts = df[features].to_dict(orient='records')
card_values = {
    "yes": 1,
    "no": 0
}
df["card"] = df.card.map(card_values)
##### the DictVectorizer will order on the alphabetic order the features
dv = DictVectorizer(sparse=False)
X = dv.fit_transform(dicts)
y=df["card"]

# here we can see the feature names
dv.get_feature_names()

model = LogisticRegression(solver='liblinear').fit(X, y)

try :
    os.mkdir("model_deployment")
except :
    print("le dossier est déja crée")

os.chdir("model_deployment")   

#### save the model and the dictvectorizer
# save the model to disk
filename = 'model1.bin'
pickle.dump(model, open(filename, 'wb'))

filename = 'dv.bin'
pickle.dump(dv, open(filename, 'wb'))







