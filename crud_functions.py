import sqlite3

connection = sqlite3.connect('bot_product.db')
cursor = connection.cursor()


def initiate_db():
    # для создания БД Products
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL,
    image TEXT NOT NULL
    );
    """)

# Создаю БД Products
initiate_db()

# стираю все строки в БДешке (для обновления, чтобы не накапливались данные)
cursor.execute("DELETE FROM Products")

# добавляю с использованием цикла for
"""
изменил интерацию с учетом картинок(c 5 по 9 картинки)
"""
for i in range(5, 10):
    cursor.execute("INSERT INTO Products (title, description, price, image) VALUES (?, ?, ?, ?)",
                   (f"Product{i}", f"info{i}", int(i * 100), f'Image/{i}.png'))

def get_all_products():
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()
    # connection.commit() # сохраняем имзенения
    return products

# запускаю функцию и дальше использую переменную в телеграм-боте
Products = get_all_products()

# ДЛЯ ПРОВЕРКИ
# print(get_all_products())
# for user in get_all_products():
#     title, info, price, image = user[1], user[2], user[3], user[4]
#     print(f"Продукт: {title} | Описание: {info} | Цена: {price} | Картинка: {image}")

connection.commit()
connection.close()
