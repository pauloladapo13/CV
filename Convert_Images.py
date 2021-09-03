from PIL import Image

with Image.open('empire1.jpg') as im:

    im.convert('L').show()
