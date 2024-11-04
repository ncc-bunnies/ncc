from ursina import * #ursina의 모든 개체
from ursina.prefabs.first_person_controller import FirstPersonController


#aaaa

app=Ursina()

__ = False


class Player(FirstPersonController):
    def __init__(self):
        super().__init__( 
            model = 'cube',
            Collider = 'mesh',
            color = color.blue,
            speed = 30,
            scale = 5
        )

class Exit(Entity):
    def __init__(self,i,j):
        super().__init__(
            model = 'cube',
            color = color.black90,
            scale = (5,100,5),
            position = (i*5,0,j*5),
            collider = 'box'
            )
        
        self.player = player
        self.text = Text(
            text = "GG!!",
            scale = 2,
            origin = (0,0),
            visible = False
        )

    def update(self):
        self.clear()

    def clear(self):
        dis = (self.player.position -self.position).length()
        print(dis)
        if dis < 3 :
            self.player.enable= False
            self.text.visible = True
     
def input(key):
    if key == 'escape':
        app.quit()

player = Player()

EditorCamera()


zk = Entity(
     model = 'ee/covered_car_4k.fbx',
     texture = 'eee/카.jpg',
     scale = (0.01) ,
     collider= 'mesh'

)


ground = Entity(
    model = 'plane',
    #color = color.black,
    position = (0,-10,0),
    scale = (2000,1,2000),
    collider= 'mesh', #mash는 물체의 충돌 설정
    texture = 'painted_brick_diff_4k.jpg'

)


MAP = [
    [10,__,'p',10,15,40,30,60,30,20,40,10,49,28,40,58,29,58,18,14,68,63,58,23],
    [10,__,10,10,__,__,__,60,30,20,40,__,__,28,40,58,__,__,__,__,68,__,__,'e'],
    [10,__,__,__,__,40,__,__,__,__,__,__,49,28,40,__,__,58,18,__,68,__,58,23],
    [10,__,10,10,__,40,30,60,__,20,40,10,49,__,__,__,29,__,__,__,68,__,__,23],
    [10,__,10,__,__,40,__,__,__,20,40,10,49,__,40,__,29,__,18,14,__,63,__,23],
    [10,__,10,10,__,__,__,60,__,20,40,__,__,__,40,__,__,58,18,__,__,__,__,23],
    [10,__,10,10,__,40,30,__,__,20,40,__,49,28,40,58,__,__,18,__,68,__,58,23],
    [10,'z',10,10,__,__,__,__,30,__,__,__,49,__,__,__,29,__,__,__,68,63,58,23],
    [10,__,10,10,15,40,30,60,__,__,40,10,49,__,40,__,29,58,18,__,68,__,__,23],
    [10,__,10,10,15,40,30,60,__,20,40,__,__,__,40,__,__,__,18,__,68,63,__,23],
    [10,__,__,__,__,__,__,__,__,__,__,__,49,28,40,58,29,__,18,__,__,__,__,23],
    [10,11,10,__,15,40,30,60,__,20,40,__,__,28,40,58,29,__,__,14,__,63,58,23],
    [10,11,__,__,15,40,30,__,__,__,40,10,__,28,__,__,__,58,__,14,__,__,__,23],
    [10,11,__,10,15,__,__,60,30,__,40,10,__,__,__,58,__,58,__,14,68,63,__,23],
    [10,11,__,__,__,40,__,60,30,__,__,10,49,28,40,58,__,__,__,14,__,__,__,23],
    [10,11,10,10,__,__,__,60,30,20,__,__,__,__,__,__,__,58,18,__,__,63,58,23],
    [10,11,10,10,15,40,30,60,30,20,40,10,49,28,40,58,29,58,18,14,68,63,58,23]
    
]
 

for i in range( len(MAP) ):
    for j in range( len(MAP[i]) ):

            if MAP[i][j]:
                if MAP[i][j]=='p':
                    player.position = (i*5,0,j*5)
                    continue

                if  MAP[i][j] == 'e':
                    esifdoor = Exit(i,j)
                    continue

                if MAP[i][j]=='z':
                    zk.position = (i*6,-9,j*5)
                    continue

                wall = Entity(
                    model ='cube',
                    #color = color.red,
                    scale = (8,80,8),
                    position = (8*i,-8,8*j),
                    collider = 'box',
                    texture = 'painted_brick_disp_4k.png'
                    )
            
                 




app.run()