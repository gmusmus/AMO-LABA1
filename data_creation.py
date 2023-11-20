import numpy as np
import pandas as pd
import os
import shutil
from sklearn.model_selection import train_test_split
# создрание данных набор температуры
# Создаем даты с января 2021 года по декабрь 2023 года
dates = pd.date_range(start='2021-01-01', end='2023-12-31', freq='D')

# Генерируем случайные значения температуры
temperature = np.random.normal(loc=25, scale=5, size=len(dates))

# Создаем DataFrame
temperature_df = pd.DataFrame({'Дата': dates, 'Температура': temperature})

# Устанавливаем 'Дата' в качестве индекса
temperature_df.set_index('Дата', inplace=True)

# Выводим первые несколько строк
print('Посмотрим несколько строк полученного датасета')
print(temperature_df.head())
print('размер датасета')
print(len(temperature_df))

# Разделим данные на тренировочный и тестовый наборы
train_df, test_df = train_test_split(temperature_df, test_size=0.2, random_state=42)
# Удаляем папки 'train' и 'test', если они уже существуют
if os.path.exists('train'):
    shutil.rmtree('train')
if os.path.exists('test'):
    shutil.rmtree('test')

# Создаем папки 'train' и 'test', если они не существуют
if not os.path.exists('train'):
    os.makedirs('train')
if not os.path.exists('test'):
    os.makedirs('test')

# Сохраняем данные в соответствующие папки
train_df.to_csv('train/temperature_train.csv')
test_df.to_csv('test/temperature_test.csv')

# Посмотрим информацию о размере тренировочного и тестового наборов
print('Размер тренировочного набора:', len(train_df))
print('Размер тестового набора:', len(test_df))


# добавим мусора
def add_garbage_to_csv(csv_file_path):
    # Load the original CSV file
    original_df = pd.read_csv(csv_file_path, index_col='Дата', parse_dates=True)

    # Generate random positions to insert garbage data
    num_garbage_rows = np.random.randint(1, 10)  # Change the range based on your preference
    positions = np.random.choice(original_df.index, num_garbage_rows, replace=False)

    # Generate garbage data
    garbage_dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
    garbage_temperature = np.random.normal(loc=50, scale=10, size=len(garbage_dates))
    garbage_df = pd.DataFrame({'Дата': garbage_dates, 'Температура': garbage_temperature})
    garbage_df.set_index('Дата', inplace=True)

    # Ensure the index of garbage_df is in datetime format
    garbage_df.index = pd.to_datetime(garbage_df.index)

    # Insert garbage data at random positions
    for position in positions:
        original_df = pd.concat([original_df, garbage_df], axis=0).sort_index()

    # Save the updated DataFrame to the CSV file
    original_df.to_csv(csv_file_path)


# Add garbage data to the end of the train and test CSV files
add_garbage_to_csv('train/temperature_train.csv')
add_garbage_to_csv('test/temperature_test.csv')