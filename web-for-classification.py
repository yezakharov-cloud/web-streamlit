import io
import streamlit as st
from PIL import Image
import numpy as np
from tensorflow.keras.applications import EfficientNetB0
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.efficientnet import preprocess_input, decode_predictions


@st.cache(allow_output_mutation=True)
def load_model():
    return EfficientNetB0(weights='imagenet')


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

plt.imshow(img)
plt.show()

"""Выполняем предварительную обработку изображения"""

x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)

"""Запускаем распознавание"""

preds = model.predict(x)

"""Печатаем ТОП-3 класса с самой большой вероятностью"""

classes = decode_predictions(preds, top=3)[0]
for cl in classes:
    print(cl[1], cl[2])
