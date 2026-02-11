import requests
import arcade
import PIL
MAX_SPN = 50
MIN_SPN = 0.05
class App(arcade.Window):
    def __init__(self):
        super().__init__(800, 600)


def setup_game():
    game = App()
    return game


def main():
    setup_game()
    arcade.run()


if __name__ == "__main__":
    main()