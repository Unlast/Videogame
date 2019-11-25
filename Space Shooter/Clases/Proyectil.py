import sys, os, pygame

class Proyectil(pygame.sprite.Sprite):
    def __init__(self, posx,posy,ruta,personaje):
        pygame.sprite.Sprite.__init__(self)
        
        self.imagenProyectil = pygame.image.load(ruta)
        self.rect = self.imagenProyectil.get_rect()
        self.velocidadDisparo = 1
        self.rect.top = posy
        self.rect.left = posx
        
        self.disparoPersonaje = personaje
    
    def trayectoria(self):
        if self.disparoPersonaje == True:
            self.rect.top = self.rect.top - self.velocidadDisparo
        else:
            self.rect.top = self.rect.top + self.velocidadDisparo
        
    def dibujar(self, superficie):
        superficie.blit(self.imagenProyectil, self.rect)
