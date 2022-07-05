import Maze as maze
import numpy as np
import pygame
def main():
    mazesidelength = 200
    displaysize = 1000

    a = maze.Maze()
    a.GenerateMaze(mazesidelength)

    background_colour = (255, 255, 255)
    display = pygame.display.set_mode((displaysize + 2,displaysize + 2))
    pygame.display.set_caption('Maze')
    display.fill(background_colour)
    surf = pygame.surfarray.make_surface(a.maze)
    a = pygame.transform.scale(surf, (displaysize, displaysize))
    display.blit(a,(0,0))
    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False



if __name__ == "__main__":
    main()