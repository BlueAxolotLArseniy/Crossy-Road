#all import

from ursina import *
import random
from direct.actor.Actor import Actor
import sys

#start

wait_car = 0
gen = 15
camera_speed = 0
app = Ursina()
list_of_roads = []

playerX = Entity(scale=(.2, .2, .2), position=(2, -0.9, -8.5))
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
        xmodel = Entity(scale=(.3, .3, .3), position=(2, -1, z))
        Xgrass = Actor('models/ground/grass/grass.glb')
        Xgrass.reparentTo(xmodel)

class Road():
    def __init__(self, z):
        xmodel = Entity(scale=(.3, .3, .3), position=(2, -1, z))
        Xgrass = Actor('models/road/defolte/road.glb')
        Xgrass.reparentTo(xmodel)

class Car():
    def __init__(self, z, color):
        if color == 'red':
            xmodel = Entity(scale=(.3, .3, .3), position=(-10, -0.9, z))
            Xgrass = Actor('models/car/defolte_red/car_red.glb')
            Xgrass.reparentTo(xmodel)

#models and others

Acar = Actor("models/car/defolte_red/car_red.glb")
Acar.reparentTo(player)
Aplayer = Actor('models/player/chicken/chiken.glb')
Aplayer.reparentTo(playerX)

#funcs

def generation():
    global gen, camera
    if random.randint(0, 2) != 0:
        Road(gen)
        list_of_roads.append(gen)
    else:
        Grass(gen)
    gen += 1
    print('move')

def movecamera():
    global camera_speed
    noun_x = playerX.z - (camera.z + 11.5)
    noun_x /= 50
    camera_speed = noun_x

    if camera_speed > 0:
        camera.z += camera_speed

for i in range(5, 20):
    Grass(-i)
for i in range(-4, 15):
    if random.randint(0, 1) == 0:
        Road(i)
    else:
        Grass(i)

def input(key):
    if key == 'left mouse down':
        generation()
        playerX.z += 1
    if key == 's':
        generation()
        playerX.z -= 1
    if key == 'w':
        generation()
        playerX.z += 1


def update():
    global test_cube, wait_car
    movecamera()
    camera.z += 0.01
    if playerX.z - camera.z < 10:
        sys.exit()
    wait_car += 1
    if wait_car % 100 == 0:
        for i in list_of_roads:
            Car(i, 'red')
            print('awd')

app.run()