import pygame
from pygame.locals import *

#Colors
red = (255, 51, 51)

#Images

#Classes

playerPaddles =[]

class playerPaddle:

    def __init__(self, color, x, y, size, side, speed):
        self.color = color
        self.x = x
        self.y = y
        self.size = size
        self.side = side
        self.speed = speed

    def draw(self, win):
        self.rect=pygame.draw.rect(win, self.color, ((self.x, self.y), self.size))

    def move(self, win):
        keys = pygame.key.get_pressed() 
        if keys[pygame.K_UP]:
            self.y -= self.speed
def PaddleInit():
    playerPaddles.append(playerPaddle(red, 0, 250, (25, 150), "Left", 5))
    playerPaddles.append(playerPaddle(red, 875, 250, (25, 150), "Right", 5))

def Funcs(win):
    for playerPaddle in playerPaddles:
        playerPaddle.draw(win)
        playerPaddle.move(win)
             
