import pygame,os
from pygame.locals import *
from Clases import Proyectil
from random import randint
from Clases import NaveEspacial
juego = True
ANCHO = 360
ALTO = 740
LISTA_ENEMIGOS=[]
class nave_enemiga(object):
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
        self.colision = 0
        self.cambioImagen = 1
    	
        self.derecha = True
        self.contador = 0
        self.maxDescenso = self.rect.top+40
        
        self.limiteDer= posx + distancia
        self.limiteIzq= posx - distancia
    	
        self.rangoDisparo = 1
        self.conquista = False 

        self.sonidoDisparo = pygame.mixer.Sound('recursos/audio/disparo1.ogg')
        
    def mostrar(self, superficie):
        self.imagenEnemigo = self.listaImagenes[self.posicionImagen]
        superficie.blit(self.imagenEnemigo, self.rect)
        
    def animacion(self,tiempo):
        
        if self.conquista == False:
            self.movimientos()

            self.ataque()
    
            if  self.posicionImagen>=len(self.listaImagenes)-1:
                self.posicionImagen = 0
            else:
                self.posicionImagen +=1
    
    def movimientos(self):
        if self.contador <3:
            self.movimientoLateral()
        else:
            self.descenso()
    
    def descenso(self):
        if self.maxDescenso == self.rect.top:
            self.contador =0
            self.maxDescenso = self.rect.top + 40
        else:
            self.rect.top +=20
   
    def movimientoLateral(self):
        if self.derecha == True:
            self.rect.left = self.rect.left+ self.velocidad
            if self.rect.left > self.limiteDer:
                self.derecha = False
                self.contador +=1
        else:
            self.rect.left = self.rect.left - self.velocidad
            if self.rect.left <self.limiteIzq:
                self.derecha = True
                
    def ataque(self):
        if (randint(0,600)<self.rangoDisparo):
            self.disparo()

    def disparo(self):
        x,y = self.rect.center
        miProyectil = Proyectil.Proyectil(x,y,'recursos/imagenes/tiro2.bmp',False)
        self.listaTiro.append(miProyectil)
        self.sonidoDisparo.play()
 
    def colision(lista, tiempo, superficie, jugador, altura, ancho, texto):
        for armada in lista:
            armada.animacion(tiempo)
            armada.mostrar(superficie)
            if armada.rect.colliderect(jugador.rect):
                jugador.destruccion()
                lista.remove(armada)
                armada.detenerEnemigo(lista)
            if armada.rect.top > altura-20:
                jugador.destruccion()
                jugador.Vida = False
                armada.detenerEnemigo(lista)    
            
            if len(armada.listaTiro)>0:
                    for x in armada.listaTiro:
                        x.dibujar(superficie)
                        x.trayectoria()
                        if x.rect.colliderect(jugador.rect):
                            jugador.destruccion()
                            armada.detenerEnemigo(lista)
                            for disparo in jugador.listaDisparo:
                                jugador.listaDisparo.remove(disparo)
                        if x.rect.top>900:
                            armada.listaTiro.remove(x)
                        else:
                            for disparo in jugador.listaDisparo:
                                if x.rect.colliderect(disparo.rect):
                                    jugador.listaDisparo.remove(disparo)
                                    armada.listaTiro.remove(x)
    
    def detenerEnemigo(self,lista):
            for armada in lista:
                for disparo in armada.listaTiro:
                    armada.listaTiro.remove(disparo)
                armada.conquista = True 
                
class jefe_enemigo(nave_enemiga):
    def __init__(self,posx,posy, distancia, imagenUno, imagenDos):
        super(nave_enemiga, self)
        
        self.imagenA = pygame.image.load(imagenUno)
        self.imagenB = pygame.image.load(imagenDos)
        self.listaImagenes = [self.imagenA, self.imagenB]
        self.distancia = distancia
        self.posicionImagen = 0
        self.imagenEnemigo = self.listaImagenes[self.posicionImagen]
        self.colision = 0
        self.vivo = True
        self.rect = self.imagenEnemigo.get_rect()
        self.sonidoDisparo = pygame.mixer.Sound('recursos/audio/pium.wav')
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
        nave_enemiga.mostrar(self,superficie)
    
    def animacion(self, tiempo):
        nave_enemiga.animacion(self,tiempo)
    
    def movimientos(self):
        nave_enemiga.movimientos(self)
       
    def descenso(self):
        nave_enemiga.descenso(self)
    
    def movimientoLateral(self):
        nave_enemiga.movimientoLateral(self)
    
    def ataque(self):
        nave_enemiga.ataque(self)
    
    def disparo(self):
        x,y = self.rect.center
        miProyectil = Proyectil.Proyectil(x,y,'recursos/imagenes/Proyectil.png',False)
        self.listaTiro.append(miProyectil)
        self.sonidoDisparo.play()
        
    
            
    
    