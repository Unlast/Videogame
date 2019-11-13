import pygame,sys, os, time
from pygame.locals import *
sys.path.append("/NAC/Desktop/PalomNation/Clases") #Agregar la ubicacion donde tengan las carpetas
print(sys.path)
from Clases import NaveEspacial
from Clases import Alien as Enemigo
from Clases import Proyectil

ANCHO = 640
ALTO = 480
LISTA_ENEMIGOS = []
blanco = 0,0,0

def detener():
    for armada in LISTA_ENEMIGOS:
        for disparo in armada.listaTiro:
            armada.listaTiro.remove(disparo)
        armada.conquista = True 
        
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
    fuente = pygame.font.SysFont("Arial",30)
    texto = fuente.render("Game Over",0,(120,100,40))
    
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
                        x,y = jugador.rect.center
                        jugador.disparar(x,y)
        
        pantalle.blit(imagenFondo,(0,0))
        jugador.dibujar(pantalle)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        if len(jugador.listaDisparo)>0:
            for x in jugador.listaDisparo:
                x.dibujar(pantalle)
                x.trayectoria()  
                if x.rect.top<-10:
                    jugador.listaDisparo.remove(x)
                else:    
                    for armada in LISTA_ENEMIGOS:
                        if x.rect.colliderect(armada.rect):
                            LISTA_ENEMIGOS.remove(armada)
                            jugador.listaDisparo.remove(x)
    
        if len(LISTA_ENEMIGOS)>0:
            for armada in LISTA_ENEMIGOS:
                armada.animacion(tiempo)
                armada.mostrar(pantalle)
                
                if armada.rect.colliderect(jugador.rect):
                    jugador.destruccion()
                    enJuego = False
                    detener()
                
                if len(armada.listaTiro)>0:
                    for x in armada.listaTiro:
                        x.dibujar(pantalle)
                        x.trayectoria()
                        if x.rect.colliderect(jugador.rect):
                            jugador.destruccion()
                            enJuego = False
                            detener()
                        
                        if x.rect.top>900:
                            armada.listaTiro.remove(x)
                        else:
                            for disparo in jugador.listaDisparo:
                                if x.rect.colliderect(disparo.rect):
                                    jugador.listaDisparo.remove(disparo)
                                    armada.listaTiro.remove(x)
    
            
        if enJuego == False:
            pantalle.blit(texto,(300,300))
        pygame.display.update()


NuevoJuego()
