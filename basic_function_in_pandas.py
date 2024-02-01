import pandas as pd

df = pd.read_csv('bike.csv')

print(df.shape); # return how many row and column
print(df.info); #return row and column info

print(df.head()); # return first 5 row
print(df.head(2)); # return first 5 row


print(df.tail()); # return last 5 rows

print(df.tail(2)); # return last 2 rows


# range of index
print(df[20:30])

print(df.season); # return season

print(df['season']);

# index check

print(df.index) #RangeIndex(start=0, stop=17379, step=1)

#length check

print(len(df)) #17379

print(len(df.index)) #17379

# column check    
print(df.columns)

# gor number check

print(df['season'].mean())

# standard value

print(df['season'].std())


# shob theke beshi value

print(df['temp'].mode())

# parcentage value check

print(df['temp'].quantile([0.25]))


# all check

print(df.describe())