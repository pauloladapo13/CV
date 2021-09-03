from PIL import Image
from pylab import *

# read image to array
im = array(Image.open('empire2.jpg'))

# plot the image
imshow(im)

# some points

x = [100, 100, 400, 400]
y = [200, 500, 200, 500]

# plot the points with red star-makers
plot(x, y, 'r*')

# Line plot connecting the first two points
plot(x[:2], y[:2])

# add title and show the plot
title('Plotting: "empire2.jpg" ')
axis('off')


# plot(x, y) default blue solid line
# plot(x, y, 'r*') red star-markers
# plot(x, y, 'go-') green line with circle-makers
# plot(x, y, 'ks:') black dotted line with square-makers

show()
