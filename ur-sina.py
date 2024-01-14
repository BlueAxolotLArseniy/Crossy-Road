from ursina import *
from direct.actor.Actor import Actor

app = Ursina()

# cube = Entity(model='untitled', color=hsv(300,1,1), scale=2, collider='box')

# def spin():
#     cube.animate('rotation_y', cube.rotation_y+360, duration=2, curve=curve.in_out_expo)

# cube.on_click = spin
EditorCamera()  # add camera controls for orbiting and moving the camera

entity = Entity(texture='white_cube')
actor = Actor("models/car/defolte_red/car_red.glb")
actor.reparentTo(entity)
# print('AAAAA', actor)
# print('AAAAA', actor.getAnimNames())
# actor.loop('Арматура.003Action.001')

def update():
    entity.x -= 0.1

app.run()