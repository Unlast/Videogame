import pygame, os
from pygame.locals import *
from Clases import Proyectil
ANCHO = 360
ALTO = 740

class nave(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
        pygame.sprite.Sprite.__init__(self)
        self.ImagenPersonaje = pygame.image.load('imagenes/personaje2.gif')
        self.rect = self.ImagenPersonaje.get_rect()
        self.rect.centerx = ANCHO/2
        self.rect.centery = ALTO-20
        self.listaDisparo = []
        self.Vida = True
        self.Velocidad = 2
        self.ImagenExplosion = pygame.image.load('imagenes/explosion.bmp')
        self.sonidoDisparo = pygame.mixer.Sound('Sonidos/pium.wav')
        self.sonidoDestruccion = pygame.mixer.Sound('Sonidos/explosion2.ogg')
        self.victoria = False
        
    def movimiento(self):
        if self.Vida == True:
            if self.rect.left <=0:
                self.rect.left =0
                
            elif self.rect.right >=360:
                self.rect.right = 360
    
    def disparar(self,x,y):
        miProyectil = Proyectil.Proyectil(x,y,'imagenes/Proyectil.png',True)
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
            
