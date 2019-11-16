import pygame,sys, os, time
from pygame.locals import *
sys.path.append("/NAC/Desktop/PalomNation/Clases") #Agregar la ubicacion donde tengan las carpetas
from Clases import NaveEspacial
from Clases import Alien as Enemigo
from Clases import Proyectil

ANCHO = 360
ALTO = 740
LISTA_ENEMIGOS = []

NEGRO = (0, 0, 0)
def cargarEnemigos():
       #posx ubicacion inicial sobre el eje x se le suma 50 para que no queden las imagenes superpuestas
       #el segundo valor es la posicion sobre el ej
       #el tercer espacio es la distancia que recorre sobre el eje x
        posx = 45
        for x in range(1,6):
            armada = Enemigo.nave_enemiga(posx,150,40, 'recursos/imagenes/enemigo001.bmp', 'recursos/imagenes/enemigo002.bmp') #Segundo valor distancia en y
            LISTA_ENEMIGOS.append(armada)
            posx = posx + 50 
       
        
        posx = 90
        for x in range(1,4):
            armada = Enemigo.nave_enemiga(posx,100,80, 'recursos/imagenes/enemigo001.bmp', 'recursos/imagenes/enemigo002.bmp')
            LISTA_ENEMIGOS.append(armada)
            posx = posx + 75
       
        
        posx = 180 #Desplazamiento en x
        for x in range(1,2):
            armada = Enemigo.nave_enemiga(posx,50,120, 'recursos/imagenes/enemigo001.bmp', 'recursos/imagenes/enemigo002.bmp') #Segundo valor distancia en y
            LISTA_ENEMIGOS.append(armada)
            posx = posx + 50
def detenerEnemigo():
    for armada in LISTA_ENEMIGOS:
        for disparo in armada.listaTiro:
            armada.listaTiro.remove(disparo)
        armada.conquista = True 


def NuevoJuego():
    pygame.init()
    pygame.mixer.music.load('recursos/audio/marcha.mp3')
    pygame.mixer.music.play(2)
    pantalle = pygame.display.set_mode((ANCHO,ALTO))
    jugador = NaveEspacial.nave()
    cargarEnemigos()
    pygame.key.set_repeat(10)
    reloj = pygame.time.Clock()
    imagenFondo = pygame.image.load(os.path.join('recursos','imagenes','fondo.png'))
    enJuego = True
    pygame.key.set_repeat(10)
    fuente = pygame.font.SysFont("Arial",30)
    textoVictoria = fuente.render("Todavía hay maaas",45,(120,100,40))
    texto = fuente.render("Game Over",75,(254,0,227))
   
    pantalle.fill(NEGRO)
    
    while True:

        #Mayor es el tick, mayor es la velocidad de cambio
        reloj.tick(60)
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
                    LISTA_ENEMIGOS.remove(armada)
                    enJuego = False
                    detenerEnemigo()
                if armada.rect.top > ALTO-20:
                    jugador.destruccion()
                    enJuego = False
                    detenerEnemigo()
                
                if len(armada.listaTiro)>0:
                    for x in armada.listaTiro:
                        x.dibujar(pantalle)
                        x.trayectoria()
                        if x.rect.colliderect(jugador.rect):
                            jugador.destruccion()
                            enJuego = False
                            detenerEnemigo()
                        
                        if x.rect.top>900:
                            armada.listaTiro.remove(x)
                        else:
                            for disparo in jugador.listaDisparo:
                                if x.rect.colliderect(disparo.rect):
                                    jugador.listaDisparo.remove(disparo)
                                    armada.listaTiro.remove(x)
    
        if enJuego == False:
            pantalle.blit(texto,(ANCHO/2,300))

        if len(LISTA_ENEMIGOS) == 0:
            jugador.ganar()
            pantalle.blit(textoVictoria,(75,300))

        pygame.display.update()

NuevoJuego()
