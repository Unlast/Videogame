import pygame, os, time
from pygame.locals import *
from Clases import Alien as Enemigo
from Clases import Proyectil
from Clases import Niveles
ANCHO = 360
ALTO = 740
BLANCO = (255,255,255)

class nave(pygame.sprite.Sprite):
    
    def __init__(self):
        
        pygame.sprite.Sprite.__init__(self)
        self.ImagenPersonaje = pygame.image.load('recursos/imagenes/001.gif')
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
        self.nivel = False
        self.nivel2 = False
        self.nivel3 = False
        self.puntuacion = 0
 
    def movimiento(self):
        if self.Vida == True:
            if self.rect.left <=0:
                self.rect.left =0    
            elif self.rect.right >=360:
                self.rect.right = 360
    
    def disparar(self,x,y):
        if self.Vida == True:
            miProyectil = Proyectil.Proyectil(x,y,'recursos/imagenes/tiro.bmp',True)
            self.listaDisparo.append(miProyectil)
            self.sonidoDisparo.play()
    
    
    def destruccion(self):
        self.Vida = False
        self.velocidad = 0
        self.ImagenPersonaje = self.ImagenExplosion
        self.sonidoDestruccion.play()
        self.remove()
    def dibujar(self,superficie):
        superficie.blit(self.ImagenPersonaje,self.rect)
        
    def ganar(self):
        for x in self.listaDisparo:
                x.rect.top = -10
                
    def colision(self,lista,superficie,armada,fin):
        if len(self.listaDisparo)>0:
            for x in self.listaDisparo:
                x.dibujar(superficie)
                x.trayectoria()
                if x.rect.top<-10:
                    self.listaDisparo.remove(x)
                    self.puntuacion -= 5
                else:
                    for armada in lista:
                        if x.rect.colliderect(armada.rect):
                            armada.colision+=1
                            self.puntuacion+=10
                            x.rect.top = -10
                            if armada.colision > fin:
                                lista.remove(armada)
                                self.puntuacion +=50
    
            
    def pasar_nivel(self,lista,ventana):
            self.nivel = True
            Niveles.pantalla_carga(ventana, ANCHO, ALTO)
            self.ganar()
            Niveles.cargarBossPiramide(lista,3)
            
    def pasar_nivel2(self, lista, ventana):
        self.nivel = True
        Niveles.pantalla_carga(ventana, ANCHO, ALTO)
        self.ganar()
        Niveles.cargarBossPiramideI(lista)
        
    def destruccion_total(self,lista):
       for x in lista:
           lista.remove(x)
    
    def mostrar_puntos(self,ventana):
        pygame.init()
        fuente = pygame.font.Font("recursos/fuentes//SharpCardinal.ttf", 30)
        texto = fuente.render(str(self.puntuacion).zfill(5), True, BLANCO)
        ventana.blit(texto, (0,0))