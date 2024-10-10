import sys
import pygame as pg
import math
import time

pg.init()
size = width, height = (720, 480)
screen = pg.display.set_mode(size)
screen.fill("skyblue")

car = pg.Rect(40, 80, 5, 10)

pg.display.init()
screen.fill("skyblue")
pg.draw.rect(car)
pg.display.flip()

time.sleep(5)

pg.display.quit()
SystemExit()
