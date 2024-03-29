print("Este es un programa de python crud")

import sqlite3

conn = sqlite3.connect("clientes.db") #Creamos la base de datos

c = conn.cursor()

#crear tablas
'''
c.execute("""
CREATE TABLE clientes (
    nombre text,
    apellido text,
    correo text
)
""")
#commit comando
conn.commit()
#cerrar conexion
conn.close()
''' #lo puse en comentario porque ya habia creado la tabla haciendo pruebas
#abrimos nuevamente la conexion
'''conn = sqlite3.connect("clientes.db")
c = conn.cursor()
c.execute("INSERT INTO clientes VALUES ('Manuelito', 'Nunez', 'a1231124@uabc.edu.mx')") #-----------------------------------
print("Insertar los datos Manuelito Nunez a1231124@uabc.edu.mx")
print("Datos agregados exitosamente")
#commit comando
conn.commit()
#cerrar conexion
#leer datos
''' #lo comento porque ya inserte muchas veces lo mismo
c = conn.cursor()
c.execute("SELECT * FROM clientes")
print(c.fetchall())
c.execute("SELECT * FROM clientes")
items = c.fetchall()
for item in items:
    print(item[0] + " " + item[1] + " | " + item[2] + " ")
conn.commit()
#actualizar un dato
c.execute('''UPDATE clientes SET nombre = 'Bob' #------------------------------------
wHERE apellido = 'Nunez'
''')
conn.commit()
c.execute("SELECT * FROM clientes")
items = c.fetchall()
for item in items:
    print(item[0] + " " + item[1] + " | " + item[2] + " ")
conn.commit()
c.execute("INSERT INTO clientes VALUES ('Susana', 'Distancia', 'distasus@gob.mx')")
c.execute("INSERT INTO clientes VALUES ('Manuelito', 'Nunez', 'a1231124@uabc.edu.mx')")
c.execute("INSERT INTO clientes VALUES ('Bobo', 'Perez', 'bob4@uabc.edu.mx')")
print("Datos agregados exitosamente")
c.execute("DELETE FROM clientes wHERE nombre = 'Bobo'")#-------------------------------------
print("Datos eliminados exitosamente")
c.execute("SELECT * FROM clientes")#----------------------------------------
items = c.fetchall()
for item in items:
    print(item[0] + " " + item[1] + " | " + item[2] + " ")
conn.commit()
conn.close()