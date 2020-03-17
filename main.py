import pygame
from start import start
s = -1
# s = -1: Starting Screen
# s = 0: Level Menu
# s = [insert positive int x]: Level x

gameRunning = True
while gameRunning:
    if s == -1:
        s = start(1000, s)
    else:
        break
