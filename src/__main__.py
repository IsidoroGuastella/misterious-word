# src/__main__.py
from src.user import User
from src.engine import start_game

def main():
    player = User()  # default Guest
    player.welcome()
    start_game(player)

if __name__ == "__main__":
    main()
