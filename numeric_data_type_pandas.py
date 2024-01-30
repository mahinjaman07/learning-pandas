import pandas as pd
data = {
    "Age":[18, 20, 25, 30, 26, 22],
    "Salary":[25000, 15000, 35000, 22000, 35000, 33500]
}

df = pd.DataFrame(data);

# print(df.dtypes)

# print(df.info())


# convert data type in dataframe

df["Age"] = df["Age"].astype('int64'); #float e convert korte chaile float16/32/64 dile e float e convert hoye jabe
df["Salary"] = df["Salary"].astype('int64'); #float e convert korte chaile float16/32/64 dile e float e convert hoye jabe

print(df.info())