#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
# Módulos
import sys, pygame
from pygame.locals import *
 
# Constantes
WIDTH = 640
HEIGHT = 480

# --------------------------------------------------------------------- 
# Clases
# ---------------------------------------------------------------------
class elemento(pygame.sprite.Sprite):
	def __init__(self,imagen,transp,posx,posy,velx,vely):
		pygame.sprite.Sprite.__init__(self)
		self.image = load_image(imagen, transp)
		self.rect = self.image.get_rect()
		self.rect.centerx = posx
		self.rect.centery = posy
		self.speed = [velx, vely]

# ---------------------------------------------------------------------
# Funciones generales
# ---------------------------------------------------------------------
def load_image(filename, transparent=False):
        try: image = pygame.image.load(filename)
        except pygame.error, message:
                raise SystemExit, message
        image = image.convert()
        if transparent:
                color = image.get_at((0,0))
                image.set_colorkey(color, RLEACCEL)
        return image
        
def texto(texto, fuente, posx, posy, color):
	salida = pygame.font.Font.render(fuente, texto, 1, color)
	salida_rect = salida.get_rect()
	salida_rect.centerx = posx
	salida_rect.centery = posy
	return salida, salida_rect

# ---------------------------------------------------------------------
# Funciones del juego
# ---------------------------------------------------------------------
def ProcesarMovimiento(time,keys,palajugador):
	if palajugador.rect.top >= 0:
		if keys[K_UP]:
			palajugador.rect.centery -= palajugador.speed[1] * time
	if palajugador.rect.bottom <= HEIGHT:
		if keys[K_DOWN]:
			palajugador.rect.centery += palajugador.speed[1] * time

def ProcesarIA(time,bola,palaIA):
	if bola.speed[0] >= 0 and bola.rect.centerx >= WIDTH/2:
		if palaIA.rect.centery < bola.rect.centery:
			palaIA.rect.centery += palaIA.speed[1] * time
		if palaIA.rect.centery > bola.rect.centery:
			palaIA.rect.centery -= palaIA.speed[1] * time

def ActualizarPantalla(time,bola,palajugador,palaIA,puntos):
# Actualizamos la bola
	bola.rect.centerx += bola.speed[0] * time
	bola.rect.centery += bola.speed[1] * time
# Control de la puntuación
	if bola.rect.left <= 0:
		puntos[1] += 1
	if bola.rect.right >= WIDTH:
		puntos[0] += 1
	if bola.rect.left <= 0 or bola.rect.right >= WIDTH:
		bola.speed[0] = -bola.speed[0]
		bola.rect.centerx += bola.speed[0] * time
	if bola.rect.top <= 0 or bola.rect.bottom >= HEIGHT:
		bola.speed[1] = -bola.speed[1]
		bola.rect.centery += bola.speed[1] * time

# Miramos las colisiones
	if pygame.sprite.collide_rect(bola, palajugador):
		bola.speed[0] = -bola.speed[0]
		bola.rect.centerx += bola.speed[0] * time
	if pygame.sprite.collide_rect(bola, palaIA):
		bola.speed[0] = -bola.speed[0]
		bola.rect.centerx += bola.speed[0] * time

# ---------------------------------------------------------------------
# Programa Principal
# --------------------------------------------------------------------- 
def main():
# Inicializaciones pygame
	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption("Ejemplo Pygame")
	background_image = load_image('images/fondo_pong.png')
	
# Inicializaciones elementos de juego
	bola = elemento("images/ball.png",True,WIDTH/2,HEIGHT/2,0.5,-0.5)
	palajugador = elemento("images/pala.png",False,30,HEIGHT/2,0,0.5)
	palaIA = elemento("images/pala.png",False,WIDTH-30,HEIGHT/2,0,0.5)
	puntos=[0,0]
	fuentetextopuntos = pygame.font.Font("images/DroidSans.ttf", 25)
	colortextopuntos=(255, 255, 0)

	clock = pygame.time.Clock()

	while True:
		time = clock.tick(60)
		for eventos in pygame.event.get():
			if eventos.type == QUIT:
				sys.exit(0)
# Procesamos jugador
		keys = pygame.key.get_pressed()
		ProcesarMovimiento(time,keys,palajugador)
		
# Procesamos ia
		ProcesarIA(time,bola,palaIA)
		
# Actualizamos estado de la partida
		ActualizarPantalla(time,bola,palajugador,palaIA,puntos)
		p_jug, p_jug_rect = texto(str(puntos[0]), fuentetextopuntos, WIDTH/4, 40,colortextopuntos)
		p_cpu, p_cpu_rect = texto(str(puntos[1]), fuentetextopuntos, WIDTH-WIDTH/4, 40,colortextopuntos)		
		
# Renderizamos
		screen.blit(background_image, (0, 0))
		screen.blit(p_jug, p_jug_rect)
		screen.blit(p_cpu, p_cpu_rect)
		screen.blit(bola.image,bola.rect)
		screen.blit(palajugador.image,palajugador.rect)
		screen.blit(palaIA.image,palaIA.rect)		
		pygame.display.flip()
	return 0
 
if __name__ == '__main__':
	pygame.init()
	main()
