from PyQt6 import QtWidgets
from PIL import Image
import sys, os, time, uuid

app = QtWidgets.QApplication(sys.argv)
w = QtWidgets.QWidget()
w.setWindowTitle('縮圖小城市')
# w.resize(600,400)
w.setStyleSheet('font-size:20px')

file_path = None

btn = QtWidgets.QPushButton(w)
btn.setText('選擇檔案')

label_width = QtWidgets.QLabel(w)
label_width.setText('請輸入縮圖寬度')
input_width = QtWidgets.QLineEdit(w)

label_quality = QtWidgets.QLabel(w)
label_quality.setText('請輸入縮圖品質(0-100)')
input_quality = QtWidgets.QLineEdit(w)

label_msg = QtWidgets.QLabel(w)
input_msg = QtWidgets.QTextEdit(w)

submit = QtWidgets.QPushButton(w)
submit.setText('執行')

grid = QtWidgets.QGridLayout(w)
grid.addWidget(label_width,1,1)
grid.addWidget(input_width,1,2)
grid.addWidget(label_quality,2,1)
grid.addWidget(input_quality,2,2)
grid.addWidget(btn,3,1)
grid.addWidget(submit, 4,1, 1,2)
grid.addWidget(input_msg, 5,1, 1,2)

def getfile():
    data, _ = QtWidgets.QFileDialog.getOpenFileNames(filter='圖片檔案(*.jpg *.jpeg *.gif *.png *.webp)')

    global file_path
    file_path = data


def image_resize(path):

    for idx,img in enumerate(path):
        try:
            ta = Image.open(img)
            w,h = ta.size

            resize_w = int(input_width.text())
            resize_h = int(h * resize_w / w)

            quality = int(input_quality.text())

            small_ta = ta.resize((resize_w, resize_h))
            os.makedirs('output', exist_ok=True)

            # 打包前路徑
            path = os.path.dirname(os.path.abspath(__file__))
            # path = os.path.dirname(__file__)

            # 打包後路徑
            # path = os.path.dirname(os.path.realpath(sys.executable))
            # print(path)


            # 副檔名
            _, ext = os.path.splitext(img)
            print(ext)

            # 取得檔名
            # img_name = os.path.basename(img)
            # 產生隨機檔名
            # img_name = uuid.uuid4()
            img_name = str(int(time.time()*1000))
            print(img_name)

            # small_ta.save(f'{path}/output/{img_name}',quality=quality)
            small_ta.save(f'{path}/output/{img_name}{ext}',quality=quality)
        except Exception as e:
            print(e)


def active():
    input_msg.setText('處理中')
    image_resize(file_path)
    input_msg.setText('完成')
    # print(file_path)

btn.clicked.connect(getfile)
submit.clicked.connect(active)

w.show()
sys.exit(app.exec())