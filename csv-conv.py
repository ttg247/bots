import pandas as pd
path = ""
sheet_name = ""
sj_dict = pd.read_excel(path, sheet_name, usecols="A",)

sj = sj_dict.to_csv