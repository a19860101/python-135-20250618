from PyQt6 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
w = QtWidgets.QWidget()
w.setWindowTitle('哈囉拍沈')
w.resize(600,400)
# 設定視窗樣式
w.setStyleSheet('background: #ccc; font-size:24px; font-weight: bold')

label = QtWidgets.QLabel(w)
label.move(100,20)
label.setText('我是文字')

#設定label樣式
label.setStyleSheet('color:red;')

label2 = QtWidgets.QLabel(w)
label2.move(100,50)
label2.setText('hello')

# label2.setStyleSheet('font-size: 30px; color:blue; background: pink; font-weight: bold; font-style: italic')

w.show()
sys.exit(app.exec())