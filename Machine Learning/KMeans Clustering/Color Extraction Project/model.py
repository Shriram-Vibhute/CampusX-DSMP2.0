import pandas as pd
import matplotlib
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from PIL import Image, ImageDraw
import numpy as np
import webcolors

def create_color_palette(dominant_colors, palette_size=(300, 50)):
    # Create an image to display the colors
    palette = Image.new("RGB", palette_size)
    draw = ImageDraw.Draw(palette)

    # Calculate the width of each color swatch
    swatch_width = palette_size[0] // len(dominant_colors)

    # Draw each color as a rectangle on the palette
    for i, color in enumerate(dominant_colors):
        draw.rectangle([i * swatch_width, 0, (i + 1) * swatch_width, palette_size[1]], fill=tuple(color))

    return palette

def fetch_colours(image):
    image = image.reshape(-1, 3)

    model = KMeans(n_clusters = 5)
    model.fit(image)

    return create_color_palette(model.cluster_centers_.astype(int))