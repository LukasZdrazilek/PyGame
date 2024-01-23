import pygame
from map import Map

class Player:
    def __init__(self):
        
        # Nacitani textur hrace
        self.default_image = pygame.image.load('Textures/Player/Ted_idle_right.png')
        self.Ted_idle_left = pygame.image.load('Textures/Player/Ted_idle_left.png')
        self.Ted_jump_charge = pygame.image.load('Textures/Player/Ted_jump_charge.png')
        self.Ted_jump_left = pygame.image.load('Textures/Player/Ted_jump_left.png')
        self.Ted_jump_right = pygame.image.load('Textures/Player/Ted_jump_right.png')
        self.Ted_fall_left = pygame.image.load('Textures/Player/Ted_fall_left.png')
        self.Ted_fall_right = pygame.image.load('Textures/Player/Ted_fall_right.png')
        self.Ted_walk1_left = pygame.image.load('Textures/Player/Ted_walk1_left.png')
        self.Ted_walk1_right = pygame.image.load('Textures/Player/Ted_walk1_right.png')
        self.Ted_walk2_left = pygame.image.load('Textures/Player/Ted_walk2_left.png')
        self.Ted_walk2_right = pygame.image.load('Textures/Player/Ted_walk2_right.png')
        self.Ted_walk3_left = pygame.image.load('Textures/Player/Ted_walk3_left.png')
        self.Ted_walk3_right = pygame.image.load('Textures/Player/Ted_walk3_right.png')

        # Set default textury a velikosti rectanglu
        self.image = self.default_image
        self.rect = self.image.get_rect()
        
        # Nastaveni pocatecni pozice hrace
        self.rect.x = 600
        self.rect.y = 700

        self.isJumping = False
        self.isInJump = False
        self.isFalling = False
        self.isFallingLeft = False
        self.isFallingRight = False
        self.isOnObject = False
        self.movingLeft = False
        self.movingRight = False
        self.jumpingLeft = False
        self.jumpingRight = False
        self.jumpingStraightUp = False
        self.wasMovingLeft = False
        self.wasMovingRight = False
        self.canWalk = False
        self.canJump = False
        self.bouncing = False
        self.bouncingTop = False
        self.countTime1 = True
        self.countTime2 = True
        self.GROUND_POSITION = 960
        self.current_screen = 0
        
        self.xJumpingSlowdown = 0
        self.yJumpingSlowdown = 0
        self.xFallingSpeed = 300
        
        self.last_texture_change_time = pygame.time.get_ticks()
        self.texture_change_interval = 100


    # Kresli texturu hrace na obrazovku
    def draw(self, screen):
        screen.blit(self.image, self.rect)


    # Logika a ovladani hrace
    def controls(self, dt, map_objects):
        key = pygame.key.get_pressed()
        aktualni_cas = pygame.time.get_ticks()
        aktualni_cas_textury = pygame.time.get_ticks()  
        
        
        # Pohyb hrace vlevo a vpravo, pokud neskace a nepada
        if key[pygame.K_a] and self.isJumping == False and self.canWalk == True:
            
            self.rect.x -= 600 * dt
            self.movingLeft = True
            self.wasMovingLeft = True
            self.wasMovingRight = False

        elif key[pygame.K_d] and self.isJumping == False and self.canWalk == True:
          
            self.rect.x += 600 * dt
            self.movingRight = True
            self.wasMovingRight = True
            self.wasMovingLeft = False
            
        else:
            self.movingRight = False
            self.movingLeft = False
            

        # Hrozna logika textur pro animaci chozeni vlevo a vpravo 
        if self.isJumping == False and self.canWalk == True:
            if self.movingLeft:
                if aktualni_cas_textury - self.last_texture_change_time >= self.texture_change_interval:
                    self.last_texture_change_time = aktualni_cas_textury
                    if self.image == self.default_image or self.image == self.Ted_idle_left or self.image == self.Ted_fall_left or self.image == self.Ted_fall_right or self.image == self.Ted_walk1_right or self.image == self.Ted_walk2_right or self.image == self.Ted_walk3_right:
                        self.image = self.Ted_walk1_left
                    elif self.image == self.Ted_walk1_left:
                        self.image = self.Ted_walk2_left
                    elif self.image == self.Ted_walk2_left:
                        self.image = self.Ted_walk3_left
                    elif self.image == self.Ted_walk3_left:
                        self.image = self.Ted_walk2_left

            elif self.movingRight:
                if aktualni_cas_textury - self.last_texture_change_time >= self.texture_change_interval:
                    self.last_texture_change_time = aktualni_cas_textury
                    if self.image == self.default_image or self.image == self.Ted_idle_left or self.image == self.Ted_fall_right or self.image == self.Ted_fall_left:
                        self.image = self.Ted_walk1_right
                    elif self.image == self.Ted_walk1_right:
                        self.image = self.Ted_walk2_right
                    elif self.image == self.Ted_walk2_right:
                        self.image = self.Ted_walk3_right
                    elif self.image == self.Ted_walk3_right:
                        self.image = self.Ted_walk2_right
            else:
                # Reset textur kdyz se hrac nehybe
                if self.wasMovingRight:
                    self.image = self.default_image
                elif self.wasMovingLeft:
                    self.image = self.Ted_idle_left        


        # Hrac stiskne a drzi mezernik, zaznamena se cas stisku
        if key[pygame.K_SPACE] and self.isJumping == False and self.countTime1:
            
            # Zaznam casu stisku a ochrana proti loopu
            if self.countTime1 == True:
                self.jump_start_time = aktualni_cas
                self.countTime1 = False

            self.image = self.Ted_jump_charge
            self.isJumping = True
            self.jumpingRight = False
            self.jumpingLeft = False


        # Zmena smeru skoku pri drzeni mezerniku
        if key[pygame.K_SPACE] and self.isJumping == True:
            
            # 'A' hrac bude skakat vlevo
            if key[pygame.K_a]:
                self.jumpingLeft = True
                self.wasMovingLeft = True
                self.wasMovingRight = False

            # 'D' = hrac bude skakat vpravo
            elif key[pygame.K_d]:
                self.jumpingRight = True
                self.wasMovingRight = True
                self.wasMovingLeft = False


        # Hrac pusti mezernik, zaznamena se cas pusteni
        if not key[pygame.K_SPACE] and self.isJumping == True:
            
            # Zaznam casu pusteni a ochrana proti loopu
            if self.countTime2 == True:
                self.jump_end_time = aktualni_cas
                self.countTime2 = False

            # Maximalni vyska skoku podle max casu
            self.jump_duration = self.jump_end_time - self.jump_start_time
            if self.jump_duration > 1200:   # Zde se upravuje max vyska skoku v milisekundach
                self.jump_duration = 1200

            # Dokud se aktualni cas nerovna aktualnimu casu + doby skoku, hrac skace
            if aktualni_cas <= (self.jump_end_time + (self.jump_duration)):
                
               self.isInJump = True

               # Skok rovne nahoru
               if aktualni_cas <= (self.jump_end_time + (self.jump_duration / 2)) and self.bouncingTop == False:
                   if self.wasMovingRight == True:
                       self.image = self.Ted_jump_right
                   elif self.wasMovingLeft == True:
                       self.image = self.Ted_jump_left
                   self.rect.y -= (2500.0 - self.xJumpingSlowdown) * dt     # Zde se upravuje sila skoku
                   self.xJumpingSlowdown += 30000.0 / (self.jump_duration / 2) # 25  # Zde se upravuje postupne zpomaleni skoku (cislo 30.000 vymysleno podle pocitu)
                   
                   # Skok vlevo a vpravo nahoru
                   if self.jumpingLeft == True:
                       self.rect.x -= 700 * dt     
                       self.image = self.Ted_jump_left

                   elif self.jumpingRight == True:
                       self.rect.x += 700 * dt
                       self.image = self.Ted_jump_right
                   
                   else:
                       self.jumpingStraightUp = True

               # Bounce z vrchu platformy
               elif aktualni_cas <= (self.jump_end_time + (self.jump_duration / 2)) and self.bouncingTop == True and self.bouncing == False:
                   
                   self.image = self.Ted_fall_right

                   # Bounce vlevo nebo vpravo
                   if self.jumpingLeft == True:
                       self.image = self.Ted_fall_left
                       self.rect.x -= 700 * dt         

                   if self.jumpingRight == True:
                       self.image = self.Ted_fall_right
                       self.rect.x += 700 * dt 
                       
               else:
                   #######################################################
                   self.rect.y += (-410.0 + self.yJumpingSlowdown) * dt
                   self.yJumpingSlowdown += 60#############################
                   if self.yJumpingSlowdown > 1200:                 # 690 max
                       self.yJumpingSlowdown = 1200

                   # Padani vlevo a vpravo pouze vlivem gravitace ale stale v case padani
                   if self.jumpingLeft == True:
                       self.image = self.Ted_fall_left
                       self.rect.x -= 700 * dt

                   if self.jumpingRight == True:
                       self.image = self.Ted_fall_right
                       self.rect.x += 700 * dt  
                           
            
            else:
                # Hrac uz neskace, neni v case skoku, jen pada gravitaci
                self.isInJump = False
                
                # Padani vlevo a vpravo pouze vlivem gravitace
                if self.jumpingLeft == True:
                    self.image = self.Ted_fall_left         ############### Nejde to udelat smooth ( zatim )
                    self.rect.x -= (200) * dt

                elif self.jumpingRight == True:
                    self.image = self.Ted_fall_right
                    self.rect.x += (200) * dt
                    
                
                # Spadl dolu, je na zemi nebo platforme
                if self.canWalk == True:
                    self.bouncingTop = False
                    self.isJumping = False
                    self.countTime1 = True
                    self.countTime2 = True
                    self.jumpingLeft = False
                    self.jumpingRight = False
                    self.jumpingStraightUp = False
                    self.movingLeft = False
                    self.movingRight = False
                    self.xJumpingSlowdown = 0
                    self.yJumpingSlowdown = 0
                    self.xFallingSpeed = 300


        # Kontrola proti skakani v padani
        if self.isInJump == False and self.canWalk == False:
            if key[pygame.K_SPACE]:
                self.isJumping = False#####################################################
                self.countTime1 = False
            else:
                self.countTime1 = True

        # X pohyb v padani po skoku nebo po sejiti z platformy
        if not self.isJumping and not key[pygame.K_a] and not key[pygame.K_d] and not self.image == self.default_image and not self.image == self.Ted_idle_left and not self.jumpingStraightUp:
            self.isFalling = True                          # isInJump, canWalk a jumpingStraightUp                 # Cursed AF but kinda works
            if self.wasMovingRight == True:
                self.isFallingRight = True
                self.image = self.Ted_fall_right
                self.rect.x += (self.xFallingSpeed) * dt
                self.xFallingSpeed -= 12                    # SMOOTH FALL
                if self.xFallingSpeed < 0:
                    self.xFallingSpeed = 0
                
            elif self.wasMovingLeft == True:
                self.isFallingLeft = True
                self.image = self.Ted_fall_left
                self.rect.x -= (self.xFallingSpeed) * dt
                self.xFallingSpeed -= 12
                if self.xFallingSpeed < 0:
                    self.xFallingSpeed = 0
        else:
            self.xFallingSpeed = 300
            if self.canWalk == True and self.isJumping == False and self.movingLeft == False and self.movingRight == False:
                self.isFalling = False
                self.isFallingLeft = False
                self.isFallingRight = False
                if self.wasMovingRight == True:
                    self.image = self.default_image
                elif self.wasMovingLeft == True:
                    self.image = self.Ted_idle_left
        

        # Kolize
        for obj in map_objects[self.current_screen]:

            # Handle Y-axis collisions
            if self.rect.colliderect(obj):
                self.rect.y -= 800 * dt
                # Collision from the top of the object
                if self.rect.bottom == obj.rect.top:
                    if obj.topPlatform == True:
                        self.rect.bottom = obj.rect.top
                    
                # Collision from the bottom of the object
                elif self.rect.top <= obj.rect.bottom and self.rect.bottom > obj.rect.bottom:
                    if obj.botPlatform == True:
                        self.rect.top = obj.rect.bottom
                        self.bouncingTop = True
        

            # Handle X-axis collisions
            self.bouncing = False
            #player.canWalk = False

            if self.rect.colliderect(obj.rect):
                if self.rect.right >= obj.rect.left and self.rect.left < obj.rect.left:  # Player is on the right, not moving
                    self.rect.right = obj.rect.left
                    # Bounce zprava
                    if self.jumpingRight or self.isFallingRight:###################falling right333333333333333333333333333333333333333333333333333333
                        self.jumpingLeft = True
                        self.jumpingRight = False
                        self.wasMovingRight = False
                        self.wasMovingLeft = True
                        self.bouncing = True
                elif self.rect.left <= obj.rect.right and self.rect.right > obj.rect.right:  # Player is on the left, not moving
                    self.rect.left = obj.rect.right
                    # Bounce zleva
                    if self.jumpingLeft or self.isFallingLeft:###################falling left333333333333333333333333333333333333333333333333333333333
                        self.jumpingRight = True
                        self.jumpingLeft = False
                        self.wasMovingLeft = False
                        self.wasMovingRight = True
                        self.bouncing = True

        # Gravity
        self.rect.y += 800 * dt
            

        # Prechod na dalsi screen
        if self.rect.y < 0:
            self.current_screen += 1
            self.rect.y = 960
        elif self.rect.y > 960:
            self.current_screen -= 1
            self.rect.y = 0
            

################################# TO DO LIST ####################################

# Kdyz drzim A nebo D pri schazeni platformy dolu tak to neni smooth, jde rovne dolu //// kdyz pada tak self.canWalk = False

# Zachyceni na platforme ------------------- Je to gravitaci        NOT A PROBLEM?? maybe..

# !!!!!!!!!!!!! BIG PROBLEM (?)- ve skoku se da mezernikem zastavit a v padu po skoku taky !!!!!!!!!!!!!!!!!!

#   Coins TEXTURY

#   Dodelat NPC

