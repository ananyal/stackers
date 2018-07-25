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
        row = 7
        c = 0
        pygame.time.set_timer(USEREVENT +1, 700)
        while self.gaming:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    sense.set_pixel((i-1), row, (255,0,255))
                    if row <= 6:
                        if c != i:
                            sense.show_message('Game Over', 0.05, text_colour=(255,255,255), back_colour = (0,0,0))
                            self.gaming = False
                        else:
                            if row == 0:
                                sense.show_message('You Win!', 0.05, text_colour=(0,255,255), back_colour = (0,0,0))
                                self.gaming = False
                            else:
                                row = row - 1 
                                i = 0 
                    else:
                        c= i 
                        row = row - 1 
                        i = 0 
     
            else:       
                sense.set_pixel(i, row, (0,0,255))
                time.sleep(0.2)
                sense.set_pixel(i, row, (0,0,0))
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
