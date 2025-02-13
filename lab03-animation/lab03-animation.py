#---importo la bibloteca que voy a usar
import arcade

#--- codigo que genera el dibujo en sí
def piramide():
    arcade.draw_triangle_filled(300,40,780,40,540,450,arcade.color.AMBER)

def sol():
    arcade.draw_circle_filled(0,720,200,arcade.color.AUREOLIN)

def fondo():
    arcade.set_background_color(arcade.color.BLACK)

def arena():
    arcade.draw_rectangle_filled(540,30,1090,60,arcade.color.ARYLIDE_YELLOW)

def main():
    arcade.open_window(1080, 720, "Dibujo de la más alta calidad 2 :D")
    fondo()
    #elementos a partir de aquí
    arcade.start_render()
    arena()
    sol()
    piramide()
    arcade.finish_render()
    arcade.run()
main()