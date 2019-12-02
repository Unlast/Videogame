import sqlite3
"""
Base de datos donde se guardaran los resultados de los jugadores
"""

conexion = sqlite3.connect("BdSpaceShoot.db")

cursor = conexion.cursor()
"""
cursor.execute("CREATE TABLE JUGADOR(nombre TEXT, puntos INTEGER)")

lista_demo = [('AAA',500),('BBB',1000),('CCC',1500),('DDD',2000),('EEE',2500)]

cursor.executemany("INSERT INTO JUGADOR VALUES (?, ?)", lista_demo)

cursor.execute("SELECT * FROM JUGADOR")

jugadores = cursor.fetchall()

for jugador in jugadores:
    print(jugador)

conexion.commit()

conexion.close()
"""

def ordenar(db):
    
    conexion = sqlite3.connect(db)
    
    cursor = conexion.cursor()
    
    cursor.execute("SELECT * FROM JUGADORES ORDER BY puntos")
    
    lista_jugadores = cursor.fetchall()
    
    for jugador in lista_jugadores:
        print(jugador)
    
    conexion.commit()
    conexion.close()
    
def borrar(db):
    
    conexion = sqlite3.connect(db)
    
    cursor = conexion.cursor()
    
    cursor.execute("DELETE FROM JUGADORES WHERE puntos < 500")
    
    conexion.commit()
    conexion.close()
    