import glob
from PIL import Image

imgs = glob.glob('./images/marek-piwnicki-kgFdZvtyW4E-unsplash.jpg')
img =Image.open(imgs[0])

# img_rotate = img.rotate(45,expand=1)
#
# img_rotate.show()

img = img.transpose(Image.FLIP_LEFT_RIGHT)
# img = img.transpose(Image.FLIP_TOP_BOTTOM)
# img = img.transpose(Image.ROTATE_90)
# img = img.transpose(Image.ROTATE_180)
# img = img.transpose(Image.ROTATE_270)

img.show()

