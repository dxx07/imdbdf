import pandas as pd
import matplotlib.pyplot as plt
# Загрузка данных
df = pd.read_csv('IMDB-Movie-Data.csv')
df.info()
# Гипотеза
print('Фильмы с Мэтью Макконахи имеют выше рейтинг, чем фильмы с Мел Гибсоном')

# Создадим два отдельных датафрейма для Макконахи и Гибсона
matthew_mcconaughey_df = df[df['Actors'].str.contains('Matthew McConaughey', case=False)]
mel_gibson_df = df[df['Actors'].str.contains('Mel Gibson', case=False)]

# Средний рейтинг фильмов Мэтью Макконахи
avg_rating_mcconaughey = matthew_mcconaughey_df['Rating'].mean()

# Средний рейтинг фильмов Мел Гибсона
avg_rating_gibson = mel_gibson_df['Rating'].mean()

# Вывод результатов
print(f"Средний рейтинг фильмов Мэтью Макконахи: {avg_rating_mcconaughey}")
print(f"Средний рейтинг фильмов Мел Гибсона: {avg_rating_gibson}")

# Создание столбчатой диаграммы
actors = ['Matthew McConaughey', 'Mel Gibson']
avg_ratings = [avg_rating_mcconaughey, avg_rating_gibson]

plt.bar(actors, avg_ratings)
plt.xlabel('Актеры')
plt.ylabel('Средний рейтинг')
plt.title('Сравнение средних рейтингов фильмов Мэтью Макконахи и Мел Гибсона')
plt.show()
