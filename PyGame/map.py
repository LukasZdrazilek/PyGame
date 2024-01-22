import pygame

# List objektu mapy  ( vlastne jen jejich kolizi - zdi, platforerm a zeme ) 
map_objects = [[]]

class Map:
    def __init__(self, x, y, width, height, type):

        self.rect = pygame.Rect(x, y, width, height)
        self.topPlatform = False
        self.botPlatform = False
        
        if type == "Top":
            self.topPlatform = True
            
        elif type == "Bot":
            self.botPlatform = True
            
        elif type == "Solo":
            self.topPlatform = True
            self.botPlatform = True 
            
        else:
            self.topPlatform = False
            self.botPlatform = False


    # Pouze pro testovani hratelnosti mapy, v samotne hre se pak nepouziva
    def draw(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), self.rect)


    def collide_with(self, player_rect):
        return self.rect.colliderect(player_rect)
        

# Konstruktor objektu mapy
def create_map_object(x, y, width, height, screenNo, type):
    mapObject = Map(x, y, width, height, type)
    
    if screenNo >= len(map_objects):
        map_objects.append([])
        
    map_objects[screenNo].append(mapObject)
    return mapObject


# Funkce ktera cte z textaku mapy podle znaku, '\n' mezi nimi = nova screen
# '+' = rectangle ktery funguje jako bocni kolize ( zdi a platformy), '-' = nic se nevykresli, 'T' = top platform kdy se aktivuje horni kolize, 
# 'B' = bot platform kdy se aktivuje spodni kolize, 'S' = solo platform kdy se aktivuji obe kolize
with open("map.txt", "r") as file:
    content = file.read()

line_count = 0
character_count = 0
screen = 0
next_screen = False

for i, char in enumerate(content):
    
    if char == '\n':
        if next_screen == True:
            line_count = -1
            screen += 1
            
        line_count += 1
        character_count = 0
        next_screen = True

    elif char == '+':
        pixelX_count = character_count * 40
        pixelY_count = line_count * 40
        mapObject = create_map_object(pixelX_count, pixelY_count, 40, 40, screen, "")
        character_count += 1
        next_screen = False
        
    elif char == 'T':
        pixelX_count = character_count * 40
        pixelY_count = line_count * 40
        mapObject = create_map_object(pixelX_count, pixelY_count, 40, 40, screen, "Top")
        character_count += 1
        next_screen = False
        
    elif char == 'B':
        pixelX_count = character_count * 40
        pixelY_count = line_count * 40
        mapObject = create_map_object(pixelX_count, pixelY_count, 40, 40, screen, "Bot")
        character_count += 1
        next_screen = False
        
    elif char == 'S':
        pixelX_count = character_count * 40
        pixelY_count = line_count * 40
        mapObject = create_map_object(pixelX_count, pixelY_count, 40, 40, screen, "Solo")
        character_count += 1
        next_screen = False

    elif char == '-':
        pixelX_count = character_count * 40
        pixelY_count = line_count * 40
        character_count += 1
        next_screen = False
        

    