import pandas as pd

# df = pd.read_excel('pokemon_date.xlsx')
df = pd.read_csv('pokemon_data.txt', '|')
print(df.head(5))
print(df.tail(5))
