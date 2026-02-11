import requests
import arcade
import PIL
from pyglet.event import EVENT_HANDLE_STATE

MAX_SPN = 50
MIN_SPN = 0.05
map_api_server = "https://static-maps.yandex.ru/v1"
api_key = "f3a0fe3a-b07e-4840-a1da-06f18b2ddf13"


class App(arcade.Window):
    def __init__(self, x, y):
        super().__init__(800, 600)
        self.width = 800
        self.height = 600
        self.x = float(x)
        self.y = float(y)
        self.span = 1

        resp = requests.get(url=map_api_server, params={'ll': f"{self.x},{self.y}",
                                                        'spn': f"{self.span},{self.span}",
                                                        'apikey': str(api_key)})
        with open("map.png", "wb") as mp:
            mp.write(resp.content)
        self.texture = arcade.load_texture("map.png")
        arcade.draw_texture_rect(self.texture,
                                 arcade.rect.XYWH(self.width // 2, self.height // 2, self.width, self.height))

    def on_key_press(self, key, modifiers):
        if arcade.key.PAGEUP == key:
            self.span *= 1.4 if self.span * 1.4 < MAX_SPN else MAX_SPN
        if arcade.key.PAGEDOWN == key:
            self.span /= 1.4 if self.span / 1.4 > MIN_SPN else MIN_SPN

        resp = requests.get(url=map_api_server, params={'ll': f"{self.x},{self.y}",
                                                        'spn': f"{self.span},{self.span}",
                                                        'apikey': str(api_key)})
        with open("map.png", "wb") as mp:
            mp.write(resp.content)
        self.texture = arcade.load_texture("map.png")
        step_move = self.span * 0.8
        if arcade.key.LEFT == key:
            self.x -= step_move
        elif arcade.key.RIGHT == key:
            self.x += step_move
        if arcade.key.UP == key:
            self.y += step_move
        if arcade.key.DOWN == key:
            self.y -= step_move

    def on_update(self, delta_time):
        print(self.span)

        """"""

    def on_draw(self):
        arcade.draw_texture_rect(self.texture,
                                 arcade.rect.XYWH(self.width // 2, self.height // 2, self.width, self.height))


def setup_game(coord_x, coord_y):
    game = App(coord_x, coord_y)
    return game


def main(coord_x, coord_y):
    setup_game(coord_x, coord_y)
    arcade.run()


if __name__ == "__main__":
    main(input(), input())
