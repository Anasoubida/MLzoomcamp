#!/usr/bin/env python
# coding: utf-8

import numpy as np

import tflite_runtime.interpreter as tflite
from io import BytesIO
from urllib import request
from PIL import Image

def download_image(url):
    with request.urlopen(url) as resp:
        buffer = resp.read()
    stream = BytesIO(buffer)
    img = Image.open(stream)
    return img


def prepare_image(img, target_size):
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img = img.resize(target_size, Image.NEAREST)
    return img

# loading the model
def predict(url,model_path='dino_dragon_10_0.899.tflite'):
    img=download_image(url)
    img=prepare_image(img,(150,150))
    X=np.array(img)
    X=X/255
    X=np.array(X,dtype=np.float32)
    X=np.expand_dims(X, axis=0)
    interpreter = tflite.Interpreter(model_path=model_path)
    interpreter.allocate_tensors()
    input_index=interpreter.get_input_details()[0]["index"]
    output_index=interpreter.get_output_details()[0]["index"]
    
    interpreter.set_tensor(input_index, X)
    interpreter.invoke()
    preds = interpreter.get_tensor(output_index)
    if float(preds[0])>0.5:
        classe='Your image is dragon'
    else:
        classe='Your image is dino'
    return classe,float(preds[0])

def lambda_handler(event, context):
    url = event['url']
    result = predict(url)
    return result
