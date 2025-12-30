import asyncio
import pygame
import sys
import os
from pygame.locals import *



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
#Big_font = pygame.font.Font("freesansbold.ttf", 60)

#images
Play1PlayerDim = pygame.image.load("sprites/Play1Player.png")
Play2PlayerDim = pygame.image.load("sprites/Play2Player.png")
SettingsDim = pygame.image.load("sprites/Settings.png")
QuitDim = pygame.image.load("sprites/Quit.png")

Play1PlayerHover = pygame.image.load("sprites/Play1PlayerHover.png")
Play2PlayerHover = pygame.image.load("sprites/Play2PlayerHover.png")
SettingsHover = pygame.image.load("sprites/SettingsHover.png")
QuitHover = pygame.image.load("sprites/QuitHover.png")

#Vars

#Lists
DimButtons = [
Play1PlayerDim,
Play2PlayerDim,
SettingsDim,
QuitDim 
             ]

HoverButtons = [
Play1PlayerHover,
Play2PlayerHover,
SettingsHover,
QuitHover
               ]

#Classes

#-MenuButtons
buttons = []

def SinglePlayerInit(Game_State):
    Game_State["Unstarted"] = False
    Game_State["OnePlayer"] = True
    print(Game_State)

def TwoPlayerInit(Game_State):
    Game_State["Unstarted"] = False
    Game_State["TwoPlayer"] = True
    print(Game_State)

def SettingsInit(Game_State):
    Game_State["Unstarted"] = False
    Game_State["Settings"] = True
    print(Game_State)

def QuitInit(Game_State):
    sys.exit()
    
ButtonActions = [
    SinglePlayerInit,
    TwoPlayerInit,
    SettingsInit,
    QuitInit
                ]           


class button:

    def __init__(self, color, pos, size, clickfunction, Game_State):
        self.color = color
        self.pos = pos
        self.size = size
        self.clickfunction = clickfunction
        self.Game_State = Game_State
            

    def draw(self, win):
        self.rect=pygame.draw.rect(win, self.color, (self.pos, self.size))
        win.blit(DimButtons[self.clickfunction], (self.pos))
        
    def clicked(self, win):
        mousePos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mousePos):
            win.blit(HoverButtons[self.clickfunction], (self.pos))
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                ButtonActions[self.clickfunction](self.Game_State)
                
            

def ButtonInit(Game_State):
    ButtonNumber = -1
    buttony = 100
    for count in range(4):
        ButtonNumber += 1
        buttons.append(button(red, (325, buttony), (250, 50), ButtonNumber,Game_State))
        buttony += 125
        
        
        
#Shapes

#main loop
    
def MenuFuncs(win, Game_State):
        for button in buttons:
            button.draw(win)
            button.clicked(win)       
            #win.blit(Play1PlayerDim, (100,100))
                        
        #sampleText = Big_font.render("SampleText!", True, back)
        #win.blit(sampleText, (100,100))
        
