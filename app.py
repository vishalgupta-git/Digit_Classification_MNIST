import streamlit as st
import numpy as np
from streamlit_drawable_canvas import st_canvas
from tensorflow.keras.models import load_model 
from PIL import Image
import io

model = load_model('bin/model.keras')  

def preprocess_image(image_data):
    img = Image.fromarray(image_data.astype(np.uint8))  
    img = img.convert('L') 
    img = img.resize((28, 28))  
    img = np.array(img)  
    img = 255 - img  
    img = img / 255.0  
    img = img.reshape(1, 28, 28, 1) 
    
    return img

st.title("Draw a Digit for Prediction")

canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 1)",  
    stroke_width=3,
    stroke_color="#000000",
    background_color="#eee",
    height=300,
    width=300,
    drawing_mode="freedraw",
    key="canvas",
)

if st.button('Predict Digit'):
    if canvas_result.image_data is not None:
        img = preprocess_image(canvas_result.image_data)
        prediction = model.predict(img)
        predicted_digit = np.argmax(prediction)
        st.write(f"Predicted Digit: {predicted_digit}")
    else:
        st.warning("Please draw a digit on the canvas first!")


