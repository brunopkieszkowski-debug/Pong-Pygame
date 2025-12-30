import pygame
from pygame.locals import *
import random

#Colors
red = (255, 51, 51)
back = (40,19,13)

#images
BallImg = pygame.image.load("sprites/ball.png")
RotateAngle = 1

#Classes
balls = []

class ball:

    def __init__(self, color, x, y, size):
        self.color = color
        self.x = x
        self.y = y
        self.size = size

    def draw(self, win):
        
        self.rect=pygame.draw.ellipse(win, self.color, ((self.x, self.y), self.size))
        
        

    def move(self, win):
        self.x += 1

    def rotate(self, win):
        global RotateAngle
        RotatingBall = pygame.transform.rotate(BallImg, RotateAngle)
        BallBox = RotatingBall.get_rect(center=((self.x+11.25), (self.y+12)))
        win.blit(RotatingBall, BallBox.topleft)
        RotateAngle += 5

def BallInit():
    balls.append(ball(red, 100,100, (25, 25)))


def Funcs(win):
    for ball in balls:
        ball.draw(win)
        ball.move(win)
        ball.rotate(win)


