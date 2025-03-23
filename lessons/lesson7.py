import sqlite3

# A4 - Бумага
connect = sqlite3.connect('users.db')

# Рука которая держит ручку
cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        name VARCHAR (100) NOT NULL,
        age INTEGER NOT NULL,
        hobby TEXT
    )
''')


connect.commit()


def add_user(name, age, hobby):
    cursor.execute(
        'INSERT INTO users(name, age, hobby) VALUES (?,?,?)',
        (name,age,hobby)
    )
    connect.commit()
    print(f"Пользователь {name} добавлен")

# add_user("LUIZA", 20, "плавать")
# add_user("NIKITA", 20, "плавать")
# add_user("MIRANA", 20, "плавать")
# add_user("LIRA", 20, "плавать")

def get_all_users():
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()

    if users:
        print("Список всех пользователей")
        for i in users:
            print(f'NAME: {i[0]}, AGE: {i[1]}, HOBBY: {i[2]}')
    else:
        print('Пользователей нет')

get_all_users()

def update_users(rowid, hobby=None, name=None, age=None):
    cursor.execute('UPDATE users SET hobby = ? WHERE rowid = ?', (hobby, rowid))
    connect.commit()
    print('Пользователь обновлен')

update_users(rowid=1, hobby='Спать')

def delete_users(name):
    cursor.execute('DELETE FROM users WHERE name = ?', (name,))
    connect.commit()
    print('Пользователь удален')

delete_users("LIRA")
get_all_users()