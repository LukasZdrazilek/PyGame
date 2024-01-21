import pygame
import time

class GameTimer:
    def __init__(self):
        self.start_time = None
        self.elapsed_time = 0
        self.font = pygame.font.Font(None, 36)
        self.position = (10, 10)

    def start(self):
        
        self.start_time = time.time()

    def update(self):
        
        if self.start_time is not None:
            current_time = time.time()
            self.elapsed_time = current_time - self.start_time

    def get_time(self):
        
        hours = int(self.elapsed_time // 3600)
        minutes = int((self.elapsed_time % 3600) // 60)
        seconds = int(self.elapsed_time % 60)
        return f'{hours:02}:{minutes:02}:{seconds:02}'

    def draw(self, screen):
        
        timer_text = self.get_time()
        timer_surface = self.font.render(timer_text, True, (255, 255, 255))
        screen.blit(timer_surface, self.position)
        
    def reset(self):
        self.start_time = 0

    def set_time(self, time_str):
        
        hours, minutes, seconds = map(int, time_str.split(':'))
        self.start_time = time.time() - (hours * 3600 + minutes * 60 + seconds)

