# import PIL
from PIL import Image
import glob
import os

imgs = glob.glob('./images/*.[jJ][pP][gG]') + glob.glob('./images/*.[pP][nN][gG]')

for idx,img in enumerate(imgs):
    ta = Image.open(img)

    w,h = ta.size

    resize_w = 600
    resize_h = int(h * resize_w / w)

    small_ta = ta.resize((resize_w, resize_h))

    os.makedirs('small', exist_ok=True)

    small_ta.save(f'small/small-{img[9:]}',quality=75)


