import pygame
import time

class Coins:
    def __init__(self):
        
        # Nacitani textur
        self.textures = [
            pygame.image.load('Textures/Coin/coin1.png'),
            pygame.image.load('Textures/Coin/coin2.png'),
            pygame.image.load('Textures/Coin/coin3.png')
        ]

        # Pomocne veci
        self.pattern = [0, 1, 2, 1]
        self.pattern_index = 0
        self.image_index = 0
        self.image = self.textures[self.image_index]
        self.last_texture_change = time.time()

        self.rect = self.image.get_rect()
        self.player_coins = 0
        
        # Souradnice X a Y coin
        self.coinsX = [625, 110, 110]
        self.coinsY = [120, 140, 140]

        # Checky na sebrani coiny
        self.can_draw = [True, True, True]


    


    def handle_coins(self, screen, player):
        
        # Prochazeni coinu podle listu can_draw
        for i in range(len(self.can_draw)):
            if self.can_draw[player.current_screen]:
                
                # Animace textury coiny dle casu
                if time.time() - self.last_texture_change >= 0.5:
                    
                    self.pattern_index = (self.pattern_index + 1) % len(self.pattern)
                    self.image_index = self.pattern[self.pattern_index]
                    self.image = self.textures[self.image_index]
                    self.last_texture_change = time.time()

                # Vykresleni coin podle pozice hrace
                self.rect.x = self.coinsX[player.current_screen]
                self.rect.y = self.coinsY[player.current_screen]

                screen.blit(self.image, self.rect)

                # Sebrani coiny
                if self.rect.colliderect(player.rect) and self.can_draw[i]:
                    
                    self.player_coins += 1
                    self.can_draw[i] = False
                    
        
