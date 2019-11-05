import pygame, sys, os, time
from pygame.locals import *

ANCHO = 800
ALTO = 600
LISTA_ENEMIGOS = []
class Enemigo(pygame.sprite.Sprite):
    def __init__(self,posx,posy, distancia, imagenUno, imagenDos):
        pygame.sprite.Sprite.__init__(self)
        self.posx = posx
        self.posy = posy
        
        self.enemigo_imagenA  = pygame.image.load(imagenUno)
        self.enemigo_imagenB  = pygame.image.load(imagenDos)

        self.listaImagenes = [self.enemigo_imagenA, self.enemigo_imagenB]
        self.posicionImagen = 0
    
        self.imagenEnemigo = self.listaImagenes[self.posicionImagen]
        self.rect = self.imagenEnemigo.get_rect()
        
        self.listaTiro = []
        self.velocidadTiro = 5
        self.velocidad = 50
        self.rect.top = posy
        self.rect.left = posx
        
        self.cambioImagen = 1
    	
        self.derecha = True
        self.contador = 0
        self.maxDescenso = self.rect.top+40
        
        self.limiteDer= posx + distancia
        self.limiteIzq= posx - distancia
    	
    def mostrar(self, superficie):
        self.imagenEnemigo = self.listaImagenes[self.posicionImagen]
        superficie.blit(self.imagenEnemigo, self.rect)
        
    def animacion(self,tiempo):
        self.__movimientos()
        
        if  self.posicionImagen>=len(self.listaImagenes)-1:
            self.posicionImagen = 0
        else:
            self.posicionImagen +=1
    
    def __movimientos(self):
        if self.contador <3:
            self.__movimientoLateral()
        else:
            self.__descenso()
    
    def __descenso(self):
        if self.maxDescenso == self.rect.top:
            self.contador =0
            self.maxDescenso = self.rect.top + 40
        else:
            self.rect.top +=20
   
    def __movimientoLateral(self):
        if self.derecha == True:
            self.rect.left = self.rect.left+ self.velocidad
            if self.rect.left > self.limiteDer:
                self.derecha = False
                self.contador +=1
        else:
            self.rect.left = self.rect.left - self.velocidad
            if self.rect.left <self.limiteIzq:
                self.derecha = True
                
def cargarEnemigos():
   
    posx = 350
    for x in range(1,6):
        armada = Enemigo(posx,150,40, 'recursos/imagenes/enemigo001.bmp', 'recursos/imagenes/enemigo002.bmp') #Segundo valor distancia en y
        LISTA_ENEMIGOS.append(armada)
        posx = posx + 50 
   
    
    posx = 300
    for x in range(1,4):
        armada = Enemigo(posx,100,80, 'recursos/imagenes/enemigo001.bmp', 'recursos/imagenes/enemigo002.bmp')
        LISTA_ENEMIGOS.append(armada)
        posx = posx + 75
   
    
    posx = 600 #Desplazamiento en x
    for x in range(1,2):
        armada = Enemigo(posx,50,120, 'recursos/imagenes/enemigo001.bmp', 'recursos/imagenes/enemigo002.bmp') #Segundo valor distancia en y
        LISTA_ENEMIGOS.append(armada)
        posx = posx + 50
    
def juego():
    pygame.init()
    pantalle = pygame.display.set_mode((ANCHO,ALTO))
    cargarEnemigos()
    reloj = pygame.time.Clock()
    imagenFondo = pygame.image.load(os.path.join('recursos','imagenes','fondo.png'))
    
    while True:
        #Mayor es el tick, mayor es la velocidad de cambio
        reloj.tick(1)
        tiempo = reloj
        pantalle.blit(imagenFondo,(0,0))
        
        for armada in LISTA_ENEMIGOS:
            armada.animacion(tiempo)
            armada.mostrar(pantalle)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

juego()
