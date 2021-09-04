from copy import deepcopy
from time import sleep
import pygame
import sys
import Constants



def nextFrame(grid):
    grid2 = deepcopy(grid)
    hm = 0
    for i in range(Constants.cols):
        for j in range(Constants.rows):
            count = 0
            try:
                if grid[j-1][i]:
                    count += 1
            except IndexError:
                pass
            try:
                if grid[j+1][i]:
                    count += 1
            except IndexError:
                pass
            try:
                if grid[j][i-1]:
                    count += 1
            except IndexError:
                pass
            try:
                if grid[j][i+1]:
                    count += 1
            except IndexError:
                pass
            try:
                if grid[j-1][i-1]:
                    count += 1
            except IndexError:
                pass
            try:
                if grid[j-1][i+1]:
                    count += 1
            except IndexError:
                pass
            try:
                if grid[j+1][i-1]:
                    count += 1
            except IndexError:
                pass
            try:
                if grid[j+1][i+1]:
                    count += 1
            except IndexError:
                pass
            if grid[j][i]:
                if count in [2, 3]:
                    grid2[j][i] = True
                else:
                    grid2[j][i] = False
            else:
                if count == 3:
                    grid2[j][i] = True
                else:
                    grid2[j][i] = False

    return grid2


screen = pygame.display.set_mode((Constants.screen_width, Constants.screen_height))
pygame.font.init()
grid = [[False for i in range(Constants.cols)] for h in range(Constants.rows)]

space_pressed = False

while True:
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    screen.fill(Constants.bg_color)
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((0, 0), (Constants.screen_width, Constants.screen_height*.1)))
    if pygame.mouse.get_pressed(3)[0]:
        grid[int(pygame.mouse.get_pos()[1]-.1*Constants.screen_height)//Constants.cell_width][pygame.mouse.get_pos()[0]//Constants.cell_width] = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                space_pressed = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                space_pressed = False
    if space_pressed:
        grid = nextFrame(grid)
    for i in range(Constants.cols):
        for j in range(Constants.rows):
            if grid[j][i]:
                actual_color = (255, 255, 255)
            else:
                actual_color = (100, 0, 0)
            pygame.draw.rect(screen, actual_color, pygame.Rect((i * Constants.cell_width + 1, Constants.screen_height*.1 + j * Constants.cell_width + 1), (Constants.cell_width - 2, Constants.cell_width - 2)))
    hm = 0
    for i in range(Constants.cols):
        for j in range(Constants.rows):
            if grid[j][i]:
                hm += 1
    textsurface = myfont.render(f'Occupied {hm}/{Constants.rows * Constants.cols}', False, (255, 255, 255))
    screen.blit(textsurface, (Constants.screen_width - 280, 15))
    textsurface = myfont.render('Use Mouse and Spacebar', False, (255, 255, 255))
    screen.blit(textsurface, (0, 15))
    myfont = pygame.font.SysFont('Comic Sans MS', 50)
    textsurface = myfont.render('Game of Life', False, (255, 255, 255))
    screen.blit(textsurface, (Constants.screen_width//2 - 150, -5))
    myfont = pygame.font.SysFont('Comic Sans MS', 20)
    textsurface = myfont.render('by John Conway', False, (255, 255, 255))
    screen.blit(textsurface, (Constants.screen_width//2 - 80, 50))
    pygame.display.flip()
    if space_pressed:
        sleep(0.2)
