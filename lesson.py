import pandas as pd
# my_series = pd.Series([5, 6, 7, 8, 9, 10])
# print(my_series)
df = pd.DataFrame({
     'country': ['Kazakhstan', 'Russia', 'Belarus', 'Ukraine'],
     'population': [17.04, 143.5, 9.5, 45.5],
     'square': [2724902, 17125191, 207600, 603628]
})

df['density'] = df['population'] / df['square'] * 1000000
print(df)
df.to_csv('fffff.csv')