from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import pandas as pd

excel = pd.read_excel(r"C:\Users\wojci\Desktop\korekta\ALDI.xlsx", sheet_name="Missing_coding")
print(excel.head())

excel['ratio'] = excel.apply(lambda row: fuzz.ratio(row['SIRPAIR'], row['OGRDS']), axis=1)
print(excel.head())
print(excel.ratio.min(axis=0))
print(excel[excel.ratio == excel.ratio.min(axis=0)])
excel.to_excel(r"C:\Users\wojci\Desktop\korekta\ALDI2.xlsx",'Sheet1', index=False)

print(fuzz.ratio("STRYHNÆS JULEPOSTEJ [24.95]", "STRYHN�S JULEPOSTEJ [24.95�"))

fuzz.partial_ratio("ACME Factory", "ACME Factory Inc.")

