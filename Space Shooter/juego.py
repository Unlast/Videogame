import pygame,sys, os, time
from pygame.locals import *
sys.path.append("/NAC/Desktop/PalomNation/Clases") #Agregar la ubicacion donde tengan las carpetas
print(sys.path)
from Clases import NaveEspacial
from Clases import Alien as Enemigo

ANCHO = 640
ALTO = 480
LISTA_ENEMIGOS = []
blanco = 0,0,0

def cargarEnemigos():
   
    posx = 200
    for x in range(1,6):
        armada = Enemigo.nave_enemiga(posx,150,40, 'recursos/imagenes/enemigo001.bmp', 'recursos/imagenes/enemigo002.bmp') #Segundo valor distancia en y
        LISTA_ENEMIGOS.append(armada)
        posx = posx + 50 
   
    
    posx = 300
    for x in range(1,4):
        armada = Enemigo.nave_enemiga(posx,100,80, 'recursos/imagenes/enemigo001.bmp', 'recursos/imagenes/enemigo002.bmp')
        LISTA_ENEMIGOS.append(armada)
        posx = posx + 75
   
    
    posx = 400 #Desplazamiento en x
    for x in range(1,2):
        armada = Enemigo.nave_enemiga(posx,50,120, 'recursos/imagenes/enemigo001.bmp', 'recursos/imagenes/enemigo002.bmp') #Segundo valor distancia en y
        LISTA_ENEMIGOS.append(armada)
        posx = posx + 50
        
def NuevoJuego():
    pygame.init()
    pantalle = pygame.display.set_mode((ANCHO,ALTO))
    jugador = NaveEspacial.nave()
    pygame.key.set_repeat(10)
    cargarEnemigos()
    reloj = pygame.time.Clock()
    imagenFondo = pygame.image.load(os.path.join('recursos','imagenes','fondo.png'))
    enJuego = True
    pygame.key.set_repeat(10)

    while True:
        #Mayor es el tick, mayor es la velocidad de cambio
        reloj.tick(30)
        tiempo = reloj
        pantalle.blit(imagenFondo,(0,0))
        jugador.movimiento()
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if enJuego == True:
                if event.type == pygame.KEYDOWN:
                    if event.key == K_LEFT:
                        jugador.rect.left -= jugador.Velocidad
                        
                    elif event.key == K_RIGHT:
                        jugador.rect.right += jugador.Velocidad
                            
                        
                    elif event.key == K_s:
                        jugador.disparar()
        jugador.dibujar(pantalle)
        for armada in LISTA_ENEMIGOS:
            armada.animacion(tiempo)
            armada.mostrar(pantalle)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()


NuevoJuego()
