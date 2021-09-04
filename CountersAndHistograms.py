from PIL import Image
from pylab import *

# read image to array

im1 = array(Image.open('empire1.jpg').convert('L'))


# create a new figure
# dont use colors
# sin la función  gray() se muestra la imagen con destellos del verde al azul y un fondo blancopygame.examples.mask.main()
gray()
# show contours with origin upper left corner
contour(im1, origin='image')
axis('equal')
axis('off')

# the Histogram of the image is done using the hist() function

figure()
hist(im1.flatten(), 128)
show()
