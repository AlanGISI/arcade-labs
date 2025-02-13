"""
Programa propio para la práctica dos del lab, aprendiendo a dubujar.
"""

#---importo la bibloteca que voy a usar
import arcade

#---abrir la ventana en la cual estará el dibujo
arcade.open_window(1080, 720, "Dibujo de la más alta calidad :D")

#---Definir el color de fondo de la ventana
arcade.set_background_color(arcade.color.CADMIUM_GREEN	)

#---insertar las figuras
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

#lanza
arcade.draw_rectangle_filled(380,340,7,250,arcade.color.BRONZE,45)
arcade.draw_triangle_filled(484,450,460,436,476,423,arcade.color.DARK_GRAY)

#aro cubre punta lanza
arcade.draw_circle_outline(540,510,90,arcade.color.WHITE,10)

#termino el renderizado
arcade.finish_render()

#bucle para mantener la ventana abierta
arcade.run()