from constants import *
import pygame
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    fps = pygame.time.Clock()
    dt = 0
    
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    AsteroidField.containers = (updateable)
    Asteroid.containers = (updateable, drawable, asteroids)
    Player.containers = (updateable, drawable)
    Shot.containers = (updateable, drawable, shots)
    
    # Player spawns in the center of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    AsteroidField()
    
    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Makes sure we can quit
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        dt = fps.tick(60) / 1000.0
        
        updateable.update(dt)
        
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides(shot):
                    asteroid.kill()
                    shot.kill()
            if asteroid.collides(player):
                print("Game over!")
                pygame.quit()
                exit()
        
        # Draws a black screen    
        screen.fill((0, 0, 0))
        for object in drawable:
            object.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()
