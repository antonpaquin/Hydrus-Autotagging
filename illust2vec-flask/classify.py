from keras.models import load_model
from keras import backend as K
import numpy as np
import json

K.clear_session()

model = load_model('illust2vec.h5')
model._make_predict_function()

with open('tag_list.json') as in_f:
    tag_list = json.load(in_f)

def classify(image, threshold):
    img_data = image.reshape((1, 224, 224, 3))

    predict = model.predict(img_data).reshape(len(tag_list))

    res = []
    for score, tag in zip(predict, tag_list):
        if score >= threshold:
            res.append(tag)
    return res
