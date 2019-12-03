import sqlite3

"""
Base de datos donde se guardaran los resultados de los jugadores
"""
"""

conexion = sqlite3.connect("BdSpaceShoot.db")

cursor = conexion.cursor()
cursor.execute("CREATE TABLE JUGADOR(juego AUTO_INCREMENT, puntos INTEGER)")

lista_demo = [(1,500),(2,1000),(3,1500),(4,2000),(5,2500)]
cursor.executemany("INSERT INTO JUGADOR VALUES (?,?)", lista_demo)

jugadores = cursor.fetchall()

for jugador in jugadores:
    print(jugador)

conexion.commit()


conexion.close()
"""

def ordenar():
    conexion = sqlite3.connect("BdSpaceShoot.db")
    
    cursor = conexion.cursor()
    
    cursor.execute("SELECT * FROM JUGADOR ORDER BY puntos DESC")
    
    conexion.commit()
    conexion.close()
    mostrar()
    
def borrar(db):
    conexion = sqlite3.connect("BdSpaceShoot.db")

    
    cursor = conexion.cursor()
    
    cursor.execute("DELETE FROM JUGADOR WHERE puntos < 500")
    
    conexion.commit()
    conexion.close()
    
def mostrar():
    conexion = sqlite3.connect("BdSpaceShoot.db")
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM JUGADOR")

    jugadores = cursor.fetchall()

    for jugador in jugadores:
        print(jugador)

def maximo():
    conexion = sqlite3.connect("BdSpaceShoot.db")
    cursor = conexion.cursor()

    max = cursor.execute("SELECT MAX(posicion) FROM JUGADOR")
    print(max)

def agregar(num):
     conexion = sqlite3.connect("BdSpaceShoot.db")
     cursor = conexion.cursor()
     insertar = [(num)]
     cursor.execute("INSERT INTO JUGADOR VALUES (6,?)",insertar)
     conexion.commit()
     conexion.close()