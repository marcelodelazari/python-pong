import pygame
import time

from Ball import Ball
from Controller import Controller
from Drawer import Drawer
from Racket import Racket

pygame.init()


def gameplay():
    controller.gameplay()


# Screen Setup
WIDTH = 480
HEIGHT = 360
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("PyPong")

# Game variables
racket_height = HEIGHT // 6
racket_width = WIDTH // 30

#  Instanciate classes
player_racket = Racket((
    WIDTH - racket_width*2, HEIGHT // 2 - racket_height // 2),
    racket_width, racket_height)

bot_racket = Racket((
    racket_width, HEIGHT // 2 - racket_height // 2),
    racket_width, racket_height)

ball = Ball((WIDTH // 2 - racket_width // 2, HEIGHT // 2 - racket_width // 2),
            racket_width, WIDTH // 80)

controller = Controller(WIDTH, HEIGHT, player_racket, bot_racket, ball)

drawer = Drawer(screen, WIDTH, HEIGHT, controller,
                player_racket, bot_racket, ball)

# Game loop
running = True
clock = pygame.time.Clock()
framerate = 80
controller.release_ball(time.time())

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            pass

    gameplay()

    drawer.draw()
    clock.tick(framerate)
