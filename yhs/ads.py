from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app=Ursina(
    borderless=False
)

class Player(FirstPersonController):
    def __init__(self):
        super().__init__(
            position=(0,1,0),
            scale=1,
            model='cube',
            collider='box',
            texture='white_cube',
            gravity=1.7,
            jump_height=6,
            visible_self=True
        )
        
    def input(self, key):
        super().input(key)
        if held_keys['shift']:
            self.speed=11
        else:
            self.speed=5

player=Player()

plane=Entity(
    model='Plane',
    color=color.green,
    scale=(50000,-15,50000),
    position=0,
    collider='box',
)

wall=Entity(
    model='cube',
    color=color.red,
    position=10,
    scale=(5,25,5),
)

aa=Button(
    text='32',
    color=color.black50,
    origin=(-1.25,1.45),
    scale=(0.5,0.25)
)

class Voxel(Button):
    def __init__(self, position=(0,0,0)):
        super().__init__(parent=scene,
            position=position,
            model='cube',
            origin_y=.5,
            texture='white_cube',
            color=color.hsv(0, 0, random.uniform(.9, 1.0)),
            highlight_color=color.lime,
        )

def input(key):
    if key=='escape':
        if player.enabled:
            player.enabled=False
        else:
            player.enabled=True
    if key=='f11':
        if window.fullscreen:
            not window.fullscreen
        else:
            window.fullscreen

voxel=Voxel(position=(1,3,0))

app.run()