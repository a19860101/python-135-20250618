from PyQt6 import QtWidgets
import sys

# 建立應用程式
app = QtWidgets.QApplication(sys.argv)

# 建立視窗
w = QtWidgets.QWidget()

# 設定視窗標題
w.setWindowTitle('哈囉拍沈')
# 設定視窗尺寸
w.resize(300,300)

# 顯示
w.show()

# 執行
sys.exit(app.exec())