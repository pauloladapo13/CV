from PIL import Image
from pylab import *

im = array(Image.open('empire2.jpg'))

print(im.shape, im.dtype)

im = array(Image.open('empire2.jpg').convert('L'), 'f')
print(im.shape, im.dtype)

# im[i,:] = im[j,:] set the values of row i with values from row j.
