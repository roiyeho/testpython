# ui.py

def print_welcome_message():
    print("Welcome to my amazing game!")
    print("Press ENTER to start")
    input()

def draw_board():
    print("======================")
    print("======================")
    print("===== Game board =====")
    print("======================")
    print("======================")
    print()

def get_move(player_num):
    print("Player {}: it's your turn".format(player_num))
    move = input("Enter your move: ")
    return move


