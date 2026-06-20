from PIL import Image
from pathlib import Path
import math

input_folder = Path("input")
normal_images = []
resized_images = []
grey_images = []
quantized_images = []

image_height = 100
chars = """ .:-=+*#%@"""
#chars = """.'`^",;:Il!i><~+_-?][}{1)(|\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MWM&%8@$"""

for image in input_folder.glob("*.png"):
    normal_images.append(Image.open(image))

for image in normal_images:
    aspect_ratio = image.width / image.height
    new_width = math.ceil(image_height * aspect_ratio * 1.85)
    resized_images.append(image.resize((new_width, image_height)))

for image in resized_images:
    grey_images.append(image.convert("L"))
    
for image in grey_images:
    quantized_images.append(image.quantize(colors=10).convert("L"))

i = 0
for image in quantized_images:
    pixels = image.load()
    lines = []
    for y in range(image.height):
        temp_string = ""
        for x in range(image.width):
            pixel = pixels[x,y]
            index = pixel * (len(chars) - 1) // 255
            char = chars[index]
            temp_string += char
        lines.append(temp_string)
    for line in lines:
        print(line)
    print("")
#python ASCII_generator.py