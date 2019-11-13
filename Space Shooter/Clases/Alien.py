import pygame
from pygame.locals import *
from Clases import Proyectil
from random import randint

class nave_enemiga(pygame.sprite.Sprite):
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
        self.velocidadTiro = 450
        self.velocidad = 1
        self.rect.top = posy
        self.rect.left = posx
        
        self.cambioImagen = 1
    	
        self.derecha = True
        self.contador = 0
        self.maxDescenso = self.rect.top+40
        
        self.limiteDer= posx + distancia
        self.limiteIzq= posx - distancia
    	
        self.rangoDisparo = 1
        self.conquista = False 
        
    def mostrar(self, superficie):
        self.imagenEnemigo = self.listaImagenes[self.posicionImagen]
        superficie.blit(self.imagenEnemigo, self.rect)
        
    def animacion(self,tiempo):
        
        if self.conquista == False:
            self.__movimientos()

            self.__ataque()
    
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
                
    def __ataque(self):
        if (randint(0,600)<self.rangoDisparo):
            self.__disparo()

    def __disparo(self):
        x,y = self.rect.center
        miProyectil = Proyectil.Proyectil(x,y,'recursos/imagenes/tiro2.bmp',False)
        self.listaTiro.append(miProyectil)
