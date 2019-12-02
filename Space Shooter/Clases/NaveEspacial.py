import pygame
from Clases import Proyectil
from Clases import Niveles
ANCHO = 360
ALTO = 740
BLANCO = (255,255,255)


class nave(pygame.sprite.Sprite):
    """
    Clase que contiene al personaje.
    Que contiene una imagen que se le aplica un get rect para calcular su diemension
    3er y 4to atributo son su ubicacion dentro de la pantalla
    Una lista disparo donde se guardará cada elemento cuando se dispare
    Un booleano llamado Vida que indica si fue alcanzado por un disparo enemigo
    comienza en verdadero porque aún no ha sido impactado.
    El desplazamiento en la pantalla
    Una imagen para cuando es alcanzado por un proyectil
    Un sonido para cada vez que se dispara
    Y otro para cuando es alcanzado por un proyectil
    Una atributo para detectar si eliminó a todos los enemigos
    Otro que indica la dirección hacia donde dispara
    2 para controlar en que nivel se encuentra
    y la puntuación inicializada en 0
    """
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

        self.puntuacion = 0

 
    def movimiento(self):
            """
            Movimiento: indica hacia donde se puede mover dentro del eje x
            ya que la nave sólo se mueve de costado.
            """
            if self.rect.left <=0:
                self.rect.left =0    
            elif self.rect.right >=360:
                self.rect.right = 360
            
    
    def disparar(self,x,y):
        """
        Disparar: solo se ejecutará si la nave no fue destruida (Vida = True)
        se instancia un proyectil y se  le asigna una imagen
        se agrega a la lista cada vez que se ejecuta 
        y se reproduce el sonido correspondiente
        con el lugar donde saldrán los disparos
        """
        if self.Vida == True:
            miProyectil = Proyectil.Proyectil(x,y,'recursos/imagenes/tiro.bmp',True)
            self.listaDisparo.append(miProyectil)
            self.sonidoDisparo.play()
    
    
    def destruccion(self):
        """
        Si es impactado por un proyectil enemigo se cambia el booleano Vida
        se mueestra la imagen y se reproduce el sonido de explosion
        """
        self.Vida = False
        self.ImagenPersonaje = self.ImagenExplosion
        self.sonidoDestruccion.play()
    
    def dibujar(self,superficie):
        """
        Dibujar: se ingresa el parámetro de la imagen en la que a través
        del método blit se superpondrá la imagen del personaje.
        """
        superficie.blit(self.ImagenPersonaje,self.rect)
        
    def ganar(self):
        """
        Ganar: Si todas las naves enemigas son eliminadas se destruirán los disparos
        """
        for x in self.listaDisparo:
                x.rect.top = -10
                
    def colision(self,lista,superficie,armada,fin):
        """
        Colision: Si el disparo de la nave colisiona con uno de los enemigos, los 2 desaparecen
        no se restan puntos. Si impacta con un enemigo se suman 10, si lo destruye 50, en este caso
        se elimina el disparo y el enemigo. En todos los casos se dibuja la trayectoria del proyectil.
        Si el proyectil no impacta con nada, desaparece de la pantalla, se elimina y se restan 10 puntos.
        """
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
            """
            PasarNivel: Ambos comprueban que la condicion sea correcta y cargan el nuevo escenario
            """
            self.nivel = True
            Niveles.pantalla_carga(ventana, ANCHO, ALTO)
            self.ganar()
            Niveles.cargarBossPiramide(lista,3)
            
    def pasar_nivel2(self, lista, ventana):
        self.nivel = True
        Niveles.pantalla_carga(ventana, ANCHO, ALTO)
        self.ganar()
        Niveles.cargarBossLineal(lista,1)
        Niveles.cargarEnemigosLineal(lista,1)
    
        
        
    def destruccion_total(self,lista):
        """
        DestruccionTotal: Para pulsar un boton y en base a la lista que entra por parámetro,
        se vayan destruyendo los enemigos.
        """
        for x in lista:
           lista.remove(x)
    
    def mostrar_puntos(self,ventana):
        """
        MostrarPuntos: muestra la puntuación, en la parte superior izquierda de la pantalla
        """
        pygame.init()
        fuente = pygame.font.Font("recursos/fuentes//SharpCardinal.ttf", 30)
        texto = fuente.render(str(self.puntuacion).zfill(5), True, BLANCO)
        ventana.blit(texto, (0,0))
    

