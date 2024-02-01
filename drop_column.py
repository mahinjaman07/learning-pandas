import pandas as pd

df = pd.read_csv('Screen Time Data.csv')

#way 1 : del

del df['index'];
del df['Other'];

# print(df)


# way 2 : pop()

df.pop('Productivity')

# print(df)


# use loc and iloc

df2 = df.loc[ :,['Week Day', 'Reading and Reference']]

# print(df2)


df3 = df.iloc[ : , [0, 1, 2]]

# print(df3)


# way 3 : drop()

df = df.drop('Week Day',  axis= 1)

print(df)

df = df.drop(columns=['Reading and Reference'])

print(df)