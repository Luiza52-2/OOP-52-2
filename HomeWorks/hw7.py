import sqlite3

# Подключение к базе данных
connect = sqlite3.connect('users.db')
cursor = connect.cursor()

# Создание таблицы, если она не существует
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        name VARCHAR (100) NOT NULL,
        age INTEGER NOT NULL,l
        hobby TEXT
    )
''')

connect.commit()

# Функция для добавления пользователя
def add_user(name, age, hobby):
    cursor.execute(
        'INSERT INTO users(name, age, hobby) VALUES (?, ?, ?)',
        (name, age, hobby)
    )
    connect.commit()
    print(f"Пользователь {name} добавлен")

# Функция для получения всех пользователей
def get_all_users():
    cursor.execute('SELECT rowid, * FROM users')  # Добавлен rowid для идентификации
    users = cursor.fetchall()

    if users:
        print("Список всех пользователей:")
        for user in users:
            print(f'ROWID: {user[0]}, NAME: {user[1]}, AGE: {user[2]}, HOBBY: {user[3]}')
    else:
        print('Пользователей нет')

# Новая функция для получения пользователя по rowid
def get_user_by_id(rowid):
    cursor.execute('SELECT * FROM users WHERE rowid = ?', (rowid,))
    user = cursor.fetchone()

    if user:
        print(f'NAME: {user[0]}, AGE: {user[1]}, HOBBY: {user[2]}')
    else:
        print(f'Пользователь с rowid {rowid} не найден')

# Обновленная функция для изменения данных пользователя
def update_users(rowid, name=None, age=None, hobby=None):
    if name:
        cursor.execute('UPDATE users SET name = ? WHERE rowid = ?', (name, rowid))
    if age:
        cursor.execute('UPDATE users SET age = ? WHERE rowid = ?', (age, rowid))
    if hobby:
        cursor.execute('UPDATE users SET hobby = ? WHERE rowid = ?', (hobby, rowid))
    connect.commit()
    print(f'Пользователь с rowid {rowid} обновлен')

# Функция для удаления пользователя
def delete_users(name):
    cursor.execute('DELETE FROM users WHERE name = ?', (name,))
    connect.commit()
    print(f'Пользователь с именем {name} удален')


if __name__ == "__main__":
    add_user("LUIZA", 20, "плавать")
    add_user("NIKITA", 25, "читать")
    add_user("MIRANA", 22, "петь")
    add_user("LIRA", 30, "рисовать")

    print("\n--- Список пользователей ---")
    get_all_users()

    print("\n--- Получение пользователя по rowid ---")
    get_user_by_id(3)

    print("\n--- Обновление данных пользователя ---")
    update_users(rowid=3, name="Oleg", hobby="играть на гитаре")

    print("\n--- Список пользователей после обновления ---")
    get_all_users()

    print("\n--- Удаление пользователя ---")
    delete_users("LIRA")

    print("\n--- Список пользователей после удаления ---")
    get_all_users()

connect.close()