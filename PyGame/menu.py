
import pygame
from pygame.locals import *

class MainMenu:
    
    def __init__(self, screen):
        
        self.background = pygame.image.load('Textures/menu_image.png')

        self.screen = screen
        self.font = pygame.font.Font(None, 90)
        self.font2 = pygame.font.Font(None, 36)
        self.options = ['Continue', 'New game', 'Exit']
        self.text = "Game saves data automatically after exiting ( Esc )"
        self.selected_option = 0
        self.saveError = False
        

    def draw(self):
        
        key = pygame.key.get_pressed()
        self.screen.fill((82, 19, 16))
        
        text2 = self.font2.render(self.text, True, (255, 255, 255))
        
        self.screen.blit(self.background, (80, 80))

        self.screen.blit(text2, (650, 920))

        for i, option in enumerate(self.options):
            
            color = (255, 255, 255) if i == self.selected_option else (128, 128, 128)
            text = self.font.render(option, True, color)
            text_sprite = text.get_rect(center = (1280 // 2 + 300, 960 // 2 - 100 + i * 150))
            self.screen.blit(text, text_sprite)
            
        if self.saveError == True:
            self.save_not_found()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    self.saveError = False
            
    
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

    
    def save_not_found(self):
        
        self.screen.fill((82, 19, 16))

        color = (255, 255, 255)
        error = "Saved game not found"
        error_text = self.font.render(error, True, color)
        error_text_sprite = error_text.get_rect(center = (1280 // 2, 960 // 2))
        self.screen.blit(error_text, error_text_sprite)
    