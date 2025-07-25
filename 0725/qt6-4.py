from PyQt6 import QtWidgets, QtGui
import sys

app = QtWidgets.QApplication(sys.argv)
w = QtWidgets.QWidget()
w.setWindowTitle('哈囉拍沈')
w.resize(600,400)

# 定義樣式
font = QtGui.QFont()
font.setBold(True)
font.setPointSize(20)


label = QtWidgets.QLabel(w)
label.move(100,20)
label.setText('我是文字')
label.setFont(font)

label_input = QtWidgets.QLineEdit(w)
# label_input.move(300,20)
label_input.setGeometry(100,100,150,30)
# setGeometry(水平偏移,垂直偏移,寬度,高度)

btn = QtWidgets.QPushButton(w)
btn.setGeometry(400,300,150,30)
btn.setText('執行')

sel = QtWidgets.QComboBox(w)
# sel.addItem('test 1')
# sel.addItem('test 2')
sel.addItems(['one','two','three','four'])


sel.move(200,200)

textarea = QtWidgets.QTextEdit(w)
textarea.setGeometry(10,300,300,100)

w.show()
sys.exit(app.exec())