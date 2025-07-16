import matplotlib.pyplot as plt

plt.rc('font',family='Microsoft Jhenghei')

plt.pie([21,35,12,44],
        labels=['A','B','C','D'],
        labeldistance=1.1,
        startangle=10,
        explode=[0,0,.3,0],
        autopct='%.2f%%'
        )

# plt.legend()

plt.show()