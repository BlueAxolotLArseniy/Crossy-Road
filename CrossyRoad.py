#V0.0016
#all import

from ursina import *
import random
import sys

#start

crossing_tree = False
last_key = None
wait_car = 0
gen = -10
camera_speed = 0
app = Ursina()
biggest_coordinate = 15
list_of_roads = []
list_of_cars = []
list_of_tree = []
list_of_all_models = []

player = Entity(model='models/player/chicken/chiken.glb', scale=(.2, .2, .2), position=(0, -0.5, -8), collider='box')
player.rotation_y = 180

camera.rotation_x = 40
camera.rotation_y = -20
camera.y = 14
camera.x = 9

#classes

class Grass():
    def __init__(self, z):
        self.xmodel = Entity(model='models/ground/grass/grass.glb', scale=(.3, .3, .3), position=(0, -1, z))

class Road():
    def __init__(self, z):
        self.xmodel = Entity(model='models/road/defolte/road.glb', scale=(.3, .3, .3), position=(0, -1, z))

class Car():
    def __init__(self, z, color):
        if color == 'red':
            self.xmodel = Entity(model='models/car/defolte_red/car_red.glb', scale=(.23, .23, .23), position=(-12, -.7, z), collider='box')
            self.xmodel.rotation_y = 180
class Tree():
    def __init__(self, z, type, x):
        if type == '2':
            self.xmodel = Entity(model='models/tree/defolte/tree2/tree2.glb', scale=(.2, .2, .2), position=(x, -0.5, z+0.2), collider='box')
            self.xmodel.rotation_y = 180

global_list_of_grass = [Grass(x) for x in range(-50, -20)]
global_list_of_roads = [Road(x) for x in range(-70, -20)]
global_list_of_trees = [Tree(x, '2', random.randint(-4, 7)) for x in range(-110, -20)]
global_list_of_cars = [Car(x, 'red') for x in range(-170, -20)]
global_list_of_gens = [x for x in range(-70, -20)]

#funcs

def movecamera():
    global camera_speed
    noun_x = player.z - (camera.z + 15)
    noun_x /= 50
    camera_speed = noun_x

    if camera_speed > 0:
        camera.z += camera_speed

def move_car():
    global wait_car, global_list_of_cars
    if wait_car % 300:
        for i in global_list_of_cars:
            if i.xmodel.rotation_y == 180:
                i.xmodel.x += 0.1
            else:
                i.xmodel.x -= 0.1

# def generation():
#     global gen, camera, objects, list_of_all_models
#     if random.randint(0, 2) != 0:
#         list_of_all_models.append(Road(gen))
#         list_of_roads.append(gen)
#         objects += 1
#     else:
#         list_of_all_models.append(Grass(gen))
#         q = Tree(gen, '2', random.randint(-3, 6))
#         list_of_all_models.append(q)
#         q = Tree(gen, '2', random.randint(-3, 6))
#         list_of_all_models.append(q)
#         q = Tree(gen, '2', random.randint(-3, 6))
#         list_of_all_models.append(q)
#         objects += 4
#     gen += 1

def generation():
    global global_list_of_roads, global_list_of_grass, global_list_of_trees, global_list_of_gens
    for i in range(-15, 10):
        global_list_of_grass[0].xmodel.z = i
        global_list_of_grass.append(global_list_of_grass.pop(0))

    for i in range(10, 15):
        if random.randint(1, 3) == 3:
            global_list_of_roads[0].xmodel.z = i
            global_list_of_roads.append(global_list_of_roads.pop(0))
            global_list_of_gens[0] = i
            global_list_of_gens.append(global_list_of_gens.pop(0))
        else:
            global_list_of_grass[0].xmodel.z = i
            global_list_of_grass.append(global_list_of_grass.pop(0))

            #X3
            for _ in range(3):
                global_list_of_trees[0].xmodel.z = i
                global_list_of_trees.append(global_list_of_trees.pop(0))

def move_generation():
    global global_list_of_roads, global_list_of_grass, biggest_coordinate
    if random.randint(1, 3) != 3:
        global_list_of_roads[0].xmodel.z = biggest_coordinate
        global_list_of_roads.append(global_list_of_roads.pop(0))
        global_list_of_gens[0] = biggest_coordinate
        global_list_of_gens.append(global_list_of_gens.pop(0))
        biggest_coordinate += 1
    else:
        global_list_of_grass[0].xmodel.z = biggest_coordinate
        global_list_of_grass.append(global_list_of_grass.pop(0))

        #X3
        for _ in range(3):
            global_list_of_trees[0].xmodel.z = biggest_coordinate
            global_list_of_trees.append(global_list_of_trees.pop(0))
        biggest_coordinate += 1

def create_and_move_car():
    global wait_car, list_of_roads, objects, list_of_cars, global_list_of_gens
    if wait_car % 50 == 0:
        for i in global_list_of_gens:
            if random.randint(0, 4) == 0:
                if random.randint(0, 1) == 1:
                    global_list_of_cars[0].xmodel.z = i
                    global_list_of_cars[0].xmodel.x = -12
                    global_list_of_cars[0].xmodel.rotation_y = 180
                    global_list_of_cars.append(global_list_of_cars.pop(0))
                else:
                    global_list_of_cars[0].xmodel.z = -i
                    global_list_of_cars[0].xmodel.x = 10
                    global_list_of_cars[0].xmodel.rotation_y = 0
                    global_list_of_cars.append(global_list_of_cars.pop(0))

def cross_tree():
    global player, last_key
    if str(player.intersects().entities).find("model='models/tree/defolte/tree2/tree2'") != -1:
        print('пересечение с деревом')
        if last_key == 'w': player.z -= 1
        if last_key == 's': player.z += 1
        if last_key == 'a': player.x += 1
        if last_key == 'd': player.x -= 1
        return 'true'


generation()

def input(key):
    global last_key
    if key == 'left mouse down':
        last_key = 'w'
        if player.z - camera.z < 24:
            player.z += 1
            player.rotation_y = 180
            if cross_tree() != 'true':
                move_generation()
    if key == 's':
        last_key = 's'
        player.z -= 1
        player.rotation_y = 0
    if key == 'w':
        last_key = 'w'
        if player.z - camera.z < 24:
            player.z += 1
            player.rotation_y = 180
            if cross_tree() != 'true':
                move_generation()
    if key == 'a':
        last_key = 'a'
        if player.x > -3.7:
            player.x -= 1
            player.rotation_y = 90
    if key == 'd':
        last_key = 'd'
        if player.x < 6.7:
            player.x += 1
            player.rotation_y = 270
    if key == 'q':
        sys.exit()
    cross_tree()


def update():
    global test_cube, wait_car, objects
    movecamera()
    camera.z += 0.01
    if player.z - camera.z < 10:
        sys.exit()
    wait_car += 1
    create_and_move_car()
    move_car()
    if str(player.intersects().entities).find("model='models/car/defolte_red/car_red'") != -1:
        print('пересечение с машиной')
    cross_tree()
    #remove_models()

    print(biggest_coordinate)



app.run()