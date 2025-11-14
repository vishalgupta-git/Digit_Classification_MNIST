import streamlit as st
from streamlit_drawable_canvas import st_canvas

st.title("🎨 Drawable Canvas Example")

# Specify canvas parameters
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",  # fixed fill color with opacity
    stroke_width=3,
    stroke_color="#000000",
    background_color="#eee",
    height=300,
    width=400,
    drawing_mode="freedraw",
    key="canvas",
)

# Access the drawn image as a NumPy array
if canvas_result.image_data is not None:
    st.image(canvas_result.image_data)

# Get drawn shapes data
if canvas_result.json_data is not None:
    st.json(canvas_result.json_data)
