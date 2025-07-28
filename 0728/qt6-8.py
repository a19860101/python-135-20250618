from PyQt6 import QtWidgets, QtGui
import sys

app = QtWidgets.QApplication(sys.argv)
w = QtWidgets.QWidget()
w.setWindowTitle('哈囉拍沈')
w.resize(600,400)

def getfile():
    # 單一檔案
    # result = QtWidgets.QFileDialog.getOpenFileName()
    # 多檔案
    data, ftype = QtWidgets.QFileDialog.getOpenFileNames(filter='JPG(*.jpg);;GIF(*.gif);;PNG(*.png)')
    print(data, ftype)

btn = QtWidgets.QPushButton(w)
btn.move(100,100)
btn.setText('選擇檔案')

btn.clicked.connect(getfile)


w.show()
sys.exit(app.exec())
