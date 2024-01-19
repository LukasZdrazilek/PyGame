import pygame

screen_backgrounds = []

# Nacitani obrazku pozadi
background1 = pygame.image.load('Textures/screen1.png')
background2 = pygame.image.load('Textures/screen2.png')
background3 = pygame.image.load('Textures/screen3.png')

# Push textur do listu
screen_backgrounds.append(background1)
screen_backgrounds.append(background2)
screen_backgrounds.append(background3)

# Kresleni pozadi, NPC a hrace
def draw(player, npc, screen):
    
    screen.blit(screen_backgrounds[player.current_screen], (0, 0))

    if player.current_screen == 0:
        npc.draw(screen)
        
    player.draw(screen)
