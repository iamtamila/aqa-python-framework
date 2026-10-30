# config.py — единственное место, откуда тесты берут настройки.
# Если адрес стенда поменяется, правим .env, а не 50 тестов.

import os                       # стандартный модуль: доступ к переменным окружения
from dotenv import load_dotenv  # из библиотеки python-dotenv: умеет читать файл .env

# Шаг 1. Читаем файл .env и превращаем его строки в переменные окружения.
# Если файла нет (например, в CI), функция просто ничего не делает:
# значения тогда придут из секретов CI.
load_dotenv()

# Шаг 2. Достаём значения по имени.
# os.getenv("ИМЯ", "запасное значение") вернёт запасное, если переменной нет.
API_BASE_URL = os.getenv("API_BASE_URL", "https://jsonplaceholder.typicode.com")
UI_BASE_URL = os.getenv("UI_BASE_URL", "https://www.saucedemo.com")

# Шаг 3. У секретов запасного значения НЕТ специально:
# если забыли заполнить .env, получим None и сразу это заметим.
SAUCE_USER = os.getenv("SAUCE_USER")
SAUCE_PASSWORD = os.getenv("SAUCE_PASSWORD")