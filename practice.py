import pandas as pd 

df = pd.read_csv('Screen Time Data.csv')

# problem1

# print(df[(df['Week Day'] == 'Wednesday') & (df['Entertainment'] == 0)]);

# problem2


# print(df[df['Productivity'] > 15])


#problem3

print(df[(df['Productivity']) == df['Productivity'].min()])

