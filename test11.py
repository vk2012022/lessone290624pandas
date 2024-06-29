import pandas as pd

df = pd.read_csv("nvidia_stock_2015_to_2024.csv")

print(df.head())
print(df.tail())
print(df.info())
print(df.describe())

