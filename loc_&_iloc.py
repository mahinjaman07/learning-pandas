import pandas as pd

'''
1.loc -> working with 'index value'  it also number and string
2.iloc -> working with 'index position'
'''

df = pd.read_csv('Screen Time Data.csv')

print(df.loc[0])

print(df.iloc[0])

df.set_index('Week Day', inplace= True)

print(df.loc['Wednesday'])

print(df.iloc[0])

# print(df.iloc['Wednesday']) not working because iloc working with index position can be number