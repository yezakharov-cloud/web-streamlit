"altair>=3.2.0",
"blinker>=1.0.0",
"cachetools>=4.0",
"click>=7.0",
# 1.4 introduced the functionality found in python 3.8's importlib.metadata module
"importlib-metadata>=1.4",
"numpy",
"packaging>=14.1",
"pandas>=0.21.0",
"pillow>=6.2.0",
"protobuf<4,>=3.12",
"pyarrow>=4.0",
"pympler>=0.9",
"python-dateutil",
"requests>=2.4",
"rich>=10.11.0",
"semver",
"toml",
"typing-extensions>=3.10.0.0",
"tzlocal>=1.1",
"validators>=0.2",





import io
import streamlit as st
from PIL import Image

import tensorflow_probability as tfp


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
