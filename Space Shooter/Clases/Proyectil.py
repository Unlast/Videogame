import pygame

class Proyectil(pygame.sprite.Sprite):
    """
    Clase que contiene los disparos que ejecutarán tanto el jugador
    como las naves enemigas. Está compuesto por una imagen, que se
    convierte a rectangulo, la velocidad por pixel a la que se desplazará,
    las posiciones sobre el eje X y el Y. Así también como quien será el que dispara.
    """
    def __init__(self, posx,posy,ruta,personaje):
        pygame.sprite.Sprite.__init__(self)
        
        self.imagenProyectil = pygame.image.load(ruta)
        self.rect = self.imagenProyectil.get_rect()
        self.velocidadDisparo = 2
        self.rect.top = posy
        self.rect.left = posx
        
        self.disparoPersonaje = personaje
    
    def trayectoria(self):
        """
        Trayectoría:si es True el disparo lo realizará
        el jugador e irá en dirección hacia arriba. Si es False el disparo lo realizará
        la nave enemiga e irá en dirección opuesta, es decir hacia abajo.
        """
        if self.disparoPersonaje == True:
            self.rect.top = self.rect.top - self.velocidadDisparo
        else:
            self.rect.top = self.rect.top + self.velocidadDisparo
        
    def dibujar(self, superficie):
        """
        El método dibujar, plasma sobre la pantalla el dibujo del proyectil que corresponda
        """
        superficie.blit(self.imagenProyectil, self.rect)
