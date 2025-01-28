#main
import pygame
import random

pygame.init()

WIDTH = 450
HEIGHT = 800
timer = pygame.time.Clock()
fps = 60
screen = pygame.display.set_mode([WIDTH,HEIGHT])
pygame.display.set_caption('Mastermind!')
font = pygame.font.Font('freesanabold.ttf', 18)
# game variables
background = int(.125*255), int(.165*255), int(.267*255)


run = True
while run:
    timer.tick(fps)
    screen.fill(background)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
pygame.quit()
