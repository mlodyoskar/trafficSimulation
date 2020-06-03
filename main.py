import pygame
import numpy as np

RED = (255, 0, 0)
GREEN = (0, 255, 0)

WIDTH = 800
HEIGHT = 600
SPAWN_POINT1 = (WIDTH / 2 - 60, 20)
SPAWN_POINT2 = (WIDTH - 60, HEIGHT/2 - 40)
SPAWN_POINT3 = (WIDTH / 2 + 40, HEIGHT - 60)
SPAWN_POINT4 = (60, HEIGHT / 2 + 40)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Traffic")


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


class Car:

    def __init__(self, pos):
        self.width = 30
        self.height = 50
        self.pos = np.array(pos, dtype=np.float64)
        self.vel = [0, 0]

    def draw(self, screen):
        pygame.draw.rect(screen, RED, (self.pos[0], self.pos[1], self.width, self.height))

    def update(self):
        self.pos += self.vel


class Light:

    def __init__(self, x, y, state):
        self.width = 20
        self.height = 50
        self.x = x
        self.y = y
        self.currentState = state

    def draw(self, screen):
        if self.currentState:
            pygame.draw.rect(screen, GREEN, (self.x, self.y, self.width, self.height))
        else:
            pygame.draw.rect(screen, RED, (self.x, self.y, self.width, self.height))

    def lightsOff(self):
        self.currentState = False

    def lightsOn(self):
        self.currentState = True


class Timer:

    def __init__(self):
        self._start = 0

    def start(self):
        self._start = pygame.time.get_ticks()

    def current(self):
        return (pygame.time.get_ticks() - self._start) / 1000


pygame.init()

background = Background('images/background.png', [0, 0])

car1 = Car(SPAWN_POINT1)

run = True
while run:
    screen.fill((0, 0, 0))
    screen.blit(background.image, background.rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    car1.draw(screen)
    car1.update()
    print(car1.pos, car1.vel)
    pygame.display.update()
pygame.quit()
