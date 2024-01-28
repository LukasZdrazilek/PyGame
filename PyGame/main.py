from ast import Try
import pygame
from pygame.locals import *
import sys

from player import Player
from draw import *
from NPC import NPC
from map import *
from menu import MainMenu
from interface import Interface
from saving import load_game, save_game
from coins import Coins

pygame.init()

# Nastaveni a inicializace obrazovky
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 960
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.DOUBLEBUF)
DISPLAYSURF = pygame.display.set_mode((1280, 960), RESIZABLE)

# Inicializace Main menu
main_menu = MainMenu(screen)
# Inicializace timeru
game_timer = Interface()
# Inicializace hrace
player = Player()
# Inicializace coins
coins = Coins()
# Inicializace NPC
npc = NPC()
# Load hudby
menu_music = pygame.mixer.Sound('Sound/menu.mp3')
menu_music_play = True


############################## Main menu loop #########################################

while True:
    
    menu_option = main_menu.handle_input()
    if menu_music_play:
        menu_music.play()
        menu_music_play = False

    # Pokud existuje save, nacte z nej pozici hrace, casovac a spusti hru
    if menu_option == 'Continue':
       try:
           load_game(player, game_timer, coins, npc)
           menu_music.fadeout(1)
           break
       except FileNotFoundError:
           main_menu.saveError = True
    
    # Spusti hru a vytvori save s pocatecnimi souradnicemi hrace
    elif menu_option == 'New game':
       save_game(player, game_timer, coins, npc)
       game_timer.start()
       menu_music.fadeout(1)
       break
    
    # Vypne hru
    elif menu_option == 'Exit' or menu_option == 'exit':
        menu_music.stop()
        pygame.quit()
        sys.exit()

    # Kresli menu, refreshuje obraz
    main_menu.draw()
    pygame.display.flip()
    

################################### Game loop ########################################

run = True
clock = pygame.time.Clock()

while run:
    
    dt = clock.tick(60) / 1000  # 60 FPS
    key = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if key[pygame.K_ESCAPE]:
            # Pri ukonceni hry ulozi souradnice, coiny, NPC dialogy a cas hrace
            save_game(player, game_timer, coins, npc)
            print("Game saved")
            run = False
            

    # Update casovace
    game_timer.update()    
    # Ovladani hrace
    player.controls(dt, map_objects)
    
    # Check kolizi ktery musi byt z nejakeho duvodu tady  (myslim si, ze jde o naturu Pythonu a toho jak zpracovava kod v case)
    player.canWalk = False
    for obj in map_objects[player.current_screen]:
        if obj.collide_with(player.rect):
            if player.rect.bottom > obj.rect.top:
                player.rect.bottom = obj.rect.top
            player.canWalk = True
            if player.isInJump == True and player.bouncing == False:
                player.jumpingRight = False
                player.jumpingLeft = False
    
    # Kresleni veskerych objektu
    draw(player, npc, screen, game_timer, coins)
    coins.handle_coins(screen, player, npc)

    pygame.display.flip()

pygame.quit()
sys.exit()
