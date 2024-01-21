import pygame
        

def save_game(player, game_timer):
    
    with open("save.txt", "w") as file:
   
        file.write(str(player.current_screen) + '\n')
        file.write(str(player.rect.x) + '\n')
        file.write(str(player.rect.y) + '\n')
        file.write(game_timer.get_time())
            

def load_game(player, game_timer):
    with open('save.txt', 'r') as file:
        
        player.current_screen = int(file.readline().strip())
        player.rect.x = int(file.readline().strip())
        player.rect.y = int(file.readline().strip())
        time_str = file.readline().strip()
        
        game_timer.set_time(time_str)



