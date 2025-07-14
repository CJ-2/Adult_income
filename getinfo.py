import pandas as pd
df = pd.read_csv('adult.csv')
print(df.shape)
print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())

