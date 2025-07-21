# import PIL
from PIL import Image
import glob
import os

# jpg, jpeg, gif, png, webp, tiff, bmp,

# 多重副檔名時，使用+把所有型態加起來
imgs = glob.glob('./images/*.[jJ][pP][gG]') + glob.glob('./images/*.[pP][nN][gG]')


try:
    img = Image.open(imgs[0])
    # print(img)
    os.makedirs('thumbnail', exist_ok=True)
    # exist_ok=True 若檔案存在，繼續執行

    img.save('thumbnail/qqq.jpg', quality=70, subsampling=0)
    # quality 1-100, subsampling 0,1,2
except IndexError:
    print('IndexError')
except FileExistsError:
    print('當檔案已存在時，無法建立該檔案')