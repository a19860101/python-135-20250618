# import PIL
from PIL import Image
import glob
import os

imgs = glob.glob('./images/*.[jJ][pP][gG]') + glob.glob('./images/*.[pP][nN][gG]')

for idx,Img in enumerate(imgs):
    print(Img[9:])
    # print(idx)
    try:
        img = Image.open(imgs[idx])
        os.makedirs('thumbnail', exist_ok=False)
        # img.save(f'thumbnail/qqq-{idx}.jpg', quality=1, subsampling=0)
        img.save(f'thumbnail/small-{Img[9:]}', quality=1, subsampling=0)
    except IndexError as e:
        print(f'發生錯誤:{e}')
    except FileExistsError as e:
        print(f'發生錯誤:{e}')
