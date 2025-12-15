from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

# Данные
shoe_size = np.array([36, 38, 40, 42, 44, 37, 39, 41, 43, 45]).reshape(-1, 1)
height = np.array([160, 165, 170, 178, 185, 162, 168, 175, 180, 188])

# Обучаем модель
model = LinearRegression()
model.fit(shoe_size, height)

# Предсказания
predictions = model.predict(shoe_size)

# ГРАФИК!
plt.figure(figsize=(10, 6))
plt.scatter(shoe_size, height, color='blue', s=100, label='Реальные данные', zorder=3)
plt.plot(shoe_size, predictions, color='red', linewidth=2, label='Линия предсказания AI', zorder=2)
plt.xlabel('Размер обуви', fontsize=12)
plt.ylabel('Рост (см)', fontsize=12)
plt.title('🧠 Как AI находит закономерность', fontsize=14)
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

print("📊 График показывает, как AI провёл линию через данные!")