import pygame
from Clases import Proyectil
from random import randint
from Clases import NaveEspacial
juego = True
ANCHO = 360
ALTO = 740
LISTA_ENEMIGOS=[]

class nave_enemiga(object):
    """
    nave_enemiga clase madre, jefe_enemigo hereda de la madre.
    
    Posiciones sobre el ejex y el ejey
    
    Imagenes que luego se pondrán en la lista, una posición para recorrer la lista
    
    Un atributo que representa a la lista con la posición inicial
    
    Lista tiro para guardar los proyectiles, velocidad tiro el desplazamiento en pantalla
    velocidad controlar el movimiento
    
    Colision detecta la cantidad de impactos, útil para hacer más dificil de destruir
    
    Cambio de imagen = 1 para que las imagenes cambien a medidad que transcurre el tiempo
    
    Contador para verificar cuantas veces toca los limites horizontales, booleano 
    para limitar la cantidad de veces, maxDescenso es lo que tiene que descender
    cada vez que el booleano sea falso
    Max_lateral para controlar la cantidad de veces que toca los limites horizontales
    
    Limites para que no salga de pantalla.
    
    Rango disparo para manejar cada cuanto se realiza un disparo (Explicado mejor en el metodo)
    
    Conquista para verificar si el personaje fue destruido
    
    Un sonido para los disparos
    """
    def __init__(self,posx,posy, distancia, imagenUno, imagenDos, lateral):
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
        self.velocidadTiro = 2
        self.velocidad = 1
        self.rect.top = posy
        self.rect.left = posx
        self.colision = 0
        self.cambioImagen = 1
    	
        self.derecha = True
        self.contador = 0
        self.maxDescenso = self.rect.top+40
        self.maximo_lateral = lateral
        
        self.limiteDer= posx + distancia
        self.limiteIzq= posx - distancia
    	
        self.rangoDisparo = 1
        self.conquista = False 
        
        self.sonidoDisparo = pygame.mixer.Sound('recursos/audio/disparo1.ogg')
        
    def mostrar(self, superficie):
        """
        Mostrar: dibuja al/los enemigo/s sobre la pantalla
        """
        self.imagenEnemigo = self.listaImagenes[self.posicionImagen]
        superficie.blit(self.imagenEnemigo, self.rect)
        
    def animacion(self,tiempo):
        """
        Animacion: si el jugador no fue destruido se llaman a los metodos de mover y atacar
        ademas se cambia la imagen del enemigo
        """
        if self.conquista == False:
            self.movimientos()

            self.ataque()
    
            if  self.posicionImagen>=len(self.listaImagenes)-1:
                self.posicionImagen = 0
            else:
                self.posicionImagen +=1
    
    def movimientos(self):
        """
        Movimientos: Si se puede mover de costado, continuará haciendolo de lo contrario
        se invoca al método descender
        """

        if self.contador <self.maximo_lateral:
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
        """
        Movimiento lateral = Si derecha es verdadero se mueve en esa direccion, de lo contrario
        suma uno al contador y se mueve en direccion contraria
        """
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
        """
        Ataque: A través de un numero aleatorio se invoca a la funcion disparo, mientras más bajo sea
        el numero máximo del randint más disparos se realizaran
        """
        if (randint(0,200)<self.rangoDisparo):
            self.disparo()

    def disparo(self):
        x,y = self.rect.center
        miProyectil = Proyectil.Proyectil(x,y,'recursos/imagenes/tiro2.bmp',False)
        self.listaTiro.append(miProyectil)
        self.sonidoDisparo.play()
 
    def colision(lista, tiempo, superficie, jugador, altura, ancho, texto):
        """
        Colision: Controla los impactos entre el jugador y el enemigo
        """
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
            """
            DetenerEnemigo: Si el jugador es impactado por un proyectil los enemigos se dejan de mover
            y se eliminan los disparos.
            """
            for armada in lista:
                for disparo in armada.listaTiro:
                    armada.listaTiro.remove(disparo)
                armada.conquista = True 
                
class jefe_enemigo(nave_enemiga):
    def __init__(self,posx,posy, distancia, imagenUno, imagenDos,lateral):
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
        self.maximo_lateral = lateral

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
        
    
            
    
    