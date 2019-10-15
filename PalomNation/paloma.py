import pygame, sys, os, time
ANCHO = 640
ALTO = 480
 
class Enemigo(pygame.sprite.Sprite):
    def __init__(self,posx,posy):
        pygame.sprite.Sprite.__init__(self)
        self.posx = posx
        self.posy = posy
        
        self.enemigo_imagenA  = pygame.image.load(os.path.join('recursos','imagenes','izq.png'))
        self.enemigo_imagenB  = pygame.image.load(os.path.join('recursos','imagenes','dos.png'))
        self.enemigo_imagenC  = pygame.image.load(os.path.join('recursos','imagenes','der.png'))

        self.listaImagenes = [self.enemigo_imagenA, self.enemigo_imagenB, self.enemigo_imagenC]
        self.posicionImagen = 0
    
        self.imagenEnemigo = self.listaImagenes[self.posicionImagen]
        self.rect = self.imagenEnemigo.get_rect()
        
        self.listaTiro = []
        self.velocidadTiro = 5
        self.velocidad = 25
        self.rect.top = posy
        self.rect.left = posx
        
        self.cambioImagen = 1
    	
        self.derecha = True
        self.contador = 0
        self.maxDescenso = self.rect.top+40
    	
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
            self.rect.top +=1
   
    def __movimientoLateral(self):
        if self.derecha == True:
            self.rect.left = self.rect.left+ self.velocidad
            if self.rect.left > 500:
                self.derecha = False
                self.contador +=1
        else:
            self.rect.left = self.rect.left - self.velocidad
            if self.rect.left <0:
                self.derecha = True
        
def juego():
    pygame.init()
    pantalle = pygame.display.set_mode((ANCHO,ALTO))
    ene = Enemigo(100,100)
    reloj = pygame.time.Clock()
    while True:
        #Mayor es el tick, mayor es la velocidad de cambio
        reloj.tick(1)
        tiempo = reloj
        ene.animacion(tiempo)
        
        ene.mostrar(pantalle)
        
        pygame.display.update()

juego()