import pandas as pd

def clean_and_save_csv(csv_file_path):
    # загрузка датасета
    df = pd.read_csv(csv_file_path, index_col='Дата', parse_dates=True)

    # сохранение кол-ва записей
    initial_records = len(df)

    # удаление дубликатов
    df = df[~df.index.duplicated(keep='first')]

    # удаление аномальных значений температур
    initial_anomalies = len(df)
    df = df[(df['Температура'] >= -45) & (df['Температура'] <= 55)]
    remaining_records = len(df)

    # сохранение файла
    df.to_csv(csv_file_path)

    # распечатаем результаты работы
    print(f"Файл обработанный: {csv_file_path}")
    print(f"Первоначальное кол-во записей: {initial_records}")
    print(f"Удалено дубликатов: {initial_records - len(df)}")
    print(f"Удалено строк с аномальными значения температур: {initial_anomalies - remaining_records}")
    print(f"Всего скопировано записей: {remaining_records}")
    print("\n")

# сохранение файлов
clean_and_save_csv('train/temperature_train.csv')

clean_and_save_csv('test/temperature_test.csv')