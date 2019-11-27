import pygame,sys, os, time
from pygame.locals import *
sys.path.append("/NAC/Desktop/PalomNation/Clases") #Agregar la ubicacion donde tengan las carpetas
from Clases import NaveEspacial
from Clases import Alien as Enemigo
from Clases import Proyectil
from Clases import Menu
from Clases import Opcion
from Clases import Cursor
from Clases import Niveles

ANCHO = 360
ALTO = 740
LISTA_ENEMIGOS = []
LISTA_ENEMIGOS2 = []

NEGRO = (0, 0, 0)

def NuevoJuego():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO,ALTO))
    imagenFondo = pygame.image.load(os.path.join('recursos','imagenes','fondo.jpg'))
    Niveles.pantalla_juego(ventana, ANCHO, ALTO)
    fuente = pygame.font.Font("recursos/fuentes//monolight.ttf", 30)
    textoVictoria = fuente.render("Todavia hay mas",45,(120,100,40))
    textoDerrota = fuente.render("Game Over",75,(254,0,227))
    pygame.mixer.music.load('recursos/audio/menu.mp3')
    pygame.mixer.music.play(4)
    
    jugador = NaveEspacial.nave()
    pygame.key.set_repeat(1)
    reloj = pygame.time.Clock()
    juego = True
    ventana.fill(NEGRO)
    Niveles.cargarEnemigosPiramide(LISTA_ENEMIGOS)
    while True:

        #Mayor es el tick, mayor es la velocidad de cambio
        reloj.tick(60)
        tiempo = reloj
        ventana.blit(imagenFondo,(0,0))
        jugador.movimiento()
        pygame.key.get_pressed()
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
                
                if event.type == pygame.KEYUP:
                    if event.key == K_s:
                        x,y = jugador.rect.center
                        jugador.disparar(x,y)                       
        ventana.blit(imagenFondo,(0,0))
        jugador.dibujar(ventana)
        
        jugador.colision(LISTA_ENEMIGOS,ventana,Enemigo.nave_enemiga,0)
        Enemigo.nave_enemiga.colision(LISTA_ENEMIGOS, tiempo,ventana,jugador, ALTO, ANCHO, textoDerrota)
        jugador.colision(LISTA_ENEMIGOS,ventana,Enemigo.jefe_enemigo,4)

        if jugador.Vida == False:
            ventana.blit(textoDerrota,(ANCHO/2,ALTO/5))
            
            
        if len(LISTA_ENEMIGOS) == 0 and jugador.Vida == True and jugador.nivel == False:
            time.sleep(3)
            jugador.nivel = True
            Niveles.pantalla_carga(ventana, ANCHO, ALTO)
            jugador.ganar()
            Niveles.cargarBossPiramide(LISTA_ENEMIGOS)
            Niveles.pantalla_juego(ventana,ANCHO, ALTO)    
            if len(LISTA_ENEMIGOS) == 0 and len(LISTA_ENEMIGOS2)== 0 and jugador.Vida == True: 
                jugador.ganar()
                ventana.blit(textoVictoria,(ANCHO/2,ALTO/5))
            
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

