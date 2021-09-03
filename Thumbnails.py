from PIL import Image

with Image.open('empire2.jpg') as im:
    im.thumbnail((128, 128))

im.show()
