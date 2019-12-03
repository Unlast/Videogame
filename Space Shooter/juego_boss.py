import pygame,sys, os, time, sqlite3
from pygame.locals import *
sys.path.append("/NAC/Desktop/UNLa/Seminario-de-Lenguajes/Space-Shooter/Clases") #Agregar la ubicacion donde tengan las carpetas
from Clases import NaveEspacial
from Clases import Alien as Enemigo
from Clases import Menu
from Clases import Niveles
from Clases import BD
"""
Se importan los módulos a utilizar, se agregan el módulo Clases propio del juego y las clases a utilizar
Se inicia pygame, se define el alto y ancho de la pantalla, 2 colores, la fuente a utilizar
el texto de pausa y se crea la pantalla.
"""
pygame.init()    
ANCHO = 360
ALTO = 740
LISTA_ENEMIGOS = []
NEGRO = (0, 0, 0)
BLANCO = (255,255,255)
fuente = pygame.font.Font("recursos/fuentes//monolight.ttf", 30)
textoPausa = fuente.render("C continua, Q salir",50,(255,255,255))
ventana = pygame.display.set_mode((ANCHO,ALTO))

def conectar():
    """
    Conectar: coneecta a la base de datos donde se guardan los 5 puntajes mas altos
    """
    conexion = sqlite3.connect("BdSpaceShoot.db")


def pausa():
    """
    Pausa: Si se presiona la letra P se pausa el juego, C para continuar, Q para salir
    """

    pausado = True
    while pausado:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    pausado = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    exit()
        ventana.blit(textoPausa,(50,ALTO/5))
        pygame.display.update()
        
def pantalla_principal():
    """
    Pantalla Principal: muestra la pantalla de inicio con las opciones a seleccionar
    """
    ventana= pygame.display.set_mode((ANCHO, ALTO ))
    salir = False
    #Lista de opciones que aparecerán en el menú
    opciones = [
        ("Jugar", NuevoJuego),
        ("Salir", salir_del_programa)
        ]
   

    jugador= NaveEspacial.nave()
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

def NuevoJuego():
    """
    NuevoJuego: contiene el bucle While donde se ejecuta la lógica del juego, música textos a mostrar en caso de Victoria o Derrota
    la instancia de enemigos. Dentro del bucle se pone los FPS y controles. La cantidad
    de colisiones contra los enemigos en el caso que se necesite. Se evalua las condiciones de derrota
    pasar de nivel y ganar el juego.
    """
    conectar()
    ventana = pygame.display.set_mode((ANCHO,ALTO))
    imagenFondo = pygame.image.load(os.path.join('recursos','imagenes','fondo.jpg'))
    Niveles.pantalla_juego(ventana, ANCHO, ALTO)
    textoVictoria = fuente.render("¡Los eliminaste!",45,(255,255,255))
    textoDerrota = fuente.render("A casa",75,(254,0,227))
    pygame.mixer.music.load('recursos/audio/menu.mp3')
    pygame.mixer.music.play(4)
    jugador = NaveEspacial.nave()
    jugador.mostrar_puntos(ventana)
    pygame.key.set_repeat(1)
    reloj = pygame.time.Clock()
    juego = True
    ventana.fill(NEGRO)
    Niveles.cargarBossPiramideI(LISTA_ENEMIGOS)
    Niveles.cargarEnemigosPiramide(LISTA_ENEMIGOS)
    mostrarDatos = False
    contadorDatos = 0
    while True:

        #Mayor es el tick, mayor es la velocidad de cambio
        reloj.tick(60)
        tiempo = reloj
        ventana.blit(imagenFondo,(0,0))
        jugador.movimiento()
        pygame.key.get_pressed()
        for event in pygame.event.get():
            jugador.mostrar_puntos(ventana)
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                
            if juego == True:
                if event.type == pygame.KEYDOWN:
                    if event.key == K_LEFT:
                        jugador.rect.left -= jugador.Velocidad
                                
                    elif event.key == K_RIGHT:
                        jugador.rect.right += jugador.Velocidad
                    
                    elif event.key == K_p:
                        pausa()
                if event.type == pygame.KEYUP:
                    if event.key == K_s:
                        x,y = jugador.rect.center
                        jugador.disparar(x,y)      
                
                    elif event.key == K_z:
                        jugador.destruccion_total(LISTA_ENEMIGOS)
                       

                    elif event.key == K_r:
                        for x in range(1,6):
                            jugador.destruccion_total(LISTA_ENEMIGOS)
                        pantalla_principal()
                        
                    elif event.key == K_v:
                        pygame.mixer.music.stop()
                        pygame.mixer.music.load('recursos/audio/marcha.mp3')
                        pygame.mixer.music.play(4)

                    elif event.key == K_b:
                        pygame.mixer.music.stop()
                        pygame.mixer.music.load('recursos/audio/menu.mp3')
                        pygame.mixer.music.play(4)
    
        ventana.blit(imagenFondo,(0,0))
        jugador.mostrar_puntos(ventana)

        jugador.dibujar(ventana)
        jugador.colision(LISTA_ENEMIGOS,ventana,Enemigo.nave_enemiga,0)
        Enemigo.nave_enemiga.colision(LISTA_ENEMIGOS, tiempo,ventana,jugador, ALTO, ANCHO, textoDerrota)
        jugador.colision(LISTA_ENEMIGOS,ventana,Enemigo.jefe_enemigo,2)

        if jugador.Vida == False:
            ventana.blit(textoDerrota,(110,ALTO/2))
            juego = False
            for x in range(1,6):
                jugador.destruccion_total(LISTA_ENEMIGOS)
            
        if len(LISTA_ENEMIGOS) == 0 and jugador.Vida == True and jugador.nivel == False:
            jugador.pasar_nivel2(LISTA_ENEMIGOS, ventana)    
       
        if len(LISTA_ENEMIGOS) == 0 and jugador.Vida == True and jugador.nivel == True:
            jugador.ganar()
            juego = False
            Niveles.pantalla_carga(ventana,ANCHO,ALTO)
            ventana.blit(textoVictoria,(67,ALTO/2))
            if contadorDatos == 0:
                BD.agregar(jugador.puntuacion)
                BD.ordenar()
                contadorDatos +=1
             
        
                
        pygame.display.update()

def salir_del_programa():
    import sys
    pygame.quit()
    exit()

if __name__ == '__main__':
   pantalla_principal()

