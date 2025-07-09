import pandas

# 一維資料

data = pandas.Series([1,2,35,6,7,12,23])

# print(data)

# 二維資料
q = [
        [1,2,3,4,5],
        ['a','b','c','d','e'],
        ['a','b','c','d','e'],
        ['a','b','c','d','e'],
        ['a','b','c','d','e'],
        ['a','b','c','d','e'],
        ['a','b','c','d','e'],
        ['a','b','c','d','e'],
        ['a','b','c','d','e'],
        ['a','b','c','d','e']
    ]
data2 = pandas.DataFrame(
    q,
    columns=['A','B','C','D','E'],
    index=range(len(q))
)

# print(data2)
# print(data2.shape)
# print(data2.size)
#
data3 = pandas.DataFrame(
    [
        ['商品1','299'],
        ['商品2','399']
    ]
)
# print(data3)

data4 = pandas.DataFrame(
    [
        {
            '名稱':'商品一',
            '價格':'299'
        },
        {
            '名稱':'商品二',
            '價格':'399'
        }
    ],
    index=['A','B']
)
print(data4)
# print(data4.size)
# print(data4.shape)
# print(data4.index)
# print(data4.columns)

# print(data4.iloc[0])
# print(data4.loc['B'])
# print(data4.iloc[1])
# print(data4['名稱'])
# print(data4['價格'])

# print(data4.loc['B']['價格'])
print(data4['價格'].iloc[1])