import pygame
import os
import tkinter

SCREEN_WIDTH = tkinter.Tk().winfo_screenwidth()
SCREEN_HEIGHT = tkinter.Tk().winfo_screenheight()

BACKGROUND_IMAGE = pygame.transform.smoothscale(pygame.image.load(os.path.join('images', 'background.jpeg')), (SCREEN_WIDTH, SCREEN_HEIGHT))
CARD_BACK_IMAGE = pygame.image.load(os.path.join('images', 'card-back.png'))

OPTION_BUTTON_SIZE = 60

pygame.font.init()
GAME_FONT = pygame.font.SysFont('comicsansms', 20)
OPTION_BUTTON_FONT = pygame.font.SysFont('comicsansms', 30, True)
