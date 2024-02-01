import pandas as pd
import requests
from io import StringIO

url = 'https://raw.githubusercontent.com/mahinjaman07/learning-pandas/master/bike.csv';

response = requests.get(url)

content = StringIO(response.text)

data = pd.read_csv(content)

print(data.head())