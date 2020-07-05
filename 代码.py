import sys
from random import randint
import pygame
from pygame.locals import *

pygame.init()
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("Flappy bird")

bird_1 = pygame.image.load("I:/Flappy Bird/bird.png")
ground = pygame.image.load("I:/Flappy Bird/ground.jpg")
ground_1 = pygame.image.load("I:/Flappy Bird/ground.jpg")
guanzi_shang = pygame.image.load("I:/Flappy Bird/guanzishang.png")
guanzi_xia = pygame.image.load("I:/Flappy Bird/guanzixia.png")
wel = pygame.image.load("I:/Flappy Bird/wel.png")
_0 = pygame.image.load("I:/Flappy Bird/0.png")
over = pygame.image.load("I:/Flappy Bird/over.png")
_1 = pygame.image.load("I:/Flappy Bird/1.png")
_2 = pygame.image.load("I:/Flappy Bird/2.png")
_3 = pygame.image.load("I:/Flappy Bird/3.png")
_4 = pygame.image.load("I:/Flappy Bird/4.png")
_5 = pygame.image.load("I:/Flappy Bird/5.png")
_6 = pygame.image.load("I:/Flappy Bird/6.png")
_7 = pygame.image.load("I:/Flappy Bird/7.png")
_8 = pygame.image.load("I:/Flappy Bird/8.png")
_9 = pygame.image.load("I:/Flappy Bird/9.png")
clock = pygame.time.Clock()
running=True
bird_y =400
guanzi_shang_x=450
guanzi_xia_x=450
guanzi_y=500
ground_x = 0
ground_1_x=800
move_bird_y=0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_UP:
                move_bird_y = -30
        elif event.type == KEYUP:
            move_bird_y = 0
    guanzi_shang_y = randint(-400, -25)
    guanzi_xia=guanzi_shang_y+600
    bird_y += move_bird_y
    clock.tick(40)
    bird_y+=5
    clock.tick(40)
    ground_x-=5
    ground_1_x -= 5
    guanzi_shang_x-=5
    guanzi_xia_x=guanzi_shang_x
    if bird_y<=0:
        bird_y=0
    if bird_y>=488:
        bird_y=488
    if guanzi_shang_x==-100:
        guanzi_y = randint(-400, -25)
        guanzi_shang_x=800
        guanzi_xia_x=guanzi_shang_x
    if ground_x==-800:
        ground_x=0
        ground_1_x=800        
    screen.blit(ground, (ground_x, 0))
    screen.blit(ground_1, (ground_1_x, 0))
    screen.blit(bird_1, (100, bird_y))
    screen.blit(guanzi_shang, (guanzi_shang_x, guanzi_y))
    screen.blit(guanzi_xia, [guanzi_xia_x, guanzi_y])
    pygame.display.update()
