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
        pygame.time.set_timer(USEREVENT +1, 800)
        while self.gaming:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    while i < 8:
                        sense.set_pixel(i, 7, (0,0,255))
                        time.sleep(0.1)
                        sense.set_pixel(i, 7, (0,0,0))
                        time.sleep(0.05)
                        i = i+ 1
                    

if __name__ == "__main__":
    try:
        game = stack()
        game.startGame()
    except KeyboardInterrupt:
        sense.clear()
