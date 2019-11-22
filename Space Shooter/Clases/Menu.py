import sys, os, pygame
from Clases import Cursor
from Clases import Opcion
from pygame.locals import *
class Menu:
    #Representa un menú con opciones para un juego
    def __init__(self, opciones):

    
        self.opciones = []
        fuente = pygame.font.Font('recursos/fuentes/monolight.ttf', 20)
        x = 150
        y = 360
        paridad = 1

        self.cursor = Cursor.Cursor(x - 80, y, 30)

        for titulo, funcion in opciones:
            self.opciones.append(Opcion.Opcion(fuente, titulo, x, y, paridad, funcion))
            y += 30
            if paridad == 1:
                paridad = -1
            else:
                paridad = 1

        self.seleccionado = 0
        self.total = len(self.opciones)
        self.mantiene_pulsado = False

    def actualizar(self):
        """Altera el valor de 'self.seleccionado' con los direccionales."""

        k = pygame.key.get_pressed()

        if not self.mantiene_pulsado:
            if k[K_UP]:
                self.seleccionado -= 1
            elif k[K_DOWN]:
                self.seleccionado += 1
            elif k[K_RETURN]:
                # Invoca a la función asociada a la opción.
                self.opciones[self.seleccionado].activar()

        # procura que el cursor esté entre las opciones permitidas
        if self.seleccionado < 0:
            self.seleccionado = 0
        elif self.seleccionado > self.total - 1:
            self.seleccionado = self.total - 1
        
        self.cursor.seleccionar(self.seleccionado)

        # indica si el usuario mantiene pulsada alguna tecla.
        self.mantiene_pulsado = k[K_UP] or k[K_DOWN] or k[K_RETURN]

        self.cursor.actualizar()
     
        for o in self.opciones:
            o.actualizar()

    def imprimir(self, screen):
        """Imprime sobre la pantalla el texto de cada opción del menú."""
    
        self.cursor.imprimir(screen)

        for opcion in self.opciones:
            opcion.imprimir(screen)