import sqlite3

# A4 - Бумага
connect = sqlite3.connect('users.db')

# Рука которая держит ручку
cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR (30) NOT NULL,
        age INTEGER NOT NULL,
        hobby TEXT
    )
''')

cursor.execute("""
    CREATE TABLE IF NOT EXISTS grades (
        grade_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        subject VARCHAR (100) NOT NULL,
        grade INTEGER NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users(user_id)
    )
               """)

connect.commit()


def add_user(name, age, hobby=""):
    cursor.execute('INSERT INTO users(name, age, hobby) VALUES (?, ?, ?)', (name, age, hobby))
    connect.commit()
    print(f"Пользователь {name} добавлен")


# add_user('Илья Муромец', 25, 'фехтование')
# add_user('John Doe1', 25, 'плавание')
# add_user('John Doe2', 27, 'шахматы')
# add_user('John Doe3', 28, 'чтение')
# add_user('John Doe99', 35, 'шахматы')
# add_user('John Doe88', 33, 'чтение')


def add_grade(user_id, subject, grade):
    cursor.execute('INSERT INTO grades (user_id, subject, grade) VALUES (?,?,?)',
                   (user_id, subject, grade))

    connect.commit()


# add_grade(5, "Алгебра", 2)
# add_grade(5, "Геометрия", 3)
# add_grade(5, "Физика", 5)


# def delete_user_by_id(id):
#     cursor.execute('DELETE FROM users WHERE user_id = ?', (id,))
#     connect.commit()
#     print("Пользователь удален")


# delete_user_by_id(2)


def get_all_user_and_grades():
    cursor.execute('''
        SELECT users.name, users.age, grades.subject, grades.grade
        FROM users INNER JOIN grades ON users.user_id = grades.user_id
                   ''')

    users = cursor.fetchall()

    print("Пользователи с оценками")
    for i in users:
        print(f"NAME: {i[0]}, AGE: {i[1]}, SUBJECT: {i[2]}, GRADE: {i[3]}")


# get_all_user_and_grades()


# AVG() – Среднее значение
# MAX() – Максимальное значение
# MIN() – Минимальное значение  COUNT() SUM()

def get_average_age():
    cursor.execute('SELECT SUM(age) FROM users')
    avg_age = cursor.fetchone()
    print(f"AVG AGE: {int(avg_age[0])}")


# get_average_age()


# VIEW - Пердставление

def create_young_users_view():
    cursor.execute('''
        CREATE VIEW IF NOT EXISTS young_users AS
        SELECT name, age, hobby
        FROM users
        WHERE age < 27
                   ''')
    connect.commit()
    print('Create view')


create_young_users_view()


def get_young_users():
    cursor.execute('SELECT * FROM young_users')
    users = cursor.fetchall()

    for i in users:
        print(f"NAME: {i[0]}, AGE: {i[1]}, HOBBY: {i[2]}")


get_young_users()
