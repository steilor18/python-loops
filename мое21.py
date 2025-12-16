from sklearn.linear_model import LinearRegression
import numpy as np
print("Введите ваши оценочки")
print("Для завершения ввода введите: '0'")
print()
grades = []
while True:
    try:
        grade = str(input("Введите оценочку: "))
        if grade == '0':
            break
        
        grades.append(grade)
    except ValueError:
        print("Ошибка: введи целое число!")
        continue

average_grade = str(sum(grades)) / len(grades)

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

model.fit(grades)

print("\n" + "="*50)
print("РЕЗУЛЬТАТЫ:")
print(f"Средний балл: {average_grade:.2f}")
print(f"Предсказанная годовая оценка: {predicted_grade}")
print(f"Коментик: {comment}")