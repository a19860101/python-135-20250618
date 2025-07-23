import glob
from PIL import Image, ImageDraw, ImageFont

imgs = glob.glob('./images/marek-piwnicki-kgFdZvtyW4E-unsplash.jpg')
img =Image.open(imgs[0])

font = ImageFont.truetype('Huninn-Regular.ttf', 150)

draw = ImageDraw.Draw(img)

w, h = img.size
# draw.text((0,0), '聯成電腦', font_size=150)
# draw.text((w/2,h/2), '聯成電腦', font=font)
draw.text((w/2,h/2), '聯成電腦', font=font, fill='red')

img.show()

