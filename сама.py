import pandas as pd
df = pd.read_csv ('shopping.csv')
df['сумма'] = df['цена'] * df['количество']
print (df)