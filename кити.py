import pandas as pd
df = pd.read_csv('оценки.csv')
средняя_оценка = df.mean().mean()
средние_по_предметам = df.mean()
print("Средние оценки по предметам:")
print(средние_по_предметам)