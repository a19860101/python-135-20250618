from PyQt6 import QtWidgets, QtGui
import sys

app = QtWidgets.QApplication(sys.argv)
w = QtWidgets.QWidget()
w.setWindowTitle('哈囉拍沈')
# w.resize(600,400)

w.setStyleSheet('font-size: 24px')

dollar_label = QtWidgets.QLabel(w)
dollar_input = QtWidgets.QLineEdit(w)
dollar_label_2 = QtWidgets.QLabel(w)
dollar_btn = QtWidgets.QPushButton(w)
dollar_sel = QtWidgets.QComboBox(w)
dollar_sel.addItems(['台幣換算日幣','日幣換算台幣'])
result = QtWidgets.QTextEdit(w)
dollar_label_2.setText('模式')
dollar_label.setText('金額')
dollar_btn.setText('換算')

grid = QtWidgets.QGridLayout(w)
grid.addWidget(dollar_label, 1, 1)
grid.addWidget(dollar_label_2,2,1)
grid.addWidget(dollar_input, 1, 2)
grid.addWidget(dollar_sel, 2, 2)
grid.addWidget(dollar_btn, 3, 1,1,2)
grid.addWidget(result, 4, 1,1,2)


def dollar():
    rate = 0.208
    if dollar_sel.currentText() == '台幣換算日幣':
        r = float(dollar_input.text()) / rate
        result.setText(f'換算匯率為{rate}\n台幣{dollar_input.text()}約為日幣{r:.2f}')
    else:
        r = float(dollar_input.text()) * rate
        result.setText(f'換算匯率為{rate}\n日幣{dollar_input.text()}約為台幣{r:.2f}')


dollar_btn.clicked.connect(dollar)

w.show()
sys.exit(app.exec())

# pyinstaller -F -w 檔案
# -F 打包成獨立執行檔（沒有_internal資料夾）
# -w 沒有終端機只有視窗