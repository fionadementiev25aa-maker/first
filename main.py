from dotenv import load_dotenv
import os

# Эта строка загружает переменные из файла .env в окружение
load_dotenv()

def print_author():
    # Получаем значение переменной AUTHOR из окружения
    author = os.getenv("AUTHOR")
    print(f"Автор проекта: {author}")

# Вызываем функцию, чтобы проверить работу
print_author()


