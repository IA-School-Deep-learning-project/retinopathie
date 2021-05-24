import time
start = time.time()
from flask import Flask, render_template
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

AUTOTUNE = tf.data.experimental.AUTOTUNE
LABELS = ["No DR", "Mild", "Moderate", "Severe", "Proliferative DR"]
BATCH_SIZE = 8
IMAGE_SIZE = [320, 320]

def predict(image_path):
    d = dict()
    model = tf.keras.models.load_model("model.h5")
    image = list(tf.data.Dataset.list_files(image_path))
    def decode_img(image):
        image = tf.image.decode_png(image, channels=3)
        image = tf.image.convert_image_dtype(image, tf.float32)
        return tf.image.resize(image, IMAGE_SIZE)

    def preprocess(image):
        image = tf.io.read_file(image)
        image = decode_img(image)
        return image
    ds = tf.data.Dataset.from_tensor_slices(image)
    ds = ds.map(preprocess, num_parallel_calls=AUTOTUNE)
    ds = ds.batch(BATCH_SIZE)

    prediction = model.predict(ds)
    
    number = str(round(100 * prediction[0][np.argmax(prediction[0])], 2))
    predicted_label = f"This image is {number}% {LABELS[np.argmax(prediction)]}"
    
    d['predicted_label'] = predicted_label
    d['prediction'] = prediction
    return d

def plot_schema(prediction, predicted_label):
    plt.subplot(1, 1, 1)
    plt.title(predicted_label)
    plt.bar(np.arange(len(prediction[0])), prediction[0])
    plt.xlabel("DR Severity Grade")
    plt.ylabel("Model Score")
    #plt.show()
    plt.savefig('static/images/plot.png')
    return '/static/images/plot.png'