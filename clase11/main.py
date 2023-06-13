import sqlite3
import getpass


def main():
    username = input('Nombre de usuario: ')
    password = getpass.getpass('Contraseña: ')

    if check_credentials(username, password):
        print('Bienvenido')
    else:
        print('Credenciales incorrectas')


def check_credentials(username, password):
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()

    query = f'SELECT id FROM user WHERE username = {username}'

    rows = cursor.execute(query)
    data = rows.fetchone()

    cursor.close()
    conn.close()

    if data is None:
        return False


if __name__ == '__main__':
    main()

conn = sqlite3.connect('test.db')

cursor = conn.cursor()

# cursor.execute(
#     'create table user (id varchar(20) primary key, name varchar(20))')

# cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')

# rows = cursor.execute('select * from user')

# for row in rows:
#     print(row)

# cursor.close()

# conn.close()
