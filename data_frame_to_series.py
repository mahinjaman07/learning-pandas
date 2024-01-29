import pandas as pd
li = [10, 20, 30, 40, 50, 60, 70, 80];

my_data_frame = pd.DataFrame(li, columns=["num"]);

series = my_data_frame["num"]

# print(series);

li2 = [[10, 20], [30, 40], [50, 60], [70, 80]];

my_data_frame2 = pd.DataFrame(li2, columns=["num1", "num2"])

series2 = my_data_frame2[["num1", "num2"]]

print(type(series2));