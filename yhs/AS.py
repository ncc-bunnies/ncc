from ursina import *
app=Ursina()
b = Button(scale=(.5, .25), text='zzz')
b.on_mouse_enter = Func(setattr, b, 'text', 'Hi, friend :D')
b.on_mouse_exit = Func(setattr, b, 'text', '''No! Don't leave me ;-;''')
app.run()