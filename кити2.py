import pandas as pd
данные = {
 'ОБЗР' : [5, 4, None, None, None, None, None, None, None, None],
 'Вероятность_и_Статистика' : [5, 4, 3, None, None, None, None, None, None, None],
 'География' : [4, 5, 4, 3, None, None, None, None, None, None],
 'Труд' : [4, 4, 4, None, None, None, None, None, None, None],
 'Черчение' : [4, 4, 4, None, None, None, None, None, None, None],
 'Биология' : [4, 4, 5, 5, 5, 4, 4, None, None, None],
 'Русский_язык' : [4, 4, 4, 4, 4, 4, None, None, None, None],
 'Литература' : [5, 4, 5, 3, 5, None, None, None, None, None],
 'Англиский_язык' : [5, 4, 5, 5, 5, 5, 5, 4, 5, 4],
 'Физика' : [4, 5, 4, 5, 3, 3, 3, 3, 2, 3],
 'Алгебра' : [5, 4, 5, 4, 2, None, None, None, None, None],
 'Геометрия' : [3, 5, 4, 5, None, None, None, None, None, None],
 'Химия' : [4, 4, 4, None, None, None, None, None, None, None],
 'Обществознание' : [4, 5, 4, 2, None, None, None, None, None, None],
 'Информатика' : [5, 4, None, None, None, None, None, None, None, None],
 'Физкультура' : [4, 3, 5, 5, 4, 5, 4, 4, None, None],
 'История' : [5, 5, 5, 4, 5, None, None, None, None, None]
}
df = pd.DataFrame(данные)
df.to_csv('оценки.csv', index=False, encoding='utf-8')