import pandas as pd
data = [10, 20, 30, 40, 50, 60, 70, 80];

series = pd.Series(data, name="number");

data_frame = pd.DataFrame(series);

print(data_frame);


li2 = [[10, 20], [30, 40], [50, 60], [70, 80]];

series2 = pd.Series(li2, name="number");


data_frame2 = pd.DataFrame(series2);

print(data_frame2);