import pygame
import time

class Coins:
    def __init__(self):
        
        # Nacitani textur
        self.textures = [
            pygame.image.load('Textures/NPC/dog1.png'),
            pygame.image.load('Textures/NPC/dog2.png'),
            pygame.image.load('Textures/NPC/dog3.png')
        ]
        
        # Pomocne veci
        self.pattern = [0, 1, 2, 1]
        self.pattern_index = 0
        self.image_index = 0
        self.image = self.textures[self.image_index]
        self.last_texture_change = time.time()
        
        self.rect = self.image.get_rect()
        self.rect.x = 675
        self.rect.y = 160
        
        self.can_draw = True
        self.player_coins = 0
        

    def update(self):
        
        if time.time() - self.last_texture_change >= 0.5:
            # Move to the next index in the pattern
            self.pattern_index = (self.pattern_index + 1) % len(self.pattern)
            self.image_index = self.pattern[self.pattern_index]
            self.image = self.textures[self.image_index]
            self.last_texture_change = time.time()
    
    
    def draw(self, screen):
        
        if self.can_draw:
            screen.blit(self.image, self.rect)
    
    
    def pick_up(self, screen, player):
        
        if self.rect.colliderect(player.rect) and self.can_draw:
            self.player_coins += 1
            print(self.player_coins)
            self.can_draw = False
            

    def handle_coins(self, screen, player):
        
        self.draw(screen)
        self.update()
        self.pick_up(screen, player)
            
