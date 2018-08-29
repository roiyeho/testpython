# game.py

# import the ui module
import ui

def start():
    ui.print_welcome_message()
    play_game()

def play_game():
    current_player = 0
    current_move = None

    while current_move != "exit":
        ui.draw_board()
        current_move = ui.get_move(current_player)
        current_player = 1 - current_player

if __name__ == "__main__":
    start()

