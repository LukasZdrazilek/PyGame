
import pygame
from pygame.locals import *

class MainMenu:
    
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 90)
        self.options = ['Continue', 'New game', 'Exit']
        self.selected_option = 0
        
    
    def draw(self):
        
        self.screen.fill((0, 0, 0))
        
        for i, option in enumerate(self.options):
            
            color = (255, 255, 255) if i == self.selected_option else (128, 128, 128)
            text = self.font.render(option, True, color)
            text_sprite = text.get_rect(center = (1280 // 2 + 300, 960 // 2 - 100 + i * 150))
            self.screen.blit(text, text_sprite)
            
    
    def handle_input(self):
        
        key = pygame.key.get_pressed()
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                return 'exit'
            
            if key[pygame.K_UP] or key[pygame.K_w]:
                self.selected_option = (self.selected_option - 1) % len(self.options)
                
            if key[pygame.K_DOWN] or key[pygame.K_s]:
                self.selected_option = (self.selected_option + 1) % len(self.options)
                
            if key[pygame.K_RETURN]:
                return self.options[self.selected_option]
            
        return None
