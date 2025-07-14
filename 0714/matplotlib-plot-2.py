import matplotlib.pyplot as plt

plt.rc('font', family='Microsoft Jhenghei')

dataY = [34, 22, 18, 26, 28]
dataX = [10,20,30,40,50]

dataY2 = [18, 24, 22, 18,24]
dataY3 = [22, 34, 26, 28,34]



plt.plot(dataX,dataY,
         color='red',
         linewidth=1,
         linestyle='-',
         marker='.',
         markersize=10,
         label='亞洲'
         )

plt.plot(dataX,dataY2,
         color='blue',
         linewidth=1,
         linestyle='-',
         marker='.',
         markersize=10,
         label='北美洲'
         )

plt.plot(dataX,dataY3,
         color='orange',
         linewidth=1,
         linestyle='-',
         marker='.',
         markersize=10,
         label='南美洲'
         )

plt.legend()

plt.title('一周天氣圖表')

plt.xlabel('天')
plt.ylabel('氣溫')

plt.xlim(0, 60)
plt.ylim(0, 50)

plt.xticks(range(0,60,10))
plt.yticks(range(0,50,5))

plt.show()

