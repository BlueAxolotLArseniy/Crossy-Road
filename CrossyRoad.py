from ursina import *
import random
from direct.actor.Actor import Actor

gen = 15
camera_speed = 0
app = Ursina()
playerX = Entity(scale=(.2, .2, .2), position=(2, -0.9, -8.5))
playerX.rotation_y = 180
player = Entity(scale=(.3, .3, .3))
test_cube = Entity(model='cube', position=(-2, 0, 0))

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
            xmodel = Entity(scale=(.3, .3, .3), position=(-10, -1, z))
            Xgrass = Actor('models/road/defolte/road.glb')
            Xgrass.reparentTo(xmodel)

Acar = Actor("models/car/defolte_red/car_red.glb")
Acar.reparentTo(player)
Aplayer = Actor('models/player/chicken/chiken.glb')
Aplayer.reparentTo(playerX)

camera.rotation_x = 40
camera.rotation_y = -20
camera.y = 14
camera.x = 9

def generation():
    global gen, camera
    if random.randint(0, 2) != 0:
        Road(gen)
    else:
        Grass(gen)
    gen += 1
    print('move')

def movecamera():
    noun_x = playerX.z - (camera.z + 11.5)
    noun_x /= 2
    camera_speed = noun_x / 50
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


def update():
    movecamera()

app.run()