import sqlite3 

try:
    sqlite_connection = sqlite3.connect('users_tgbot.db')
    create_table = ('''CREATE TABLE IF NOT EXISTS Users (
                        UserID INTEGER PRIMARY KEY,
                        Name TEXT,
                        LastName TEXT,
                        Age INTEGER,
                        City TEXT,
                        Description TEXT,
                        Image BLOB
                        )''')
    cursor = sqlite_connection.cursor()
    print('База данных успешно создана и подключена к SQLite')
    cursor.execute(create_table)
    sqlite_connection.commit()
    print('Таблицы были созданы')
    
    cursor.close()
    
except sqlite3.Error as error:
    print('Ошибка при подключении к sqlite', error)
finally:
    if (sqlite_connection):
        sqlite_connection.close()
        print('Соединение с SQLite закрыто')