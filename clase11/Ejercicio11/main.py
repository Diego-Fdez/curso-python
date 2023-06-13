import sqlite3


def main():
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()

    cursor.execute(
        'Create table if not exists alumnos (id INTEGER PRIMARY KEY, name VARCHAR(40), last_name VARCHAR(40))')

    cursor.execute(
        'insert into alumnos (name, last_name) values ("Juan", "Perez")')
    cursor.execute(
        'insert into alumnos (name, last_name) values ("Maria", "Gomez")')
    cursor.execute(
        'insert into alumnos (name, last_name) values ("Jose", "Gonzalez")')
    cursor.execute(
        'insert into alumnos (name, last_name) values ("Pedro", "Lopez")')
    cursor.execute(
        'insert into alumnos (name, last_name) values ("Ana", "Martinez")')
    cursor.execute(
        'insert into alumnos (name, last_name) values ("Luis", "Gutierrez")')
    cursor.execute(
        'insert into alumnos (name, last_name) values ("Carlos", "Rodriguez")')
    cursor.execute(
        'insert into alumnos (name, last_name) values ("Marta", "Sanchez")')

    search_student = input('Ingrese el nombre del estudiante a buscar: ')
    query = f'select * from alumnos WHERE name = "{search_student}"'

    rows = cursor.execute(query)
    data = rows.fetchone()

    cursor.close()
    conn.close()

    if data is None:
        return False

    print(data)


if __name__ == '__main__':
    main()
