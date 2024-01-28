import pygame
        

def save_game(player, game_timer, coins, npc):
    
    with open("save.txt", "w") as file:
        # Uklada obrazovku na ktere je hrac, hracovu X a Y pozici a cas casovac
        file.write(str(player.current_screen) + '\n')
        file.write(str(player.rect.x) + '\n')
        file.write(str(player.rect.y) + '\n')
        file.write(game_timer.get_time() + '\n')

        # Uklada maximalni pocet coinu
        file.write(str(len(coins.can_draw)) + '\n')

        # Uklada hracovy posbirane coiny
        file.write(str(coins.player_coins) + '\n')
        
        # Uklada ktere coiny byly posbirany
        for status in coins.can_draw:
            file.write(str(int(status)) + '\n')
            
        # Uklada pocet dialogu s NPC (aby se neopakoval po loadu hry)
        file.write(str(npc.told_wisdom))

            
def load_game(player, game_timer, coins, npc):
    
    with open('save.txt', 'r') as file:
        # Nacita obrazovku na ktere je hrac, hracovu X a Y pozici a cas casovace
        player.current_screen = int(file.readline().strip())
        player.rect.x = int(file.readline().strip())
        player.rect.y = int(file.readline().strip())
        time_str = file.readline().strip()
        
        # Set casu casovace
        game_timer.set_time(time_str)

        # Nacita maximalni pocet coinu
        total_coins = int(file.readline().strip())

        # Nacita hracovy posbirane coiny
        coins.player_coins = int(file.readline().strip())

        # Nacita coiny, ktere byly posbirany
        coins.can_draw = [bool(int(file.readline().strip())) for _ in range(total_coins)]
        
        # Nacita pocet dialogu s NPC
        npc.told_wisdom = int(file.readline().strip())
        




