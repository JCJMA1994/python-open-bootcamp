# En este ejercicio tendréis que crear una tabla llamada Alumnos que constará de tres columnas:
# la columna id de tipo entero, la columna nombre que será de tipo texto y la columna apellido que
# también será de tipo texto.
# Una vez creada la tabla, tenéis que insertarle datos, como mínimo tenéis que insertar 8 alumnos a la tabla.
# Por último, tienes que realizar una búsqueda de un alumno por nombre y mostrar los datos por consola.

import  sqlite3

db_connection = sqlite3.connect("my-app.sqlite")
db_cursor = db_connection.cursor()

db_cursor.execute("create table students(id  integer constraint students_pk primary key, "
                  "name  text not null, "
                  "lastname text not null)")
db_cursor.execute("create unique index students_id_uindex on students (id)")

db_cursor.execute("insert into students values (1, 'Jose Carlos Joao', 'Moreno Aleman')")
db_cursor.execute("insert into students values (2, 'Patricia', 'Suarez')")
db_cursor.execute("insert into students values (3, 'Anibal', 'Nicolas')")
db_cursor.execute("insert into students values (4, 'Inmaculada', 'Valles')")
db_cursor.execute("insert into students values (5, 'Elena', 'Ferrero')")
db_cursor.execute("insert into students values (6, 'Antoni', 'Oliveira')")
db_cursor.execute("insert into students values (7, 'Cristina', 'Tomas')")
db_cursor.execute("insert into students values (8, 'Emilio', 'Sousa')")

db_connection.commit()

db_cursor.execute("select * from students where name = 'Jose Carlos Joao'")

row = db_cursor.fetchall()
print(row)

db_connection.close()