#all import

from ursina import *
import random
from direct.actor.Actor import Actor
import sys

#start

objects = 3
last_key = None
wait_car = 0
gen = 15
camera_speed = 0
app = Ursina()
list_of_roads = []
list_of_cars = []
list_of_tree = []

playerX = Entity(model='models/player/chicken/chiken.glb', scale=(.2, .2, .2), position=(1.7, -0.5, -8.5), collider='box')
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
        xmodel = Entity(model='models/ground/grass/grass.glb', scale=(.3, .3, .3), position=(2, -1, z))

class Road():
    def __init__(self, z):
        xmodel = Entity(model='models/road/defolte/road.glb', scale=(.3, .3, .3), position=(2, -1, z))

class Car():
    def __init__(self, z, color):
        if color == 'red':
            self.xmodel = Entity(model='models/car/defolte_red/car_red.glb', scale=(.3, .3, .3), position=(-10, -0.9, z+1), collider='box')
            self.xmodel.rotation_y = 180
class Tree():
    def __init__(self, z, type, x):
        if type == '2':
            self.xmodel = Entity(model='models/tree/defolte/tree2/tree2.glb', scale=(.2, .2, .2), position=(x-0.4, -0.9, z+0.4), collider='box')
            self.xmodel.rotation_y = 180

#models and others

Acar = Actor("models/car/defolte_red/car_red.glb")
Acar.reparentTo(player)

#funcs

def generation():
    global gen, camera, objects
    if random.randint(0, 2) != 0:
        Road(gen)
        list_of_roads.append(gen)
        objects += 1
    else:
        Grass(gen)
        Tree(gen, '2', random.randint(-3, 6))
        Tree(gen, '2', random.randint(-3, 6))
        Tree(gen, '2', random.randint(-3, 6))
        objects += 4
    gen += 1

def movecamera():
    global camera_speed
    noun_x = playerX.z - (camera.z + 15)
    noun_x /= 50
    camera_speed = noun_x

    if camera_speed > 0:
        camera.z += camera_speed

for i in range(5, 20):
    Grass(-i)
for i in range(-4, 15):
    if random.randint(0, 1) == 0:
        Road(i)
        objects += 1
    else:
        Grass(i)
        objects += 1

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


def update():
    global test_cube, wait_car, objects
    movecamera()
    camera.z += 0.01
    if playerX.z - camera.z < 10:
        sys.exit()
    wait_car += 1
    if wait_car % 20 == 0:
        for i in list_of_roads:
            if random.randint(0, 9) == 0:
                q = Car(i, 'red')
                objects += 1
                list_of_cars.append(q)
            else:
                pass
        for i in list_of_roads:
            if playerX.z - i > 10:
                list_of_roads.remove(i)
    if wait_car % 300:
        for i in list_of_cars:
            i.xmodel.x += 0.1
    if str(playerX.intersects().entities).find("model='models/car/defolte_red/car_red'") != -1:
        print('пересечение с машиной')
    if str(playerX.intersects().entities).find("model='models/tree/defolte/tree2/tree2'") != -1:
        print('пересечение с деревом')
        if last_key == 'w': playerX.z -= 1
        if last_key == 's': playerX.z += 1
        if last_key == 'a': playerX.x += 1
        if last_key == 'd': playerX.x -= 1
    # print(distance(playerX, player))
    print(objects)



app.run()