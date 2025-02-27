import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")
        self.Muro = Muro()
        self.Bola = Bola()
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        self.clear()
        self.Bola.draw()
        self.Muro.draw()

    def on_update(self, delta_time):
        self.Bola.update()

    def on_mouse_motion(self, x, y, dx, dy):
        self.Bola.update_position(x, y)


class Bola:
    def __init__(self):
        self.center_x = SCREEN_WIDTH // 2
        self.center_y = SCREEN_HEIGHT // 2

    def update_position(self, x, y):
        self.center_x = max(20, min(x, SCREEN_WIDTH - 20))
        self.center_y = max(20, min(y, SCREEN_HEIGHT - 20))

    def draw(self):
        arcade.draw_circle_filled(self.center_x, self.center_y, 20, arcade.color.WHITE)

class Muro:
    def __init__(self):
        self.center_x = SCREEN_WIDTH - SCREEN_WIDTH // 4
        self.center_y = SCREEN_HEIGHT // 2

    def draw(self):
        arcade.draw_rectangle_filled(self.center_x, self.center_y, 10, 500, arcade.color.WHITE)


def main():
    window = MyGame()
    arcade.run()


main()
