import pygame as pg
import constants as c

pg.init()

clock = pg.time.Clock()

screen = pg.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))

run = True
while run:

    clock.tick(c.FPS)

    for event in pg.event.get():

        if event.type == pg.QUIT:
            run = False

pg.quit()