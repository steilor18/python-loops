from sklearn.linear_model import LinearRegression
import numpy as np

данные = [
[4,3,4,5,4],
[5,4,5,4,5],
[3,4,3,4,4],
[4,5,4,5,5],
[5,4,5,4,5]
]
x = []
y = []
for строка in данные:
  x.append(строка[:4])
  y.append(строка[4])

model = LinearRegression()
model.fit(x, y)
def предсказать_оценку():
   print("Введи оценки за четверти: ")
первая = float(input("Первая четверть: "))
вторая = float(input("Вторая четверть: "))
третья = float(input("Третья четверть: "))
четвертая = float(input("Четвертая четверть: "))

оценка = model.predict([[первая, вторая, третья, четвертая]])[0]

результат = round(оценка)
if результат < 2:
   результат = 2
elif результат > 5:
   результат = 5

print(f"\nТвоя годовая: {результат}")
print(f"\nА, это точная: {оценка:.2f}")
