from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import os

os.system('cls')

app=Ursina(
    title='',
    borderless=False,
    size=(1000,750)
)

W=True #Block
_=False #none
P='player' #player
E='exit' #exit

class Player(FirstPersonController):
    def __init__(self):
        super().__init__(
            #model='none', #lemon_1k.fbx\lemon_1k.fbx
            #color=color.white,
            #position=(0,5,0),
            scale=1,
            collider='box',
            texture='white_cube',
            gravity=1,
            jump_height=0
        )
    def input(self, key):
        if held_keys['shift']:
            self.speed=9
        else:
            self.speed=5

class Exit(Entity):
    def __init__(self,i,j):
        super().__init__(
            model='cube',
            color=color.red,
            position=(i*5,-1,j*5),
            scale=(5,25,5),
            collider='box',
            #texture=''
        )

        self.player=player
        self.text=Text(
            text='gg lol',
            color=color.green,
            origin=(0,0),
            scale=9,
            visible=False
        )

    def sound(self):
        dis=(self.player.position-self.position).length()
        a=Audio(
            'kkk',
            volume=256/(dis**2),
            loop=True
        )
    
    def clear(self):
        if self.intersects(self.player):
            self.player.enabled=False
            self.text.visible=True
        

    def update(self):
        self.sound()
        self.clear()
    
def input(key):
    if key=='escape':
        app.quit()

player=Player()
#EditorCamera()

MAP=[
    [W,W,W],
    [W,P,W],
    [W,_,W],
    [W,_,W],
    [W,_,W],
    [W,_,W],
    [W,_,W],
    [W,_,W],
    [W,_,W],
    [W,_,W],
    [W,_,W],
    [W,_,W],
    [W,_,W,W,W,W,W,W,W,W,W,W,W],
    [W,_,_,_,_,_,_,_,_,_,_,_,E],
    [W,W,W,W,W,W,W,W,W,W,W,W,W]
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
    color=color.dark_gray,
    scale=(500,1,500),
    position=(0,-2,0),
    collider='mesh',
    #texture=''
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