# pip install matplotlib

import matplotlib.pyplot as plt

dataY = [34, 22, 18, 26, 28]
dataX = [10,20,30,40,50]

plt.plot(dataX,dataY,
         color='red',
         linewidth=1,
         linestyle='-',
         marker='.',
         markersize=10)

plt.show()

"""

color 折線顏色
linestyle 折線樣式 (-, --, -., :)
linewidth 折線寬度
marker 標記
markersize 標記大小

"""