import pandas  as pd
import requests
from io import StringIO

url  = 'https://raw.githubusercontent.com/mahinjaman07/learning-pandas/master/bike.csv'

response = requests.get(url)

csv_content = StringIO(response.text)

df = pd.read_csv(csv_content)

print(df.head())