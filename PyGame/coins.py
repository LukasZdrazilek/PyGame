import pygame
import time

class Coins:
    def __init__(self):
        
        # Nacitani textur a zvuku sebrani coiny
        self.textures = [
            pygame.image.load('Textures/Coin/coin1.png'),
            pygame.image.load('Textures/Coin/coin2.png'),
            pygame.image.load('Textures/Coin/coin3.png')
        ]
        
        self.coin = pygame.mixer.Sound('Sound/coin.wav')

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


    # Hrac da coinu NPC (dotkne se ho)
    def give_coin(self, player, npc):
        
        # Koliduje hrac s NPC, ma vic jako 0 coinu a NPC zrovna nerika wisdom
        if player.rect.colliderect(npc.rect) and player.current_screen == 0 and self.player_coins > 0 and npc.telling_wisdom == False:
            self.player_coins -= 1
            npc.telling_wisdom = True
            npc.told_wisdom += 1
            
            # Zacatek casovace rikani wisdomu
            if npc.told_wisdom == 1:
                npc.start_wisdom_timer1 = True
                
            if npc.told_wisdom == 2:
                npc.start_wisdom_timer2 = True
                
            if npc.told_wisdom == 3:
                npc.start_wisdom_timer3 = True
                
            
        # NPC rika wisdom, nahraje se aktualni cas a hrac mu nemuze davat coiny dokud neskonci
        if npc.telling_wisdom:
            if npc.tells_wisdom:
                npc.tell_wisdom(player)
                npc.tells_wisdom = False

    
    # Logika coinu
    def handle_coins(self, screen, player, npc):
        
        # Prochazeni coinu podle listu can_draw
        for i in range(len(self.can_draw)):
            if self.can_draw[player.current_screen]:
                
                # Animace textury coiny dle casu
                if time.time() - self.last_texture_change >= 0.5:
                    
                    self.pattern_index = (self.pattern_index + 1) % len(self.pattern)
                    self.image_index = self.pattern[self.pattern_index]
                    self.image = self.textures[self.image_index]
                    self.last_texture_change = time.time()

                # Vykresleni coin podle obrazovky hrace
                self.rect.x = self.coinsX[player.current_screen]
                self.rect.y = self.coinsY[player.current_screen]

                screen.blit(self.image, self.rect)

                # Sebrani coiny
                if self.rect.colliderect(player.rect) and self.can_draw[i]:
                    
                    self.coin.play()
                    self.player_coins += 1
                    self.can_draw[i] = False
            
        # Volani give_coin
        self.give_coin(player, npc)
                    
        
