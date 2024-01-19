import pygame

class NPC:
    def __init__ (self):
        
        # Nacitani textur NPC
        self.default_image = pygame.image.load('Textures/NPC/npc_prozatim.png')

        self.image = self.default_image
        self.rect = self.image.get_rect()
        
        # Nastaveni pozice NPC
        self.rect.x = 980
        self.rect.y = 720
        

    # Kresli texturu NPC na obrazovku
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
