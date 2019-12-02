import pygame, os
from Clases import Alien as Enemigo
LISTA_ENEMIGOS = []
"""
La Clase Niveles contiene la posición en las que se instanciarán las naves enemigas
posx ubicacion inicial sobre el eje x se le suma 50 para que no queden las imagenes superpuestas
el segundo valor es la posicion sobre el eje y 
el tercer espacio es la distancia que recorre sobre el eje x

Todos los cargar tienen de parámetro la lista donde serán cargados.

Otros métodos tienen un parámetro llamado lateral se utiliza en los casos
que la cantidad de naves instanciadas es igual en todas las filas
de esta manera descienden en sincronía

dentro de los metodos se instancia un enemigo que puede ser Jefe o nave, se cargar los sprites y sus posiciones y distancias que recorreran, 
mas el ultimo valor que representa a lateral
que indica cuantas veces tocarán los costados antes de bajar, los que tienen más elementos tardarán menos
en recorrer la distancia lateral por lo que se recomienda que el valor que se coloque sea mayor en los casos
de que los objetos que se instancien sean menores y mayor en el caso contrario
"""

def cargarEnemigosPiramide(lista):
     
        posx = 45
        for x in range(1,6):
            armada = Enemigo.nave_enemiga(posx,200,40, 'recursos/imagenes/enemigo001.bmp', 'recursos/imagenes/enemigo002.bmp',4) 
            lista.append(armada)
            posx = posx + 50 
       
        
        posx = 90
        for x in range(1,4):
            armada = Enemigo.nave_enemiga(posx,250,80, 'recursos/imagenes/enemigo001.bmp', 'recursos/imagenes/enemigo002.bmp',2) 
            lista.append(armada)            
            posx = posx + 75
       
        
        posx = 180 
        for x in range(1,2):
            armada = Enemigo.nave_enemiga(posx,300,120, 'recursos/imagenes/enemigo001.bmp', 'recursos/imagenes/enemigo002.bmp',1) 
            lista.append(armada)            
            posx = posx + 50


def cargarEnemigosPiramideI(lista):
      
        posx = 180
        for x in range(1,2):
            armada = Enemigo.nave_enemiga(posx,200,120, 'recursos/imagenes/enemigo001.bmp', 'recursos/imagenes/enemigo002.bmp',3)
            lista.append(armada)
            posx = posx + 50 
       
        
        posx = 90
        for x in range(1,4):
            armada = Enemigo.nave_enemiga(posx,250,80, 'recursos/imagenes/enemigo001.bmp', 'recursos/imagenes/enemigo002.bmp',5) 
            lista.append(armada)                        
            posx = posx + 75
       
        
        posx = 90 
        for x in range(1,6):
            armada = Enemigo.nave_enemiga(posx,300,40, 'recursos/imagenes/enemigo001.bmp', 'recursos/imagenes/enemigo002.bmp',10) 
            lista.append(armada)
            posx = posx + 50      
        
        
def cargarBossPiramide(lista,lateral):
        posx = 45
        for x in range(1,6):
            armada = Enemigo.jefe_enemigo(posx,150,40, 'recursos/imagenes/enemigo003.bmp', 'recursos/imagenes/enemigo004.bmp',lateral)
            lista.append(armada)
            posx = posx + 50 
       
        
        posx = 90
        for x in range(1,4):
            armada = Enemigo.jefe_enemigo(posx,100,80, 'recursos/imagenes/enemigo003.bmp', 'recursos/imagenes/enemigo004.bmp',lateral)            
            lista.append(armada)
            posx = posx + 75
       
        
        posx = 180 
        for x in range(1,2):
            armada = Enemigo.jefe_enemigo(posx,50,120, 'recursos/imagenes/enemigo003.bmp', 'recursos/imagenes/enemigo004.bmp',lateral) 
            lista.append(armada)
            posx = posx + 50

        
def cargarBossPiramideI(lista):
        posx = 90
        for x in range(1,6):
            armada = Enemigo.jefe_enemigo(posx,150,40, 'recursos/imagenes/enemigo003.bmp', 'recursos/imagenes/enemigo004.bmp',6) 
            lista.append(armada)
            posx = posx + 50 
        
        posx = 90
        for x in range(1,4):
            armada = Enemigo.jefe_enemigo(posx,100,80, 'recursos/imagenes/enemigo003.bmp', 'recursos/imagenes/enemigo004.bmp',4)             
            lista.append(armada)
            posx = posx + 75
       
        
        posx = 180 
        for x in range(1,2):
            armada = Enemigo.jefe_enemigo(posx,50,120, 'recursos/imagenes/enemigo003.bmp', 'recursos/imagenes/enemigo004.bmp',8) 
            lista.append(armada)
            posx = posx + 50


def cargarEnemigosLineal(lista,lateral):
        posx = 45
        for x in range(1,6):
            armada = Enemigo.nave_enemiga(posx,200,40, 'recursos/imagenes/enemigo001.bmp', 'recursos/imagenes/enemigo002.bmp',lateral) 
            lista.append(armada)
            posx = posx + 50 
       
        
        posx = 45
        for x in range(1,6):
            armada = Enemigo.nave_enemiga(posx,250,40, 'recursos/imagenes/enemigo001.bmp', 'recursos/imagenes/enemigo002.bmp',lateral) 
            lista.append(armada)
            posx = posx + 50
       
        
        posx = 45 
        for x in range(1,6):
            armada = Enemigo.nave_enemiga(posx,300,40, 'recursos/imagenes/enemigo001.bmp', 'recursos/imagenes/enemigo002.bmp',lateral) 
            lista.append(armada)
            posx = posx + 50

def cargarBossLineal(lista,lateral):
       
        posx = 45
        for x in range(1,6):
            armada = Enemigo.jefe_enemigo(posx,50,40, 'recursos/imagenes/enemigo003.bmp', 'recursos/imagenes/enemigo004.bmp',lateral) 
            lista.append(armada)
            posx = posx + 50 
       
        
        posx = 45
        for x in range(1,6):
            armada = Enemigo.jefe_enemigo(posx,100,40, 'recursos/imagenes/enemigo003.bmp', 'recursos/imagenes/enemigo004.bmp',lateral) 
            lista.append(armada)
            posx = posx + 50
       
        
        posx = 45 
        for x in range(1,6):
            armada = Enemigo.jefe_enemigo(posx,150,40, 'recursos/imagenes/enemigo003.bmp', 'recursos/imagenes/enemigo004.bmp',lateral) 
            lista.append(armada)
            posx = posx + 50

def pantalla_carga(ventana,ancho,alto):
    ventana = pygame.display.set_mode((ancho,alto))
    imagenFondo = pygame.image.load(os.path.join('recursos','imagenes','carga.png'))

def pantalla_juego(ventana, ancho, alto):
    ventana = pygame.display.set_mode((ancho,alto))
    pygame.display.set_caption("Space Shoot")
    imagenFondo = pygame.image.load(os.path.join('recursos','imagenes','fondo.jpg'))

    

    