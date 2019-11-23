import pygame,sys, os, time
from pygame.locals import *
sys.path.append("/NAC/Desktop/PalomNation/Clases") #Agregar la ubicacion donde tengan las carpetas
from Clases import NaveEspacial
from Clases import Alien as Enemigo
from Clases import Proyectil
from Clases import Menu
from Clases import Opcion
from Clases import Cursor

ANCHO = 360
ALTO = 740
LISTA_ENEMIGOS = []

NEGRO = (0, 0, 0)
def cargarEnemigos():
       #posx ubicacion inicial sobre el eje x se le suma 50 para que no queden las imagenes superpuestas
       #el segundo valor es la posicion sobre el eje y 
       #el tercer espacio es la distancia que recorre sobre el eje x
        posx = 45
        for x in range(1,6):
            armada = Enemigo.jefe_enemigo(posx,150,40, 'recursos/imagenes/enemigo003.bmp', 'recursos/imagenes/enemigo004.bmp') #Segundo valor distancia en y
            LISTA_ENEMIGOS.append(armada)
            posx = posx + 50 
       
        
        posx = 90
        for x in range(1,4):
            armada = Enemigo.jefe_enemigo(posx,100,80, 'recursos/imagenes/enemigo003.bmp', 'recursos/imagenes/enemigo004.bmp') #Segundo valor distancia en y
            LISTA_ENEMIGOS.append(armada)
            posx = posx + 75
       
        
        posx = 180 #Desplazamiento en x
        for x in range(1,2):
            armada = Enemigo.jefe_enemigo(posx,50,120, 'recursos/imagenes/enemigo003.bmp', 'recursos/imagenes/enemigo004.bmp') #Segundo valor distancia en y
            LISTA_ENEMIGOS.append(armada)
            posx = posx + 50
            
def detenerEnemigo():
    for armada in LISTA_ENEMIGOS:
        for disparo in armada.listaTiro:
            armada.listaTiro.remove(disparo)
        armada.conquista = True 


def NuevoJuego():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO,ALTO))
    pygame.display.set_caption("Space Shoot")
    imagenFondo = pygame.image.load(os.path.join('recursos','imagenes','fondo.jpg'))

    fuente = pygame.font.Font("recursos/fuentes//monolight.ttf", 30)
    textoVictoria = fuente.render("Todavía hay maaas",45,(120,100,40))
    textoDerrota = fuente.render("Game Over",75,(254,0,227))
    
    pygame.mixer.music.load('recursos/audio/menu.mp3')
    pygame.mixer.music.play(4)
    
    cargarEnemigos()
    jugador = NaveEspacial.nave()
    pygame.key.set_repeat(1)
    reloj = pygame.time.Clock()
    juego = True
    
   
    ventana.fill(NEGRO)
    
    while True:

        #Mayor es el tick, mayor es la velocidad de cambio
        reloj.tick(60)
        tiempo = reloj
        ventana.blit(imagenFondo,(0,0))
        jugador.movimiento()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if juego == True:
                if event.type == pygame.KEYDOWN:
                    if event.key == K_LEFT:
                        jugador.rect.left -= jugador.Velocidad
                        
                    elif event.key == K_RIGHT:
                        jugador.rect.right += jugador.Velocidad
                            
                        
                    elif event.key == K_s:
                        x,y = jugador.rect.center
                        jugador.disparar(x,y)
        
        ventana.blit(imagenFondo,(0,0))
        jugador.dibujar(ventana)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        if len(jugador.listaDisparo)>0:
            for x in jugador.listaDisparo:
                x.dibujar(ventana)
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
                armada.mostrar(ventana)
                if armada.rect.colliderect(jugador.rect): 
                    jugador.destruccion()
                    LISTA_ENEMIGOS.remove(armada)
                    juego = False
                    detenerEnemigo()
                if armada.rect.top > ALTO-20:
                    jugador.destruccion()
                    jugador.Vida = False
                    juego = False
                    detenerEnemigo()
                
                if len(armada.listaTiro)>0:
                    for x in armada.listaTiro:
                        x.dibujar(ventana)
                        x.trayectoria()
                        if x.rect.colliderect(jugador.rect):
                            jugador.destruccion()
                            juego = False
                            detenerEnemigo()
                        
                        if x.rect.top>900:
                            armada.listaTiro.remove(x)
                        else:
                            for disparo in jugador.listaDisparo:
                                if x.rect.colliderect(disparo.rect):
                                    jugador.listaDisparo.remove(disparo)
                                    armada.listaTiro.remove(x)
    
        if juego == False:
            ventana.blit(textoDerrota,(ANCHO/2,ALTO/5))

        if len(LISTA_ENEMIGOS) == 0 and jugador.Vida == True:
            jugador.ganar()
            ventana.blit(textoVictoria,(75,300))
        pygame.display.update()
    
def salir_del_programa():
    import sys
    sys.exit(0)

if __name__ == '__main__':
    
    salir = False
    #Lista de opciones que aparecerán en el menú
    opciones = [
        ("Jugar", NuevoJuego),
        ("Salir", salir_del_programa)
        ]
    pygame.init()
    pygame.font.init()

    jugador= NaveEspacial.nave()
    
    ventana= pygame.display.set_mode((ANCHO, ALTO ))
    pygame.display.set_caption("Space Shoot")
    fondo = pygame.image.load("recursos/imagenes/wea.bmp")
    menu = Menu.Menu(opciones)

    while not salir:
        for e in pygame.event.get():
            if e.type == QUIT:
                salir = True

        ventana.blit(fondo, (0, 0))
        menu.actualizar()
        menu.imprimir(ventana)

        pygame.display.flip()
        pygame.time.delay(10)

