from keras.preprocessing import image
import keras
from tensorflow.keras.models import load_model

def extract(path):
    """
    input: path to image
    output: list of class probabilities
    classes garbage potholes straydogs st
    """
    model_tf = load_model('my_model')
    img=image.load_img(path, target_size=(150, 150))
    x=image.img_to_array(img)
    x=np.expand_dims(x, axis=0)
    images = np.vstack([x])
    classes = model_tf.predict(images)
    return classes

"""
Eg -
o/p - [[1.4536333e-04 9.9946112e-05 5.1276904e-01 4.0461946e-01 8.2366183e-02]]
"""
