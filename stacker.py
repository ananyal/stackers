from sense_hat import SenseHat
from pygame.locals import *
import pygame
import time


sense = SenseHat()
sense.clear()

class stack():
    def __init__(self) :
        pygame.init()
        pygame.display.set_mode((640,480))
        self.gaming = True

    def startGame(self):
        i = 0
        pygame.time.set_timer(USEREVENT +1, 250)
        while self.gaming:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    self.gaming = False              
                sense.set_pixel(i, 7, (0,0,255))
                time.sleep(0.2)
                sense.set_pixel(i, 7, (0,0,0))
                time.sleep(0.01)
                i = i+ 1
                if i == 8:
                    i = 0
                       

if __name__ == "__main__":
    try:
        game = stack()
        game.startGame()
    except KeyboardInterrupt:
        sense.clear()
