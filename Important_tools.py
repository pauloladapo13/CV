from PIL import Image

# Resize and two sorts of rotation
box = (50, 50, 400, 400)

# with Image.open('empire2.jpg') as im1:

#     im1.rotate(0)
#     im1.resize((100, 100))
#     im1.show()

# Copy, cut and paste a region of an image

with Image.open('empire2.jpg') as im2:

    region = im2.crop(box)
    region = region.transpose(Image.ROTATE_180)
    im2.paste(region, box)
    im2.show()
