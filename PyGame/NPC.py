import pygame
import time

class NPC:
    def __init__(self):
        
        # Nacitani textur NPC
        self.textures = [
            pygame.image.load('Textures/NPC/dog1.png'),
            pygame.image.load('Textures/NPC/dog2.png'),
            pygame.image.load('Textures/NPC/dog3.png')
        ]
        
        # Nacitani zvuku NPC
        self.sound1 = pygame.mixer.Sound('Sound/dog1.mp3')
        self.sound2 = pygame.mixer.Sound('Sound/dog2.mp3')
        self.sound3 = pygame.mixer.Sound('Sound/dog3.mp3')
        self.sound_excited = pygame.mixer.Sound('Sound/dogExcited.mp3')
        self.sound_lessExcited = pygame.mixer.Sound('Sound/dogLessExcited.mp3')
        self.sound_dogFetch = pygame.mixer.Sound('Sound/dogGoAndFetchSome.mp3')
        self.sound_wisdom11 = pygame.mixer.Sound('Sound/dogWisdom11.mp3')
        self.sound_wisdom12 = pygame.mixer.Sound('Sound/dogWisdom12.mp3')
        self.sound_wisdom21 = pygame.mixer.Sound('Sound/dogWisdom21.mp3')
        self.sound_wisdom22 = pygame.mixer.Sound('Sound/dogWisdom22.mp3')
        self.sound_wisdom31 = pygame.mixer.Sound('Sound/dogWisdom31.mp3')
        self.sound_wisdom32 = pygame.mixer.Sound('Sound/dogWisdom32.mp3')
        
        # Pomocne veci
        self.start_timer = True  
        self.start_time = 0
        self.start_wisdom_timer1 = False
        self.start_wisdom_timer2 = False
        self.start_wisdom_timer3 = False
        
        self.wisdom_start_timer = True
        self.wisdom_time = 0
        self.aktualni_wisdom_cas = 0
        
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
        self.play_sound_excited = True
        self.play_sound_lessExcited = True
        self.play_sound_excited2 = True
        self.play_sound_lessExcited2 = True
        self.play_sound_excited3 = True
        self.play_sound_lessExcited3 = True
        self.play_sound_dogFetch = True
        self.play_sound_wisdom11 = True
        self.play_sound_wisdom12 = True
        self.play_sound_wisdom21 = True
        self.play_sound_wisdom22 = True
        self.play_sound_wisdom31 = True
        self.play_sound_wisdom32 = True
        
        self.told_wisdom = 0
        self.telling_wisdom = False
        self.tells_wisdom = True
        self.speaking = False
        self.text = ""
        

    # Logika ke zmene textury coiny podle paternu 0, 1, 2, 1, 0, 1,... v case
    def update(self):
        
        if time.time() - self.last_texture_change >= 0.5:
 
            self.pattern_index = (self.pattern_index + 1) % len(self.pattern)
            self.image_index = self.pattern[self.pattern_index]
            self.image = self.textures[self.image_index]
            self.last_texture_change = time.time()

    # Kresleni NPC
    def draw(self, screen):
        
        screen.blit(self.image, self.rect)
        

    # Funkce na rikani wisdoms po obdrzeni hracove coiny
    def tell_wisdom(self, player):
        
        if self.start_wisdom_timer1:
            
            self.aktualni_wisdom_cas = pygame.time.get_ticks()
            # Pocatecni cas bez loopovani
            if self.wisdom_start_timer:
                self.wisdom_time = pygame.time.get_ticks()
                self.wisdom_start_timer = False
        
        if self.start_wisdom_timer2:
            
            self.aktualni_wisdom_cas = pygame.time.get_ticks()
            # Pocatecni cas bez loopovani
            if self.wisdom_start_timer:
                self.wisdom_time = pygame.time.get_ticks()
                self.wisdom_start_timer = False
                
        if self.start_wisdom_timer3:
            
            self.aktualni_wisdom_cas = pygame.time.get_ticks()
            # Pocatecni cas bez loopovani
            if self.wisdom_start_timer:
                self.wisdom_time = pygame.time.get_ticks()
                self.wisdom_start_timer = False
        

        # WISDOM TEXTY  (there has to be a better way to do this...)
        # Monolog k wisdom 1 v case
        if self.told_wisdom == 1 and self.start_wisdom_timer1:
            self.text = "                   Ooh, how shiny! Now listen:"
            if self.play_sound_excited:
                self.sound_excited.play(0)
                self.play_sound_excited = False
        if self.told_wisdom == 1 and self.aktualni_wisdom_cas >= self.wisdom_time + 3000 and self.start_wisdom_timer1:
            self.text = "           If your ball is too big for your mouth,"
            if self.play_sound_wisdom11:
                self.sound_wisdom11.play(0)
                self.play_sound_wisdom11 = False
        if self.told_wisdom == 1 and self.aktualni_wisdom_cas >= self.wisdom_time + 6000 and self.start_wisdom_timer1:
            self.text = "                               It's not yours!"
            if self.play_sound_wisdom12:
                self.sound_wisdom12.play(0)
                self.play_sound_wisdom12 = False
        if self.told_wisdom == 1 and self.aktualni_wisdom_cas >= self.wisdom_time + 9000 and self.start_wisdom_timer1:
            self.text = "                    Aaaah, what a great wisdom!"
            if self.play_sound_lessExcited:
                self.sound_lessExcited.play(0)
                self.play_sound_lessExcited = False
        if self.told_wisdom == 1 and self.aktualni_wisdom_cas >= self.wisdom_time + 12000:
            self.start_wisdom_timer1 = False
            self.wisdom_start_timer = True
            self.telling_wisdom = False
            self.tells_wisdom = True
                

        # Monolog k wisdom 2 v case
        if self.told_wisdom == 2 and self.start_wisdom_timer2:
            self.text = "                   Ooh, this one's a beauty:"
            if self.play_sound_excited2:
                self.sound_excited.play(0)
                self.play_sound_excited2 = False
        if self.told_wisdom == 2 and self.aktualni_wisdom_cas >= self.wisdom_time + 3000 and self.start_wisdom_timer2:
            self.text = "  You cannot fetch happy, you cannot call happy,"
            if self.play_sound_wisdom21:
                self.sound_wisdom21.play(0)
                self.play_sound_wisdom21 = False
        if self.told_wisdom == 2 and self.aktualni_wisdom_cas >= self.wisdom_time + 6000 and self.start_wisdom_timer2:
            self.text = "        happy happens, happy has to happen."
            if self.play_sound_wisdom22:
                self.sound_wisdom22.play(0)
                self.play_sound_wisdom22 = False
        if self.told_wisdom == 2 and self.aktualni_wisdom_cas >= self.wisdom_time + 9000 and self.start_wisdom_timer2:
            self.text = "                  Aaaah, that's a good wisdom!"
            if self.play_sound_lessExcited2:
                self.sound_lessExcited.play(0)
                self.play_sound_lessExcited2 = False
        if self.told_wisdom == 2 and self.aktualni_wisdom_cas >= self.wisdom_time + 12000:
            self.start_wisdom_timer2 = False     
            self.wisdom_start_timer = True
            self.telling_wisdom = False
            self.tells_wisdom = True

            
        # Monolog k wisdom 3 v case
        if self.told_wisdom == 3 and self.start_wisdom_timer3:
            self.text = "                        Behold! A wisdom:"
            if self.play_sound_excited3:
                self.sound_excited.play(0)
                self.play_sound_excited3 = False
        if self.told_wisdom == 3 and self.aktualni_wisdom_cas >= self.wisdom_time + 3000 and self.start_wisdom_timer3:
            self.text = "       Life is not about how far can you jump,"
            if self.play_sound_wisdom31:
                self.sound_wisdom31.play(0)
                self.play_sound_wisdom31 = False
        if self.told_wisdom == 3 and self.aktualni_wisdom_cas >= self.wisdom_time + 6000 and self.start_wisdom_timer3:
            self.text = " it's about how many wisdoms can you gather."
            if self.play_sound_wisdom32:
                self.sound_wisdom32.play(0)
                self.play_sound_wisdom32 = False
        if self.told_wisdom == 3 and self.aktualni_wisdom_cas >= self.wisdom_time + 9000 and self.start_wisdom_timer3:
            self.text = "             Aaaah, now that's a real wisdom!"
            if self.play_sound_lessExcited3:
                self.sound_lessExcited.play(0)
                self.play_sound_lessExcited3 = False
        if self.told_wisdom == 3 and self.aktualni_wisdom_cas >= self.wisdom_time + 12000:
            self.start_wisdom_timer3 = False   


    # Funkce na pocatecni monolog + tell_wisdom a kresleni textu dohromady
    def speak(self, screen, player):
        
        aktualni_cas = pygame.time.get_ticks()
        font = pygame.font.Font(None, 26)
        self.text = ""
        
        # Pocatecni cas bez loopovani
        if self.start_timer:
            self.start_time = pygame.time.get_ticks()
            self.speaking = True
            self.start_timer = False
              
        if aktualni_cas >= self.start_time + 4000 and aktualni_cas <= self.start_time + 7000:
            self.text = "               Hello wanderer, I am Dog of Wisdom"
            if self.play_sound1:
                self.sound1.play(0)
                self.play_sound1 = False
        
        if aktualni_cas >= self.start_time + 7000 and aktualni_cas <= self.start_time + 10000:
            self.text = "    I dispense wisdom from my mighty wisdom tooth"
            if self.play_sound2:
                self.sound2.play(0)
                self.play_sound2 = False
        
        if aktualni_cas >= self.start_time + 10000 and aktualni_cas <= self.start_time + 13000:
            self.text = "                    Bring me shiny gold coins"
            if self.play_sound_dogFetch:
                self.sound_dogFetch.play(0)
                self.play_sound_dogFetch = False
                
        if aktualni_cas >= self.start_time + 13000 and aktualni_cas <= self.start_time + 18000 and self.told_wisdom == 0:
            self.text = "and I'll lend you wisdom beyond your comprehension"
            if self.play_sound3:
                self.sound3.play(0)
                self.play_sound3 = False
                
        if aktualni_cas > self.start_time + 18000 and self.told_wisdom == 0:
            self.speaking = False
                

        # Volani funkce tell_wisdom
        self.tell_wisdom(player)

        # Render a kresleni textu
        text_surface = font.render(self.text, True, (255, 255, 255))        
        screen.blit(text_surface, (780, 560))
        
