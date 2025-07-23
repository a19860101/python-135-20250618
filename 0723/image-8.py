import glob
from PIL import Image, ImageDraw, ImageFont

imgs = glob.glob('./images/marek-piwnicki-kgFdZvtyW4E-unsplash.jpg')
img =Image.open(imgs[0])

draw = ImageDraw.Draw(img)
w,h = img.size
font = ImageFont.truetype('Huninn-Regular.ttf', 200)
text = '聯成電腦'

t,l,r,b = draw.textbbox((0,0),text,font=font)
print(t,l,r,b)

q = draw.textlength(text,font=font)
print(q)

draw.text((w-r-50,h-b-50),text,font=font, fill='red')
draw.text((w-r-50,0),text,font=font, fill='red')

img.show()



