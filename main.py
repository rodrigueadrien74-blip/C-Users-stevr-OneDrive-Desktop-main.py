from ursina import *
from ursina.prefabs.platformer_controller_2d import PlatformerController2d

app = Ursina()

Sky()
cube1 = PlatformerController2d(scale=1)
cube2 = Entity(
    model='quad',
    color=color.hex("#00FFD5"),
    position=(-6, 0),
    collider='box'
)

music = Audio(
    'Dash.mp3',
    loop=True,
    autoplay=True
)

roche = Entity(
    model='quad',
    color=color.gray,
    scale=(20, 3),
    position=(0, -3),
    collider='box'
)

a = Entity(
        model='quad',
        color=color.red,
        position=(7, 0),
        collider='box'
)

b = Entity(
    model='quad',
    color=color.orange,
    position=(4, 0),
    collider='box'
)

c = Entity(
    model='quad',
    color=color.yellow,
    position=(3, 0),
    collider='box'
)

d = Entity(
    model='quad',
    color=color.green,
    position=(2, 0),
    collider='box'
)

e = Entity(
    model='quad',
    color=color.blue,
    position=(-7, 0),
    collider='box'
)

f = Entity(
    model='quad',
    color=color.pink,
    position=(-4, 0),
    collider='box'
)

g = Entity(
    model='quad',
    color=color.gray,
    position=(-3, 0),
    collider='box'
)

h = Entity(
    model='quad',
    color=color.black,
    position=(-2, 0),
    collider='box'
)

def move_cube2():
    if held_keys['up arrow']:
        cube2.y += 8 * time.dt
    if held_keys['down arrow']:
        cube2.y -= 8 * time.dt
    if held_keys['left arrow']:
        cube2.x -= 8 * time.dt
    if held_keys['right arrow']:
        cube2.x += 8 * time.dt

def update():
    move_cube2()

app.run()
