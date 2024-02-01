import pandas as pd
import gspread
from io import  StringIO

gs = gspread.service_account(filename="C:\\Users\\mahin\\Downloads\\my-data-412817-a32e85e812a0.json")

sheet = gs.open_by_url('https://docs.google.com/spreadsheets/d/1GkkjAsxPKBcreg4keKtzpckMM6XbpEwCQlRxXfhwfEA/edit?usp=sharing')

ws = sheet.worksheet('Data2')

df = pd.DataFrame(ws.get_all_records())

print(df)