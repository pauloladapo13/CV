from PIL import Image
import os

filelist = ''

for infile in filelist:
    outfile = os.path.splitext(infile)[0] + 'JPEG'
    if infile != outfile:
        try:
            with Image.open(infile).save(outfile) as newim:
                newim.rotate(0).show()
        except IOError:

            print('cannot convert', infile)
