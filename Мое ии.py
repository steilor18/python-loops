from sklearn.linear_model import LinearRegression
import numpy as np

grades = print("Введите ваши оценочки :)")

average_grade = sum(grades) / len(grades)

if average_grade >= 4.5:
 predicted_grade = 5
 comment = "Молодец! В этом году можешь отдыхать"
elif average_grade >= 3.5:
 predicted_grade = 4
 comment = "Очень хорошо, но можно было лучше"
elif average_grade >= 2.5:
 predicted_grade = 3
 comment = "Неплохо. Но перестань ленится"
else:
 predicted_grade = 2
 comment = "Ну, ты конечно хуже некуда скатился. Что делал весь год?"
 
 model = LinearRegression()

print("\n🧠 Обучаю модель...")
model.fit(grades)
print("✅ Модель обучена!")

print("\n" + "="*50)
print("РЕЗУЛЬТАТЫ:")
print(f"Средний балл: {average_grade:.2f}")
print(f"Предсказанная годовая оценка: {predicted_grade}")
print(f"Коментик: {comment}")