import pandas as pd
from sklearn.metrics import mean_squared_error
import joblib

# Загрузим тестового набора данных
test_df = pd.read_csv('test/temperature_test.csv', index_col='Дата', parse_dates=True)

# Загрузим сохраненной модели
model_filename = 'temperature_model.joblib'
loaded_model = joblib.load(model_filename)

# Подготовим данные для предсказания
X_test = test_df.index.values.reshape(-1, 1)
y_test = test_df['Температура'].values

# Предсказажем на тестовом наборе
y_pred = loaded_model.predict(X_test)

# Оценка предсказаний
mse = mean_squared_error(y_test, y_pred)
print(f'Среднеквадратичная ошибка на тестовом наборе: {mse}')

# Создадим общий датафрейм  с фактическими и предсказанными значениями
predictions_df = pd.DataFrame({'Фактическое значение': y_test, 'Предсказанное значение': y_pred},
                               index=test_df.index)

# Выведим таблицы с предсказаниями
print(predictions_df)