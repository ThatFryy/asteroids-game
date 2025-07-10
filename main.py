from constants import *
import pygame
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    fps = pygame.time.Clock()
    dt = 0
    
    # Player spawns in the center of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    player.draw(screen)
    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Makes sure we can quit
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Draws a black screen    
        screen.fill((0, 0, 0))
        pygame.display.flip()
        dt = fps.tick(60) / 1000.0 

if __name__ == "__main__":
    main()
