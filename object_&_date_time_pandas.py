import pandas as pd

data = {
    "Name":["Mahin", "Rahim", "Rasel", "Rifat"], #object
    "Age":[18, 20, 19, 22], #int64
    "Salary":['25000 euro', '15000 euro', '35000 euro', '22000 euro'], #object
    "Occupation":["Software Engineer", "Shoper", "Business Man", "Fluencer"]#object
};

df = pd.DataFrame(data);

# print(df.info());



# date and time

date = ['2024-01-30', '2024-01-30', '2025-01-30'];

dtf = pd.DataFrame({'Date': date});

# print(dtf.info())

# convert object  date and time

timestamps = pd.to_datetime(date);

dtf2 = pd.DataFrame(timestamps);

# print(dtf2.info());


# auto date time

date10 = ['2023', '2024-05-10', '2025']

timestamps10 = pd.to_datetime(date10)

dtf10 = pd.DataFrame({'Date': timestamps10})

print(dtf10)