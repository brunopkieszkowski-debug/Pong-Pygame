import asyncio
import pygame
import sys
import os
from pygame.locals import *
import menu
from menu import *
import BallCode
from BallCode import *
import PlayerPaddles
from PlayerPaddles import *

async def main():
    global Unstarted
    pygame.init()
#Colors
    back = (40,19,13)
    red = (255, 51, 51)
    white = (255,255,255)
    orange = (255,102,51)
    yellow = (255,192,51)
    green = (151,255,51)
    teal = (51,255,137)
    background = (7,9,38)

#Fonts
    Big_font = pygame.font.Font("freesansbold.ttf", 60)

#images

#Vars
    GameTitle = "MainMenu"
#ListsAndDictionaries
    Game_State = {
        "Unstarted": True,
        "OnePlayer": False,
        "TwoPlayer": False,
        "Settings": False
                 }

#Win
    clock = pygame.time.Clock()
    winw, winh = 900, 700
    win = pygame.display.set_mode((winw,winh))
    pygame.display.set_caption(GameTitle)

#Classes
    ButtonInit(Game_State)    
    BallCode.BallInit()
    PlayerPaddles.PaddleInit()
#Shapes

#main loop
    run = True
    while run:
        
        pygame.time.delay(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        win.fill(background)
        if Game_State["Unstarted"]:
            menu.MenuFuncs(win, Game_State)
        elif Game_State["OnePlayer"]:
            BallCode.Funcs(win)
            PlayerPaddles.Funcs(win)
        elif Game_State["TwoPlayer"]:
            BallCode.Funcs(win)
        #win.blit(Play1PlayerDim, (100,100))                
        #sampleText = Big_font.render("SampleText!", True, back)
        #win.blit(sampleText, (100,100))
        pygame.display.update()
        clock.tick(60)
        
        await asyncio.sleep(0)
    pygame.quit()
    sys.exit()

asyncio.run(main())
