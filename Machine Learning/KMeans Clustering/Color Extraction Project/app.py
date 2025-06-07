import streamlit as st
from PIL import Image
import matplotlib
import matplotlib.pyplot as plt
from model import fetch_colours  # Changed from .model to model

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # Read the uploaded image file
    image = matplotlib.image.imread(uploaded_file)
    st.image(image, caption='Uploaded Image', use_container_width=True)

    top_colours = fetch_colours(image)
    st.image(top_colours, caption='Top 5 Colours', use_container_width=True)