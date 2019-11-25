import pygame, os
from pygame.locals import *
from Clases import Proyectil
ANCHO = 360
ALTO = 740

class nave(pygame.sprite.Sprite):
    
    def __init__(self):
        
        pygame.sprite.Sprite.__init__(self)
        self.ImagenPersonaje = pygame.image.load('recursos/imagenes/nave001.bmp')
        self.rect = self.ImagenPersonaje.get_rect()
        self.rect.centerx = ANCHO/2
        self.rect.centery = ALTO-20
        self.listaDisparo = []
        self.Vida = True
        self.Velocidad = 2
        self.ImagenExplosion = pygame.image.load('recursos/imagenes/explosion.bmp')
        self.sonidoDisparo = pygame.mixer.Sound('recursos/audio/disparo2.ogg')
        self.sonidoDestruccion = pygame.mixer.Sound('recursos/audio/explosion1.ogg')
        self.victoria = False
        self.disparo = False
        
    def movimiento(self):
        if self.Vida == True:
            if self.rect.left <=0:
                self.rect.left =0
                
            elif self.rect.right >=360:
                self.rect.right = 360
    
    def disparar(self,x,y):
        miProyectil = Proyectil.Proyectil(x,y,'recursos/imagenes/tiro.bmp',True)
        self.listaDisparo.append(miProyectil)
        self.sonidoDisparo.play()
   
    def destruccion(self):
        self.Vida = False
        self.velocidad = 0
        self.ImagenPersonaje = self.ImagenExplosion
        self.sonidoDestruccion.play()
        
    def dibujar(self,superficie):
        superficie.blit(self.ImagenPersonaje,self.rect)
        
    def ganar(self):
        for x in self.listaDisparo:
            self.listaDisparo.remove(x)
            
