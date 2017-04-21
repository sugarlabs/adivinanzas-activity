import sys
import pygame
import time
from pygame.locals import *

from eztext.eztext import Input
from textrect.textrect import render_textrect
import gtk

resolucion = (800, 600)
reloj = pygame.time.Clock()

ROJO = (255, 0, 0)
NEGRO = (0, 0, 0)
GRIS_CLARO = (216, 216, 216)
GRIS_OSCURO = (48, 48, 48)

class Visual:

    def __init__(self):
        global resolucion
        pygame.init()

        # Dos tipos de letra, grande y chiquito
        self.font = pygame.font.SysFont("dejavusans", 32)
        self.mini_font = pygame.font.SysFont("dejavusans", 24)

        # Si estamos en Sugar la pantalla viene dada
        self.pantalla = pygame.display.get_surface()
        if not self.pantalla:
            # Sino, la creamos
            self.pantalla = pygame.display.set_mode(resolucion)

        resolucion = self.pantalla.get_size()
        self.root = None
        self.ultimo = None

    def preguntar(self, pregunta):
        """Usaremos esta funcion para solicitar un valor al usuario"""
        casillero = Input(font=self.font, color=ROJO, prompt=pregunta)
        
        # donde ubicamos la pregunta?
        rect = self.pantalla.get_rect() # representa la pantalla
        x = rect.centerx - 100
        y = rect.centery + 100
        casillero.set_pos(x, y)

        listo = False
        while not listo:
            # Ceder control a Sugar para la botonera 
            while gtk.events_pending():
                gtk.main_iteration()

            eventos = pygame.event.get()
            for event in eventos:
                if event.type == QUIT:
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        listo = True
                    if event.key == K_ESCAPE:
                        return None

            reloj.tick(30) # limitamos a 30 cuadros por segundo
            
            #actualizamos la pantalla primero el fondo, la pregunta
            self.imprimir()
            casillero.update(eventos)
            casillero.draw(self.pantalla)

            # y pintamos todo
            pygame.display.flip()
                    
        return casillero.value

    def imprimir(self, texto=None, mini=False, fondo=GRIS_OSCURO,
                        color=GRIS_CLARO):
        if not texto:
            texto = self.ultimo

        ancho = resolucion[0] - 100  # resolucion horizontal
        pos_y = self.pantalla.get_rect().centery - 150
        rect = pygame.Rect((50, pos_y, ancho, 300))
        
        if not mini:
            text = render_textrect(texto, self.font, rect, 
                                color, fondo, 1)
        else:
            text = render_textrect(texto, self.mini_font, rect, 
                                color, fondo, 1)

        self.pantalla.blit(text, rect)
        pygame.display.flip()

        # guardamos el ultimo texto por si toca volver a colocarlo
        self.ultimo = texto

    def limpiar(self):
        if self.root:
            self.pantalla.blit(self.root, (0,0))
        else:
            self.pantalla.fill(NEGRO)
        pygame.display.flip()

    def reproducir(self, cancion):
        pygame.mixer.music.load(cancion)
        pygame.mixer.music.play(-1)

    def silencio(self):
        pygame.mixer.music.fadeout(1000)

    def fondo(self, archivo):
        root = pygame.image.load(archivo)
        self.root = pygame.transform.scale(root, resolucion)
        self.root.convert()
        self.pantalla.blit(self.root, (0,0))
        pygame.display.flip()

    def esperar(self, segundos=None):
        if segundos:
            pygame.time.wait(segundos*1000)
        else:
            listo = False
            while not listo:
                # Ceder control a Sugar para la botonera 
                while gtk.events_pending():
                    gtk.main_iteration()

                eventos = pygame.event.get()
                for event in eventos:
                    if event.type == QUIT:
                        sys.exit()
                    if event.type == KEYDOWN:
                        listo = True
 
