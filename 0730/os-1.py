import os

# 檔案名稱
print(os.path.basename(__file__))

# 取得絕對路徑
print(os.path.abspath(__file__))

# 取得資料夾名稱
print(os.path.dirname(__file__))

# 分割副檔名
print(os.path.splitext(__file__))
_, ext = os.path.splitext(__file__)
print(ext)

# 判斷檔案是否存在
print(os.path.exists(__file__))