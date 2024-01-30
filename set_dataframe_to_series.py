import pandas as pd
data = {10, 20, 30, 40, 50};

df = pd.DataFrame(data, columns=['num'])

s = df['num']
print(s);