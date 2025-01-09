import os
import time

directory = '.'

for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(directory, file)
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(filepath)
        parent_dir = os.path.dirname(filepath)
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, '
              f'Родительская директория: {parent_dir}')

# Обнаружен файл: 3.py, Путь: .\3.py, Размер: 1625 байт,
# Время изменения: 08.12.2024 14:33, Родительская директория: .

# Обнаружен файл: 5.py, Путь: .\5.py, Размер: 1555 байт,
# Время изменения: 09.01.2025 16:58, Родительская директория: .

# Обнаружен файл: test_file.txt, Путь: .\test_file.txt, Размер: 171 байт,
# Время изменения: 08.12.2024 14:32, Родительская директория: .
