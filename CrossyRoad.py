#V0.0011
#all import

from ursina import *
import random
from direct.actor.Actor import Actor
import sys

#start

q = None #no global!
objects = 3
last_key = None
wait_car = 0
gen = 15
camera_speed = 0
app = Ursina()
list_of_roads = []
list_of_cars = []
list_of_tree = []
list_of_all_models = []

playerX = Entity(model='models/player/chicken/chiken.glb', scale=(.2, .2, .2), position=(0, -0.5, -8), collider='box')
playerX.rotation_y = 180
player = Entity(scale=(.3, .3, .3))
test_cube = Entity(model='cube', position=(-2, 0, 0))

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

#models and others

Acar = Actor("models/car/defolte_red/car_red.glb")
Acar.reparentTo(player)

#funcs

def generation():
    global gen, camera, objects, list_of_all_models
    if random.randint(0, 2) != 0:
        list_of_all_models.append(Road(gen))
        list_of_roads.append(gen)
        objects += 1
    else:
        list_of_all_models.append(Grass(gen))
        q = Tree(gen, '2', random.randint(-3, 6))
        list_of_all_models.append(q)
        q = Tree(gen, '2', random.randint(-3, 6))
        list_of_all_models.append(q)
        q = Tree(gen, '2', random.randint(-3, 6))
        list_of_all_models.append(q)
        objects += 4
    gen += 1

def movecamera():
    global camera_speed
    noun_x = playerX.z - (camera.z + 15)
    noun_x /= 50
    camera_speed = noun_x

    if camera_speed > 0:
        camera.z += camera_speed

def move_car():
    global wait_car, list_of_cars
    if wait_car % 300:
        for i in list_of_cars:
            i.xmodel.x += 0.1

for i in range(5, 20):
    Grass(-i)
for i in range(-4, 15):
    if random.randint(0, 1) == 0:
        q = Road(i)
        list_of_all_models.append(q)

        objects += 1
    else:
        q = Grass(i)
        list_of_all_models.append(q)
        objects += 1

def remove_gen():
    global list_of_roads, playerX
    for i in list_of_roads:
        if playerX.z - i > 10:
            list_of_roads.remove(i)

def remove_models():
    global list_of_all_models, playerX
    for i in list_of_all_models:
        if playerX.z - i.xmodel.z > 1:
            # i.xmodel.disable()
            i.xmodel.destroy()
            # list_of_all_models.remove(i.xmodel)

def create_car():
    global wait_car, list_of_roads, objects, list_of_cars
    if wait_car % 20 == 0:
        for i in list_of_roads:
            if random.randint(0, 9) == 0:
                q = Car(i, 'red')
                objects += 1
                list_of_cars.append(q)
                list_of_all_models.append(q)
            else:
                pass

def cross_tree():
    global playerX, last_key
    if str(playerX.intersects().entities).find("model='models/tree/defolte/tree2/tree2'") != -1:
        print('пересечение с деревом')
        if last_key == 'w': playerX.z -= 1
        if last_key == 's': playerX.z += 1
        if last_key == 'a': playerX.x += 1
        if last_key == 'd': playerX.x -= 1

def input(key):
    global last_key
    if key == 'left mouse down':
        last_key = 'w'
        generation()
        playerX.z += 1
        playerX.rotation_y = 180
    if key == 's':
        last_key = 's'
        generation()
        playerX.z -= 1
        playerX.rotation_y = 0
    if key == 'w':
        last_key = 'w'
        generation()
        playerX.z += 1
        playerX.rotation_y = 180
    if key == 'a':
        last_key = 'a'
        generation()
        if playerX.x > -3.7:
            playerX.x -= 1
            playerX.rotation_y = 90
    if key == 'd':
        last_key = 'd'
        generation()
        if playerX.x < 6.7:
            playerX.x += 1
            playerX.rotation_y = 270
    if key == 'q':
        sys.exit()
    cross_tree()


def update():
    global test_cube, wait_car, objects
    movecamera()
    camera.z += 0.01
    if playerX.z - camera.z < 10:
        sys.exit()
    wait_car += 1
    create_car()
    remove_gen()
    move_car()
    if str(playerX.intersects().entities).find("model='models/car/defolte_red/car_red'") != -1:
        print('пересечение с машиной')
    cross_tree()
    #remove_models()

    print(objects)



app.run()