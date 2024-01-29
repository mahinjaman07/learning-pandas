import pandas as pd
li = [10, 20, 30, 40, 50, 60, 70, 80];

my_series = pd.Series(li, name="number");

print(my_series);



li2 = [[10, 20], [30, 40], [50, 60], [70, 80]];

series2 = pd.Series(li2, name="number");


print(series2);