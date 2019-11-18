import pygame, sys, os, time
from pygame.locals import *
sys.path.append("/kaizer/escritorio/Space shoot/Clases")
from Clases import NaveEspacial
from Clases import Proyectil
from Clases import Alien as Enemigo

ancho=360
alto=740
inicio: False
celeste= (0,197,255)
blanco= (255,255,255)
negro = (0, 0, 0)
rel= pygame.time.Clock()
LISTA_ENEMIGOS = []

class Opcion:

    def __init__(self, fuente, titulo, x, y, paridad, funcion_asignada):
        self.imagen_normal = fuente.render(titulo, 1, (celeste))
        self.imagen_destacada = fuente.render(titulo, 1, (blanco))
        self.image = self.imagen_normal
        self.rect = self.image.get_rect()
        self.rect.x = 500 * paridad
        self.rect.y = y
        self.funcion_asignada = funcion_asignada
        self.x = float(self.rect.x)

    def actualizar(self):
        destino_x = 105
        self.x += (destino_x - self.x) / 5.0
        self.rect.x = int(self.x)

    def imprimir(self, screen):
        screen.blit(self.image, self.rect)

    def destacar(self, estado):
        if estado:
            self.image = self.imagen_destacada
        else:
            self.image = self.imagen_normal

    def activar(self):
        self.funcion_asignada()

class Cursor:

    def __init__(self, x, y, dy):
        self.image = pygame.image.load('imagenes/cursor.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.y_inicial = y
        self.dy = dy
        self.y = 0
        self.seleccionar(0)

    def actualizar(self):
        self.y += (self.to_y - self.y) / 10.0
        self.rect.y = int(self.y)

    def seleccionar(self, indice):
        self.to_y = self.y_inicial + indice * self.dy

    def imprimir(self, screen):
        screen.blit(self.image, self.rect)

class Menu:
    #Representa un menú con opciones para un juego
    def __init__(self, opciones):

    
        self.opciones = []
        fuente = pygame.font.Font('Fuente/monolight.ttf', 20)
        x = 150
        y = 360
        paridad = 1

        self.cursor = Cursor(x - 80, y, 30)

        for titulo, funcion in opciones:
            self.opciones.append(Opcion(fuente, titulo, x, y, paridad, funcion))
            y += 30
            if paridad == 1:
                paridad = -1
            else:
                paridad = 1

        self.seleccionado = 0
        self.total = len(self.opciones)
        self.mantiene_pulsado = False

    def actualizar(self):
        """Altera el valor de 'self.seleccionado' con los direccionales."""

        k = pygame.key.get_pressed()

        if not self.mantiene_pulsado:
            if k[K_UP]:
                self.seleccionado -= 1
            elif k[K_DOWN]:
                self.seleccionado += 1
            elif k[K_RETURN]:
                # Invoca a la función asociada a la opción.
                self.opciones[self.seleccionado].activar()

        # procura que el cursor esté entre las opciones permitidas
        if self.seleccionado < 0:
            self.seleccionado = 0
        elif self.seleccionado > self.total - 1:
            self.seleccionado = self.total - 1
        
        self.cursor.seleccionar(self.seleccionado)

        # indica si el usuario mantiene pulsada alguna tecla.
        self.mantiene_pulsado = k[K_UP] or k[K_DOWN] or k[K_RETURN]

        self.cursor.actualizar()
     
        for o in self.opciones:
            o.actualizar()

    def imprimir(self, screen):
        """Imprime sobre la pantalla el texto de cada opción del menú."""
    
        self.cursor.imprimir(screen)

        for opcion in self.opciones:
            opcion.imprimir(screen)

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
    ventana  = pygame.display.set_mode((ancho,alto))
    pygame.display.set_caption("Space Shoot")
    imagenFondo = pygame.image.load('Imagenes/fondo.jpg')

    fuente1= pygame.font.Font("Fuente/monolight.ttf", 30)
    textoVictoria = fuente1.render("Aun hay mas",30,(120,100,40))
    texto = fuente1.render("Game Over",30,(254,0,227))
   
    pygame.mixer.music.load("Sonidos/menu.mp3")
    pygame.mixer.music.play(4)

    cargarEnemigos()
    jugador = NaveEspacial.nave()
    juego = True
    pygame.key.set_repeat(1)

    while True:
        #Mayor es el tick, mayor es la velocidad de cambio
        rel.tick(60)
        tiempo = rel
        ventana.blit(imagenFondo,(0,0))
        jugador.movimiento()

        Juego=True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if Juego == True:
                if event.type == pygame.KEYDOWN:
                    if event.key == K_LEFT:
                        jugador.rect.left -= jugador.Velocidad
                        
                    elif event.key == K_RIGHT:
                        jugador.rect.right += jugador.Velocidad
                            
                        
                    elif event.key == K_s:
                        x,y = jugador.rect.center
                        jugador.disparar(x-8,y-28)
        
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
                    enJuego = False
                    detenerEnemigo()
                if armada.rect.top > alto-20:
                    jugador.destruccion()
                    Juego = False
                    detenerEnemigo()
                
                if len(armada.listaTiro)>0:
                    for x in armada.listaTiro:
                        x.dibujar(ventana)
                        x.trayectoria()
                        if x.rect.colliderect(jugador.rect):
                            jugador.destruccion()
                            Juego = False
                            detenerEnemigo()
                        
                        if x.rect.top>900:
                            armada.listaTiro.remove(x)
                        else:
                            for disparo in jugador.listaDisparo:
                                if x.rect.colliderect(disparo.rect):
                                    jugador.listaDisparo.remove(disparo)
                                    armada.listaTiro.remove(x)
    
        if Juego == False:
            ventana.blit(texto,(ancho/2,alto/5))

        if len(LISTA_ENEMIGOS) == 0:
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

    pygame.font.init()

    jugador= NaveEspacial.nave()
    
    ventana= pygame.display.set_mode((ancho, alto ))
    pygame.display.set_caption("Space Shoot")
    fondo = pygame.image.load("imagenes/wea.bmp")
    menu = Menu(opciones)

    while not salir:
        for e in pygame.event.get():
            if e.type == QUIT:
                salir = True

        ventana.blit(fondo, (0, 0))
        menu.actualizar()
        menu.imprimir(ventana)

        pygame.display.flip()
        pygame.time.delay(10)
