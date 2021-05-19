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
conn = sqlite3.connect("clientes.db")
c = conn.cursor()
c.execute("INSERT INTO clientes VALUES ('Manuelito', 'Nunez', 'a1231124@uabc.edu.mx')")
print("Insertar los datos Manuelito Nunez a1231124@uabc.edu.mx")
print("Datos agregados exitosamente")
#commit comando
conn.commit()
#cerrar conexion
#leer datos
c = conn.cursor()
c.execute("SELECT * FROM clientes")
print(c.fetchall())
conn.close()
