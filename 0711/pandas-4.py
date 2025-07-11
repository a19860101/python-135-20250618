import pandas as pd

data = pd.read_json('data.json')
print(data)

print(data[data['name'].str.contains('王')])