# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import bentoml
from bentoml.io import NumpyNdarray
import numpy as np


'''
newest model :mlzoomcamp_homework:jsi67fslz6txydu5
old model : mlzoomcamp_homework:qtzdz3slg6mwwdu5
'''

model_ref=bentoml.sklearn.get("mlzoomcamp_homework:qtzdz3slg6mwwdu5")

model_runner=model_ref.to_runner()

svc=bentoml.Service("mlzoomcamp_homework_service",runners=[model_runner])

@svc.api(input=NumpyNdarray(),output=NumpyNdarray())
# endpoint
def classify(data: np.ndarray) -> np.ndarray:
    prediction=model_runner.predict.run(data)
    # print(prediction)
    # return {"predicted value ":prediction}
    return prediction
