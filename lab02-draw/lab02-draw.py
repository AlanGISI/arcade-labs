"""
Programa propio para la práctica dos del lab, aprendiendo a dubujar.
"""

#1º importo la bibloteca que voy a usar
import arcade
from arcade.color import COOL_BLACK

#abrir la ventana en la cual estará el dibujo
arcade.open_window(1080, 720, "Dibujo de la más alta calidad :D")

# Definir el color de fondo de la ventana
arcade.set_background_color(arcade.color.CADMIUM_GREEN	)

#insertar las figuras
#iniciar renderizado
arcade.start_render()

#base
arcade.draw_rectangle_filled(540,160,20,320,arcade.color.DARK_BROWN,0)

#circulo base
arcade.draw_circle_filled(540,510,200,arcade.color.BLACK)

#circulos menores
arcade.draw_circle_filled(540,510,180,arcade.color.WHITE)
arcade.draw_circle_filled(540,510,160,arcade.color.BLACK)
arcade.draw_circle_filled(540,510,140,arcade.color.WHITE)
arcade.draw_circle_filled(540,510,120,arcade.color.BLACK)
arcade.draw_circle_filled(540,510,100,arcade.color.WHITE)
arcade.draw_circle_filled(540,510,80,arcade.color.BLACK)
arcade.draw_circle_filled(540,510,60,arcade.color.WHITE)
arcade.draw_circle_filled(540,510,40,arcade.color.BLACK)
arcade.draw_circle_filled(540,510,20,arcade.color.WHITE)
arcade.draw_circle_filled(540,510,10,arcade.color.RED)

#flecha
#arcade.draw





arcade.finish_render()

arcade.run()