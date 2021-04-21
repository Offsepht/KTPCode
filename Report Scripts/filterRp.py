import pandas as pd
import openpyxl as XL



file1 = 'C:\\Users\\tcreps\\Desktop\\AHK\\Report Scripts\\Jon Sale.xlsx'
# file2 = 'C:\\Users\\tcreps\\Desktop\\AHK\\Report Scripts\\gooseRp.xlsx'
vendr = 'C404'

df1 = pd.read_excel(file1)

print(df1.columns)

print(df1.loc[df1['VND#'] == vendr])



