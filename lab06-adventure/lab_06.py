#crear la clase en la cual se incluirán las habitaciones
class Room:
    #atributos
    def __init__(self, description, south, east, north, west):
        self.description = ""
        self.south = 0
        self.east = 0
        self.north = 0
        self.west = 0
#def para crear y modificar las distintas habitaciones
def rooms():
    room_list = []

    p1 = Room("Estás en pasillo, puedes avanzar uno hacia el centro del pasillo, desde el cual hay una puerta al norte y una al oeste o ir al este o al oeste",west=1, north=1, east=1)
    room_list.append(p1)

    p2 = Room("Estás en pasillo2,n/o/e/q(quit)",north=1,west=1,east=1)
    room_list.append(p2)

    h1 = Room("Estás en la h1,e/q(quit)",east=1)
    room_list.append(h1)

    h2 = Room("Estás en h2, e/q(quit)",east=1)
    room_list.append(h2)

    s = Room("Estás en s, w/n/q(quit)", north=1,west=1)
    room_list.append(s)

    c = Room("Estás en c, s/q(quit)",south=1)
    room_list.append(c)

    b = Room("Estás en b, s/q(quit)",south=1 )
    room_list.append(b)

    return room_list
def main():
    room_list = rooms()
    current_room = p1
    quit = False
    while not quit:
        print()
        print(room_list[room_list.index(current_room)].description)
        entrada = str(input("¿Donde quieres ir?"))
        if entrada == "n" and room_list[current_room].north == 1:
