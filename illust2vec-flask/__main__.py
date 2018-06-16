import json
from io import BytesIO
from flask import Flask, request
from PIL import Image
import numpy as np
import os

from classify import classify

#from dynamic_loader import load_with_dependencies

#classify = load_with_dependencies(os.getcwd() + '/model/classify', ['classify'])[0]

app = Flask(__name__)

@app.route('/', methods=['POST'])
def main():
    try:
        threshold = float(request.form.get('threshold'))
        img_bytes = BytesIO(request.files.get('img').read())
    except Exception:
        return 'bad request', 400

    try:
        img = Image.open(img_bytes).resize((224, 224))
        img_numpy = np.asarray(img.getdata()).astype('uint8')
    
        if img_numpy.size == 224*224*1:
            img_numpy = np.array([img_numpy] * 3)
        elif img_numpy.size == 224*224*4:
            img_numpy = img_numpy.reshape((224, 224, 4))[:,:,:3]
            img_numpy = img_numpy[:,:,:3]

    except IOError:
        return 'bad image', 400

    results = classify(img_numpy, threshold)

    resp = '\n'.join(['<tag>{}</tag>'.format(tag) for tag in results])

    return resp

'/home/anton/Media/pictures-anime/1515074923532.png'

if __name__ == '__main__':
    app.run('127.0.0.1', port=8119)
