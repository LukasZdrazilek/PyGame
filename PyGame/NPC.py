import pygame
import time

class NPC:
    def __init__(self):
        
        # Nacitani textur
        self.textures = [
            pygame.image.load('Textures/NPC/dog1.png'),
            pygame.image.load('Textures/NPC/dog2.png'),
            pygame.image.load('Textures/NPC/dog3.png')
        ]
        
        self.sound1 = pygame.mixer.Sound('Sound/dog1.mp3')
        
        # Pomocne veci
        self.start_timer = True  
        self.start_time = 0
        
        self.pattern = [0, 1, 2, 1]
        self.pattern_index = 0
        self.image_index = 0
        self.image = self.textures[self.image_index]
        self.last_texture_change = time.time()
        
        self.rect = self.image.get_rect()
        self.rect.x = 950
        self.rect.y = 620
        
        self.play_sound1 = True
        self.play_sound2 = True
        self.play_sound3 = True
        self.play_sound4 = True
        self.play_sound5 = True
        

    def update(self):
        
        if time.time() - self.last_texture_change >= 0.5:
            # Move to the next index in the pattern
            self.pattern_index = (self.pattern_index + 1) % len(self.pattern)
            self.image_index = self.pattern[self.pattern_index]
            self.image = self.textures[self.image_index]
            self.last_texture_change = time.time()


    def draw(self, screen):
        
        screen.blit(self.image, self.rect)
        
       
    def speak(self, screen):
        
        aktualni_cas = pygame.time.get_ticks()
        font = pygame.font.Font(None, 26)
        text = ""
        
        # Pocatecni cas bez loopovani
        if self.start_timer:
            self.start_time = pygame.time.get_ticks()
            self.start_timer = False
            
            
        if aktualni_cas >= self.start_time + 5000:
            text = "Hello wanderer, I am Dog of Wisdom"
            if self.play_sound1:
                self.sound1.play(0)
                self.play_sound1 = False
        
        text_surface = font.render(text, True, (255, 255, 255))
        
        
        screen.blit(text_surface, (830, 580))



    # Napady na NPC text

    # Back here? ...maybe you should loose some weight
    # 
