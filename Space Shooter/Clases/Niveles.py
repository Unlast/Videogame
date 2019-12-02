import pygame, os
from Clases import Alien as Enemigo
LISTA_ENEMIGOS = []


def cargarEnemigosPiramide(lista,lateral):
       #posx ubicacion inicial sobre el eje x se le suma 50 para que no queden las imagenes superpuestas
       #el segundo valor es la posicion sobre el eje y 
       #el tercer espacio es la distancia que recorre sobre el eje x
        posx = 45
        for x in range(1,6):
            armada = Enemigo.nave_enemiga(posx,200,40, 'recursos/imagenes/enemigo001.bmp', 'recursos/imagenes/enemigo002.bmp',lateral) #Segundo valor distancia en y
            lista.append(armada)
            posx = posx + 50 
       
        
        posx = 90
        for x in range(1,4):
            armada = Enemigo.nave_enemiga(posx,250,80, 'recursos/imagenes/enemigo001.bmp', 'recursos/imagenes/enemigo002.bmp',lateral) #Segundo valor distancia en y
            lista.append(armada)
            posx = posx + 75
       
        
        posx = 180 #Desplazamiento en x
        for x in range(1,2):
            armada = Enemigo.nave_enemiga(posx,300,120, 'recursos/imagenes/enemigo001.bmp', 'recursos/imagenes/enemigo002.bmp',lateral) #Segundo valor distancia en y
            lista.append(armada)
            posx = posx + 50


def cargarEnemigosPiramideI(lista):
       #posx ubicacion inicial sobre el eje x se le suma 50 para que no queden las imagenes superpuestas
       #el segundo valor es la posicion sobre el eje y 
       #el tercer espacio es la distancia que recorre sobre el eje x
        posx = 180
        for x in range(1,2):
            armada = Enemigo.nave_enemiga(posx,200,120, 'recursos/imagenes/enemigo001.bmp', 'recursos/imagenes/enemigo002.bmp',3) #Segundo valor distancia en y
            lista.append(armada)
            posx = posx + 50 
       
        
        posx = 90
        for x in range(1,4):
            armada = Enemigo.nave_enemiga(posx,250,80, 'recursos/imagenes/enemigo001.bmp', 'recursos/imagenes/enemigo002.bmp',5) #Segundo valor distancia en y
            lista.append(armada)
            posx = posx + 75
       
        
        posx = 90 #Desplazamiento en x
        for x in range(1,6):
            armada = Enemigo.nave_enemiga(posx,300,40, 'recursos/imagenes/enemigo001.bmp', 'recursos/imagenes/enemigo002.bmp',10) #Segundo valor distancia en y
            lista.append(armada)
            posx = posx + 50      
        
        
def cargarBossPiramide(lista,lateral):
     #posx ubicacion inicial sobre el eje x se le suma 50 para que no queden las imagenes superpuestas
       #el segundo valor es la posicion sobre el eje y 
       #el tercer espacio es la distancia que recorre sobre el eje x
        posx = 45
        for x in range(1,6):
            armada = Enemigo.jefe_enemigo(posx,150,40, 'recursos/imagenes/enemigo003.bmp', 'recursos/imagenes/enemigo004.bmp',lateral) #Segundo valor distancia en y
            lista.append(armada)
            posx = posx + 50 
       
        
        posx = 90
        for x in range(1,4):
            armada = Enemigo.jefe_enemigo(posx,100,80, 'recursos/imagenes/enemigo003.bmp', 'recursos/imagenes/enemigo004.bmp',lateral) #Segundo valor distancia en y            
            lista.append(armada)
            posx = posx + 75
       
        
        posx = 180 #Desplazamiento en x
        for x in range(1,2):
            armada = Enemigo.jefe_enemigo(posx,50,120, 'recursos/imagenes/enemigo003.bmp', 'recursos/imagenes/enemigo004.bmp',lateral) #Segundo valor distancia en y
            lista.append(armada)
            posx = posx + 50

        
def cargarBossPiramideI(lista):
     #posx ubicacion inicial sobre el eje x se le suma 50 para que no queden las imagenes superpuestas
       #el segundo valor es la posicion sobre el eje y 
       #el tercer espacio es la distancia que recorre sobre el eje x
        posx = 90
        for x in range(1,6):
            armada = Enemigo.jefe_enemigo(posx,150,40, 'recursos/imagenes/enemigo003.bmp', 'recursos/imagenes/enemigo004.bmp',2) #Segundo valor distancia en y
            lista.append(armada)
            posx = posx + 50 
        
        posx = 90
        for x in range(1,4):
            armada = Enemigo.jefe_enemigo(posx,100,80, 'recursos/imagenes/enemigo003.bmp', 'recursos/imagenes/enemigo004.bmp',4) #Segundo valor distancia en y            
            lista.append(armada)
            posx = posx + 75
       
        
        posx = 180 #Desplazamiento en x
        for x in range(1,2):
            armada = Enemigo.jefe_enemigo(posx,50,120, 'recursos/imagenes/enemigo003.bmp', 'recursos/imagenes/enemigo004.bmp',8) #Segundo valor distancia en y
            lista.append(armada)
            posx = posx + 50


def cargarEnemigosLineal(lista,lateral):
       #posx ubicacion inicial sobre el eje x se le suma 50 para que no queden las imagenes superpuestas
       #el segundo valor es la posicion sobre el eje y 
       #el tercer espacio es la distancia que recorre sobre el eje x
        posx = 45
        for x in range(1,6):
            armada = Enemigo.nave_enemiga(posx,150,40, 'recursos/imagenes/enemigo001.bmp', 'recursos/imagenes/enemigo002.bmp',lateral) #Segundo valor distancia en y
            lista.append(armada)
            posx = posx + 50 
       
        
        posx = 45
        for x in range(1,6):
            armada = Enemigo.nave_enemiga(posx,100,40, 'recursos/imagenes/enemigo001.bmp', 'recursos/imagenes/enemigo002.bmp',lateral) #Segundo valor distancia en y
            lista.append(armada)
            posx = posx + 50
       
        
        posx = 45 #Desplazamiento en x
        for x in range(1,6):
            armada = Enemigo.nave_enemiga(posx,50,40, 'recursos/imagenes/enemigo001.bmp', 'recursos/imagenes/enemigo002.bmp',lateral) #Segundo valor distancia en y
            lista.append(armada)
            posx = posx + 50

def cargarBossLineal(lista,lateral):
       #posx ubicacion inicial sobre el eje x se le suma 50 para que no queden las imagenes superpuestas
       #el segundo valor es la posicion sobre el eje y 
       #el tercer espacio es la distancia que recorre sobre el eje x
        posx = 45
        for x in range(1,6):
            armada = Enemigo.jefe_enemigo(posx,200,40, 'recursos/imagenes/enemigo003.bmp', 'recursos/imagenes/enemigo004.bmp',lateral) #Segundo valor distancia en y
            lista.append(armada)
            posx = posx + 50 
       
        
        posx = 45
        for x in range(1,6):
            armada = Enemigo.jefe_enemigo(posx,250,40, 'recursos/imagenes/enemigo003.bmp', 'recursos/imagenes/enemigo004.bmp',lateral) #Segundo valor distancia en y
            lista.append(armada)
            posx = posx + 50
       
        
        posx = 45 #Desplazamiento en x
        for x in range(1,6):
            armada = Enemigo.jefe_enemigo(posx,300,40, 'recursos/imagenes/enemigo003.bmp', 'recursos/imagenes/enemigo004.bmp',lateral) #Segundo valor distancia en y
            lista.append(armada)
            posx = posx + 50

def pantalla_carga(ventana,ancho,alto):
    ventana = pygame.display.set_mode((ancho,alto))
    imagenFondo = pygame.image.load(os.path.join('recursos','imagenes','carga.png'))

def pantalla_juego(ventana, ancho, alto):
    ventana = pygame.display.set_mode((ancho,alto))
    pygame.display.set_caption("Space Shoot")
    imagenFondo = pygame.image.load(os.path.join('recursos','imagenes','fondo.jpg'))

    

    