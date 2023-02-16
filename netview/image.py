from tkinter import Tk
root = Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.destroy()

import pygame
import numpy as np
from PIL import Image, ImageDraw

HORIZ_GAP = 20
VERT_GAP = 10

def generate_image(layers, dark_mode=False):
    # y = 414.222x - 462.222
    width = int(min((414.222 * len(layers) - 462.222), screen_width))
    # y = -12.0889x^2 + 241.778x - 58.8889
    max_neurons = max(layers)
    height = int(min(-12.0889 * max_neurons ** 2 + 241.778 * max_neurons - 58.8889, screen_height))
    if max_neurons > 9:
        height = screen_height

    bg_color = (0, 0, 0) if dark_mode else (255, 255, 255)
    image = Image.new('RGB', (width, height), bg_color)
    draw = ImageDraw.Draw(image)

    neuron_radius = 10
    x_gap = (width - HORIZ_GAP*2 - len(layers)*neuron_radius*2) / (len(layers)-1)
    curr_x = (width-(x_gap+neuron_radius*2)*len(layers)+x_gap)/2

    for l in layers:
        y_gap = min(100, (height - VERT_GAP*2 - l*neuron_radius*2) / (l-1))
        curr_y = (height-(y_gap+neuron_radius*2)*l+y_gap)/2
        for _ in range(l):
            draw.ellipse((curr_x, curr_y, curr_x+neuron_radius*2, curr_y+neuron_radius*2), fill=(0, 0, 0))
            curr_y += y_gap + neuron_radius*2
        curr_x += x_gap + neuron_radius*2

    image.show()

generate_image([2, 2, 2, 2])