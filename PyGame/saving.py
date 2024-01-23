import pygame
        

def save_game(player, game_timer, coins):
    with open("save.txt", "w") as file:
        file.write(str(player.current_screen) + '\n')
        file.write(str(player.rect.x) + '\n')
        file.write(str(player.rect.y) + '\n')
        file.write(game_timer.get_time() + '\n')

        # Save the total number of coins (including those not collected)
        file.write(str(len(coins.can_draw)) + '\n')

        # Save the player's collected coins
        file.write(str(coins.player_coins) + '\n')
        
        # Save which coins have been collected
        for status in coins.can_draw:
            file.write(str(int(status)) + '\n')

            

def load_game(player, game_timer, coins):
    with open('save.txt', 'r') as file:
        player.current_screen = int(file.readline().strip())
        player.rect.x = int(file.readline().strip())
        player.rect.y = int(file.readline().strip())
        time_str = file.readline().strip()
        game_timer.set_time(time_str)

        # Load the total number of coins
        total_coins = int(file.readline().strip())

        # Load the player's collected coins
        coins.player_coins = int(file.readline().strip())

        # Load which coins have been collected
        coins.can_draw = [bool(int(file.readline().strip())) for _ in range(total_coins)]




