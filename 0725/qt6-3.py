from PyQt6 import QtWidgets, QtGui
import sys

app = QtWidgets.QApplication(sys.argv)
w = QtWidgets.QWidget()
w.setWindowTitle('哈囉拍沈')
w.resize(600,400)
w.setStyleSheet('color: pink')

# 定義樣式
font = QtGui.QFont()
font.setBold(True)
font.setItalic(True)
font.setFamily('標楷體')
font.setUnderline(True)
font.setPointSize(20)
# font.setCapitalization('uppercase')
font.setOverline(True)


label = QtWidgets.QLabel(w)
label.move(100,20)
label.setText('我是文字')
label.setFont(font)

label2 = QtWidgets.QLabel(w)
label2.move(100,50)
label2.setText('hello')
label2.setFont(font)


w.show()
sys.exit(app.exec())