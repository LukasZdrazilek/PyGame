import pygame
import time

# Class na interface a hlavne game timer
class Interface:
    
    def __init__(self):
        
        # Nacitani hudby ve hre (nenapadlo me uplne kam to dat)
        self.music = pygame.mixer.Sound('Sound/rainforest.mp3')

        # Vlastnosti timeru
        self.start_time = None
        self.elapsed_time = 0
        self.font = pygame.font.Font(None, 36)
        self.position = (10, 10)
        self.play_music = True


    # Start timeru
    def start(self):
        
        self.start_time = time.time()


    # Update timeru
    def update(self):
        
        if self.start_time is not None:
            current_time = time.time()
            self.elapsed_time = current_time - self.start_time


    # Get time formatovany na vypis a ukladani
    def get_time(self):
        
        hours = int(self.elapsed_time // 3600)
        minutes = int((self.elapsed_time % 3600) // 60)
        seconds = int(self.elapsed_time % 60)
        return f'{hours:02}:{minutes:02}:{seconds:02}'
    

    # Kresleni casovace, coins a max coins
    def draw(self, screen, coins):
        
        if self.play_music:
            self.music.play(10)
            self.play_music = False

        # Kresleni textu casovace
        timer_text = self.get_time()
        timer_surface = self.font.render(timer_text, True, (255, 255, 255))
        screen.blit(timer_surface, self.position)
        
        # Kresleni textu poctu coins hrace
        coins_text = str(coins.player_coins)
        coins_surface = self.font.render(coins_text, True, (255, 255, 255))
        screen.blit(coins_surface, (5 ,935))
        
        # Kresleni textu max poctu coins
        max_coins_text = " / "+str(len(coins.can_draw))+" coins"
        max_coins_surface = self.font.render(max_coins_text, True, (255, 255, 255))
        screen.blit(max_coins_surface, (20, 935))
        

    # Reset casovace
    def reset(self):
        self.start_time = 0


    # Set casovace po nacteni hry
    def set_time(self, time_str):
        
        hours, minutes, seconds = map(int, time_str.split(':'))
        self.start_time = time.time() - (hours * 3600 + minutes * 60 + seconds)

