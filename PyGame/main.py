from math import fabs
import pygame, sys
from pygame.locals import *
from player import Player
from draw import *
from NPC import NPC
from map import *

pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 960
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.DOUBLEBUF)
# Nastaveni pro resize a fullscreen
DISPLAYSURF = pygame.display.set_mode((1280, 960), RESIZABLE)

player = Player()
npc = NPC()
run = True
clock = pygame.time.Clock()

# Nacitani obrazku pozadi
background1 = pygame.image.load('Textures/screen1.png')
background2 = pygame.image.load('Textures/screen2.png')


while run:
    
    dt = clock.tick(60) / 1000  # 60 FPS
    key = pygame.key.get_pressed()
    
    #screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if key[pygame.K_ESCAPE]:
            run = False
    
    # Update player controls
    player.controls(dt, map_objects)
    # Check collision for player considering camera offsetb
    player.canWalk = False#####################################################################################
    for obj in map_objects[player.current_screen]:
        if obj.collide_with(player.rect):       # smazat?
            if player.rect.bottom > obj.rect.top:
                player.rect.bottom = obj.rect.top
            player.canWalk = True################################################################################
            if player.isInJump == True and player.bouncing == False:    ###################??????
                player.jumpingRight = False
                player.jumpingLeft = False
                
    #print(player.isInJump)
           
    #print (f'Falling right =   {player.isFallingRight}')
    #print (f'Can walk =  {player.canWalk}')

    # Vykresleni objektu mapy podle aktualni obrazovky hrace        - neni vlastne potreba
    #for obj in map_objects[player.current_screen]:
    #    obj.draw(screen)
        

    draw(player, npc, screen)

    # Kresleni pozadi, NPC a hrace
    #if player.current_screen == 0:
    #    screen.blit(background1, (0, 0))
    #    npc.draw(screen)
    #elif player.current_screen == 1:
    #    screen.blit(background2, (0, 0))
    #player.draw(screen)

    pygame.display.flip()

pygame.quit()
