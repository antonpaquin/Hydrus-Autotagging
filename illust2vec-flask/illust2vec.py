from keras.models import load_model
from keras import backend as K
import numpy as np
from PIL import Image

input_size = 224

class NeuralNetworkTagger:
    def __init__(self, tag_list, weight_file_path):
        K.clear_session()
        self.model = load_model(weight_file_path)
        self.model._make_predict_function()
        self.tag_list = tag_list

    def classify(self, pil_img):
        resize_ratio = input_size / max(pil_img.size)
        size = [int(x*resize_ratio) for x in pil_img.size]
        resized_img = pil_img.resize(size, Image.BILINEAR)
        img = Image.new('RGB', (input_size, input_size))
        img.paste(resized_img, ((input_size-size[0])//2, (input_size-size[1]//2)))
        data = np.asarray(img).reshape((1, input_size, input_size, 3))
        predict = self.model.predict(data).reshape(len(self.tag_list))
        return dict(zip(self.tag_list, predict))
