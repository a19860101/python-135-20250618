import matplotlib.pyplot as plt
import pandas as pd
plt.rc('font',family='Microsoft Jhenghei')

label = ['一月','二月','三月','四月','五月']
data1 = [40,50,60,50,40]
data2 = [45,66,82,90,18]

x = [1,2,3,4,5]
x2 = [i - 0.1 for i in x]

# plt.bar([1,2,3,4,5],data1, width=.4, color='red', align='edge')
# plt.bar([.8,1.8,2.8,3.8,4.8],data2,width=.4,color='blue')

plt.bar(x,data1, width=.2, color='red', align='edge')
plt.bar(x2,data2,width=.2,color='blue')

plt.xticks(range(1,6), label)

plt.show()
