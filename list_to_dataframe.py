import pandas as pd
li = [10, 20, 30, 40, 50, 60, 70, 80];

my_data_frame = pd.DataFrame(li, columns=["num"]);

print(my_data_frame);



li2 = [[10, 20], [30, 40], [50, 60], [70, 80]];

my_data_frame2 = pd.DataFrame(li2,columns=["num1", "num2"]);


print(my_data_frame2);