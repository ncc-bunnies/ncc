from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
#from ursina.shaders.screenspace_shaders.fxaa import *
import os

os.system('cls')


app=Ursina(
    title='',
    icon='logo.ico',
    borderless=False,
    size=(1000,750)
)

#camera.shader=fxaa_shader

W=True #Wall
_=False #None
P='player' #Player
E='exit' #Exit
T='warp' #warp

tp_pos=[(150,0,5),(75,0,10)]
tp_max=2

class Player(FirstPersonController):
    def __init__(self,i,j):
        super().__init__(
            position=(i*5,5,j*5),
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

class TP(Entity):
    def __init__(self,i,j,tp_pos,tp_max):
        super().__init__(
            model='cube',
            color=color.red,
            position=(i*5,-1,j*5),
            scale=(5,25,5),
            collider='box'
        )
    
        self.player=player
        self.tp_pos=tp_pos

    def warp(self):
        global tp_max
        if self.intersects(self.player):
            tp_max-=1
            self.player.position=self.tp_pos[tp_max]
    
    def update(self):
        self.warp()

class Exit(Entity):
    def __init__(self,i,j):
        super().__init__(
            model='cube',
            color=color.red,
            position=(i*5,-1,j*5),
            scale=(5,25,5),
            collider='box'
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
        if tp_max==0:
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
        quit()
    if key=='f11':
        window.fullscreen=not window.fullscreen

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
    [W,_,_,_,_,_,_,_,_,_,_,_,T],
    [W,W,W,W,W,W,W,W,W,W,W,W,W],
    [W,_,_,_,W],
    [W,_,_,_,W],
    [W,_,_,_,W],
    [W,_,_,_,W],
    [W,_,_,_,W],
    [W,_,_,_,W],
    [W,_,_,_,W],
    [W,_,_,_,W],
    [W,_,_,_,W],
    [W,_,_,_,W],
    [W,_,_,_,W],
    [W,_,_,_,W],
    [W,W,_,W,W],
    [_,W,T,W,_],
    [W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W],
    [W,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,W],
    [W,W,W,W,W,W,W,W,W,W,_,W,W,W,W,W,W,W,W,W,W],
    [_,_,_,_,_,_,_,_,_,W,_,W],
    [_,_,_,_,_,_,_,_,_,W,_,W],
    [_,_,_,_,_,_,_,_,_,W,_,W],
    [_,_,_,_,_,_,_,_,_,W,_,W],
    [_,_,_,_,_,_,_,_,_,W,_,W],
    [_,_,_,_,_,_,_,_,_,W,_,W],
    [_,_,_,_,_,_,_,_,_,W,_,W],
    [_,_,_,_,_,_,_,_,W,_,_,W],
    [_,_,_,_,_,_,_,W,_,_,W],
    [_,_,_,_,_,_,W,_,_,W],
    [_,_,_,_,_,_,_,W,_,_,W],
    [_,_,_,_,_,_,_,_,W,_,_,W],
    [_,_,_,_,_,_,_,_,_,W,_,_,W],
    [_,_,_,_,_,_,_,_,_,_,W,_,_,W],
    [_,_,_,_,_,_,_,_,_,_,_,W,_,_,W],
    [_,_,_,_,_,_,_,_,_,_,W,_,_,W],
    [_,_,_,_,_,_,_,_,_,W,_,_,W],
    [_,_,_,_,_,_,_,_,_,W,_,W],
    [_,_,_,_,_,_,_,_,_,W,_,W],
    [_,_,_,_,_,_,_,_,_,W,_,W],
    [_,_,_,_,_,_,_,_,_,W,_,W],
    [_,_,_,_,_,_,_,_,_,W,_,W],
    [_,_,_,_,_,_,_,_,_,W,_,W],
    [_,_,_,_,_,_,_,_,_,W,E,W],
]

for i in range(len(MAP)):
    for j in range(len(MAP[i])):
        if MAP[i][j]:
            if MAP[i][j]=='player':
                player=Player(i,j)
                continue
            if MAP[i][j]=='exit':
                exit=Exit(i,j)
                continue
            if MAP[i][j]=="warp":
                tp=TP(i,j,tp_pos,tp_max)
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
    scale=(50000,1,500),
    position=(0,-2,0),
    collider='mesh',
    #texture=''
)

ceiling=Entity(
    model='Plane',
    color=color.black,
    scale=(50000,1,500),
    position=(0,25,0),
    collider='mesh',
    rotation=(0,0,180)
)

pos_print=Text(
    origin=(0,0)
)

def update():
    global ppos
    ppos=[int(oo) for oo in (player.position.x,player.position.y,player.position.z)]
    pos_print.text=ppos

app.run()