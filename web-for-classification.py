
import os
import time
import cv2
import sys
import csv
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import tensorflow as tf
import keras_preprocessing
import streamlit as st
import numpy as np
import pandas as pd
from numpy import argmax
from PIL import Image , ImageEnhance
from resizeimage import resizeimage
from utils import label_map_util
from utils import visualization_utils as vis_util
from keras.preprocessing import image
from keras_preprocessing.image import ImageDataGenerator
from pathlib import Path


import io
import streamlit as st
from PIL import Image

def load_image():
    uploaded_file = st.file_uploader(label='Оберіть зображення')
    if uploaded_file is not None:
        image_data = uploaded_file.getvalue()
        st.image(image_data)
        return Image.open(io.BytesIO(image_data))
    else:
        return None

st.title('Класифікація зображень')
img = load_image()
result = st.button('Розпізнати зображення')
