import sqlite3


# Функция для создания представления users_grade
def create_users_grades_view():
    # Подключаемся к базе данных (создаётся файл users_grades.db, если его нет)
    connection = sqlite3.connect('users_grades.db')
    cursor = connection.cursor()

    # Создаём таблицы для теста (users и grades)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS grades (
            user_id INTEGER,
            grade INTEGER,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
    ''')

    # Создаём представление users_grade
    cursor.execute('''
        CREATE VIEW IF NOT EXISTS users_grade AS
        SELECT users.id, users.name, users.age, grades.grade
        FROM users
        INNER JOIN grades ON users.id = grades.user_id
    ''')

    print("Представление users_grade создано успешно.")

    # Закрываем соединение
    connection.commit()
    connection.close()


# Пример вызова представления
def get_young_users():
    # Подключаемся к базе данных
    connection = sqlite3.connect('users_grades.db')
    cursor = connection.cursor()

    # Выбираем данные из представления users_grade
    cursor.execute('SELECT * FROM users_grade WHERE age < 25')
    results = cursor.fetchall()

    for row in results:
        print(row)

    # Закрываем соединение
    connection.close()


# Использование функций
create_users_grades_view()

# Наполняем тестовыми данными
connection = sqlite3.connect('users_grades.db')
cursor = connection.cursor()
cursor.execute("INSERT INTO users (name, age) VALUES ('Alice', 22)")
cursor.execute("INSERT INTO users (name, age) VALUES ('Bob', 27)")
cursor.execute("INSERT INTO grades (user_id, grade) VALUES (1, 90)")
cursor.execute("INSERT INTO grades (user_id, grade) VALUES (2, 85)")
connection.commit()
connection.close()

get_young_users()