import pandas as pd

data = {
    "Name":["Mahin", "Rahim", "Rasel", "Rifat"],
    "Age":[18, 20, 19, 22],
    "Gender":["Male", "Male", "Male", "Male"]
};

series = pd.Series(data);

print(series);

print(series[0]);

series = pd.Series(data["Name"]);

print(series[2]);