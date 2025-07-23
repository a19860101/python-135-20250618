import glob
from PIL import Image, ImageEnhance

imgs = glob.glob('./images/willian-justen-de-vasconcellos-_QmHXJSAI4Q-unsplash.jpg')

print(imgs)
img = Image.open(imgs[0])

# 亮度
brightness = ImageEnhance.Brightness(img)

# 對比
contrast = ImageEnhance.Contrast(img)

# 飽和度
color = ImageEnhance.Color(img)

# img = brightness.enhance(0.5)
# img = contrast.enhance(0.2)
img = color.enhance(0)

img.show()