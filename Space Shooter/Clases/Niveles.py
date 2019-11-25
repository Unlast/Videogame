from Clases import Alien as Enemigo
LISTA_ENEMIGOS = []


def cargarEnemigos(lista):
       #posx ubicacion inicial sobre el eje x se le suma 50 para que no queden las imagenes superpuestas
       #el segundo valor es la posicion sobre el eje y 
       #el tercer espacio es la distancia que recorre sobre el eje x
        posx = 45
        for x in range(1,6):
            armada = Enemigo.nave_enemiga(posx,150,40, 'recursos/imagenes/enemigo001.bmp', 'recursos/imagenes/enemigo002.bmp') #Segundo valor distancia en y
            lista.append(armada)
            posx = posx + 50 
       
        
        posx = 90
        for x in range(1,4):
            armada = Enemigo.nave_enemiga(posx,100,80, 'recursos/imagenes/enemigo001.bmp', 'recursos/imagenes/enemigo002.bmp') #Segundo valor distancia en y
            lista.append(armada)
            posx = posx + 75
       
        
        posx = 180 #Desplazamiento en x
        for x in range(1,2):
            armada = Enemigo.nave_enemiga(posx,50,120, 'recursos/imagenes/enemigo001.bmp', 'recursos/imagenes/enemigo002.bmp') #Segundo valor distancia en y
            lista.append(armada)
            posx = posx + 50

def cargarBoss(lista):
     #posx ubicacion inicial sobre el eje x se le suma 50 para que no queden las imagenes superpuestas
       #el segundo valor es la posicion sobre el eje y 
       #el tercer espacio es la distancia que recorre sobre el eje x
        posx = 45
        for x in range(1,6):
            armada = Enemigo.jefe_enemigo(posx,150,40, 'recursos/imagenes/enemigo003.bmp', 'recursos/imagenes/enemigo004.bmp') #Segundo valor distancia en y
            lista.append(armada)
            posx = posx + 50 
       
        
        posx = 90
        for x in range(1,4):
            armada = Enemigo.jefe_enemigo(posx,100,80, 'recursos/imagenes/enemigo003.bmp', 'recursos/imagenes/enemigo004.bmp') #Segundo valor distancia en y
            lista.append(armada)
            posx = posx + 75
       
        
        posx = 180 #Desplazamiento en x
        for x in range(1,2):
            armada = Enemigo.jefe_enemigo(posx,50,120, 'recursos/imagenes/enemigo003.bmp', 'recursos/imagenes/enemigo004.bmp') #Segundo valor distancia en y
            lista.append(armada)
            posx = posx + 50