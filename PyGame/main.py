from ast import Try
import pygame
from pygame.locals import *
import sys
from player import Player
from draw import *
from NPC import NPC
from map import *
from menu import MainMenu
from interface import GameTimer
from saving import load_game, save_game

pygame.init()

# Nastaveni a inicializace obrazovky
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 960
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.DOUBLEBUF)
# Nastaveni pro resize a fullscreen
DISPLAYSURF = pygame.display.set_mode((1280, 960), RESIZABLE)
# Inicializace Main menu
main_menu = MainMenu(screen)
# Inicializace timeru
game_timer = GameTimer()

player = Player()

# Main menu loop
while True:
    
    menu_option = main_menu.handle_input()

    # Pokud existuje save, nacte z nej pozici hrace, casovac a spusti hru
    if menu_option == 'Continue':
       try:
           load_game(player, game_timer)
           break
       except FileNotFoundError:
           print("Saved game not found")
    
    # Spusti hru a vytvori save s pocatecnimi souradnicemi hrace
    elif menu_option == 'New game':
       save_game(player, game_timer)
       game_timer.start()
       break
    
    # Vypne hru
    elif menu_option == 'Exit' or menu_option == 'exit':
        pygame.quit()
        sys.exit()

    main_menu.draw()
    pygame.display.flip()
    

################################### Game loop ########################################

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
            # Pri ukonceni hry ulozi souradnice a cas hrace
            save_game(player, game_timer)
            print("Game saved")
            run = False
            

    # Update casovace
    game_timer.update()    
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
    game_timer.draw(screen)

    #print(player.xFallingSpeed)

    # Kresleni pozadi, NPC a hrace
    #if player.current_screen == 0:
    #    screen.blit(background1, (0, 0))
    #    npc.draw(screen)
    #elif player.current_screen == 1:
    #    screen.blit(background2, (0, 0))
    #player.draw(screen)

    pygame.display.flip()

pygame.quit()
sys.exit()
