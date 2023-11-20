#!/bin/bash

# Очистка существующих логов
> log.log

# Активация виртуальной среды
source venv/bin/activate

# Запуск data_creation.py
echo -e "\n\n=== Запуск data_creation.py ===" | tee -a log.log
python data_creation.py >> log.log 2>&1
data_creation_exit_code=$?

if [ $data_creation_exit_code -eq 0 ]; then
    echo "data_creation.py завершился успешно" | tee -a log.log
else
    echo "data_creation.py завершился с ошибкой (код: $data_creation_exit_code)" | tee -a log.log
fi

# Добавление пустых строк перед следующим запуском
echo -e "\n\n"

# Запуск model_preparation.py
echo -e "\n\n=== Запуск model_preparation.py ===" | tee -a log.log
python model_preparation.py >> log.log 2>&1
model_preparation_exit_code=$?

if [ $model_preparation_exit_code -eq 0 ]; then
    echo "model_preparation.py завершился успешно" | tee -a log.log
else
    echo "model_preparation.py завершился с ошибкой (код: $model_preparation_exit_code)" | tee -a log.log
fi

# Добавление пустых строк перед следующим запуском
echo -e "\n\n"

# Запуск model_testing.py
echo -e "\n\n=== Запуск model_testing.py ===" | tee -a log.log
python model_testing.py >> log.log 2>&1
model_testing_exit_code=$?

if [ $model_testing_exit_code -eq 0 ]; then
    echo "model_testing.py завершился успешно" | tee -a log.log
else
    echo "model_testing.py завершился с ошибкой (код: $model_testing_exit_code)" | tee -a log.log
fi

# Добавление пустых строк перед завершением
echo -e "\n\n"

# Деактивация виртуальной среды
deactivate | tee -a log.log

# Вывод сообщения о выполнении скриптов
if [ $data_creation_exit_code -eq 0 ] && [ $model_preparation_exit_code -eq 0 ] && [ $model_testing_exit_code -eq 0 ]; then
    echo "=== Все скрипты выполнены без ошибок ===" | tee -a log.log
else
    echo "=== Произошла ошибка при выполнении скриптов. Проверьте лог для получения дополнительной информации. ===" | tee -a log.log
fi

