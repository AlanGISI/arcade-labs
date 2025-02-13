#---importo la bibloteca que voy a usar
import arcade

#--- codigo que genera el dibujo en sí
def piramide():
    arcade.draw_triangle_filled(300,5,780,5,540,300,arcade.color.AMBER)

def sol():
    arcade.draw_circle_filled(0,720,200,arcade.color.AUREOLIN)

def fondo():
    arcade.set_background_color(arcade.color.BLACK)

def arena():
    arcade.draw_rectangle_filled(540,5,1090,10,)

def main():
    arcade.open_window(1080, 720, "Dibujo de la más alta calidad 2 :D")
    fondo()
    arcade.start_render()
#-----
    arcade.finish_render()
    arcade.run()
