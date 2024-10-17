from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import os

os.system('cls')

app=Ursina()

W=True #wall
_=False #none
P='player' #player
E='exit' #exit

class Player(FirstPersonController):
    def __init__(self):
        super().__init__(
            model='none', #lemon_1k.fbx\lemon_1k.fbx
            #color=color.white,
            #position=(0,5,0),
            scale=1,
            collider='mesh',
            texture='white_cube',
            gravity=1,
            jump_height=0
        )
    def input(self, key):
        if held_keys['shift']:
            self.speed=15
        else:
            self.speed=5

class Exit(Entity):
    def __init__(self,i,j):
        super().__init__(
            model='cube',
            color=color.red,
            position=(i*5,-1,j*5),
            scale=(6,25,6),
            collider='box',
            texture='white_cube'
        )

        self.player=player
        self.text=Text(
            text='gg lol',
            color=color.green,
            origin=(0,0),
            scale=9,
            visible=False
        )

    def clear(self):
        dis=(self.player.position-self.position).length()
        if dis<4:
            self.player.enabled=False
            self.text.visible=True

    def update(self):
        self.clear()
    
def input(key):
    if key=='escape':
        app.quit()

player=Player()
#EditorCamera()

MAP=[
    [W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W],
    [W,W,W,W,W,W,W,W,_,_,W,_,W,W,W,W,W,W],
    [W,W,W,W,_,W,W,W,_,W,_,_,W,W,W,W,W,W],
    [W,W,W,_,_,W,_,_,_,W,W,_,W,W,W,_,W,W],
    [W,W,W,W,_,_,_,W,_,_,_,_,_,_,W,_,W,W],
    [W,W,_,W,W,_,W,W,_,W,W,W,W,_,W,_,_,W],
    [W,_,_,_,_,_,_,_,_,_,_,W,W,_,W,_,W,W],
    [W,_,W,W,W,W,_,_,_,_,_,_,_,_,W,_,W,W],
    [W,W,W,W,_,_,_,_,_,P,_,W,_,W,W,_,W,W],
    [W,W,W,_,_,W,W,_,_,_,_,_,_,_,_,_,_,W],
    [W,W,_,_,W,W,W,_,_,_,_,_,_,W,W,W,_,W],
    [W,W,_,W,W,W,W,W,_,W,W,W,W,_,W,W,_,W],
    [W,W,_,W,W,_,_,_,_,_,W,W,W,_,W,W,_,W],
    [W,W,_,W,W,_,W,W,W,_,_,_,_,_,W,W,_,W],
    [W,W,_,_,_,_,W,W,W,W,W,_,W,W,W,W,_,W],
    [W,W,W,W,W,W,W,_,_,_,_,_,W,W,_,_,_,W],
    [W,W,W,W,W,W,W,_,W,W,W,W,W,_,_,W,W,W],
    [W,W,W,W,W,W,W,E,W,W,W,W,W,W,W,W,W,W]
]

for i in range(len(MAP)):
    for j in range(len(MAP[i])):
        if MAP[i][j]:
            if MAP[i][j]=='player':
                player.position=(i*5,5,j*5)
                continue
            if MAP[i][j]=='exit':
                exitdoor=Exit(i,j)
                continue
            wall=Entity(
                model='cube',
                color=color.black,
                position=(i*5,-1,j*5),
                scale=(5,25,5),
                collider='box',
            )
            
plane=Entity(
    model='Plane',
    color=color.red,
    scale=(500,1,500),
    position=(0,-2,0),
    collider='mesh',
    texture='none'
)
ciling=Entity(
    model='Plane',
    color=color.black,
    scale=(500,1,500),
    position=(0,25,0),
    collider='mesh',
    rotation=(0,0,180)
)

app.run()