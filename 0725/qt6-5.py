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

btn = QtWidgets.QPushButton(w)
btn.setGeometry(400,300,150,30)
btn.setText('執行')

sel = QtWidgets.QComboBox(w)
# sel.addItem('test 1')
# sel.addItem('test 2')
sel.addItems(['one','two','three','four'])


sel.move(200,200)

textarea = QtWidgets.QTextEdit(w)
textarea.setGeometry(10,300,300,50)

def test():
    textarea.setText('hellohello')

btn.clicked.connect(test)

w.show()
sys.exit(app.exec())