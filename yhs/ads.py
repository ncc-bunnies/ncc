from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app=Ursina(
    borderless=False
)

class Player(FirstPersonController):
    def __init__(self):
        super().__init__(
            position=(0,11,0),
            scale=1,
            model='cube',
            collider='box',
            texture='white_cube',
            gravity=1.7,
            jump_height=13,
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
    scale=(50000,1,50000),
    position=0,
    collider='box',
)

wall=Entity(
    model='cube',
    color=color.black,
    position=10,
    scale=(5,25,5),
)

aa=Button(
    text='32',
    origin=(1,0)
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

app.run()