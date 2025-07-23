import glob
from PIL import Image, ImageDraw, ImageFont

imgs = glob.glob('./images/marek-piwnicki-kgFdZvtyW4E-unsplash.jpg')
img =Image.open(imgs[0])

# img = Image.open('./images/marek-piwnicki-kgFdZvtyW4E-unsplash.jpg')

draw = ImageDraw.Draw(img)

w,h = img.size

# 畫直線
# draw.line([(0,0),(200,800)],fill='red',width=10)

draw.line([(0,0),(w,h)],fill='red',width=10)
draw.line([(w,0),(0,h)],fill='blue',width=10)

# 矩形
draw.rectangle([(100,100),(800,600)],fill='pink', outline='greenyellow', width=60)

# 圓形
draw.circle((1000,1000),radius=600, fill='orange', outline='white', width=100)
draw.circle((w/2,h/2),radius=600, fill='orange', outline='white', width=100)

# 多邊形
draw.polygon([(234,462),(987,342),(564,234),(971,123),(1200,600)],outline='red',width=50)


img.show()

