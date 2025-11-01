import pandas as pd
df = pd.read_csv ('оценки.csv')
средние_по_предметам = df.mean().round(2)
total_mean = df.values.mean().round(2)
print (средние_по_предметам)
print(total_mean)