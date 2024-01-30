import pandas as pd
data = {10, 20, 30, 40, 50};

s = pd.Series(list(data));

print(s)

s1 = pd.Series(tuple(data));

print(s1)