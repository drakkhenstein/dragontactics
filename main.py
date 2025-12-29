import pygame
import sys
from constants import *
from player import *
from circleshape import *
from enemy import *
from battlefield import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen2 = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
    clock = pygame.time.Clock()
    dt = 0
    font = pygame.font.Font('freesansbold.ttf', 36)
    #player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    #asteroids = pygame.sprite.Group()
    #shots = pygame.sprite.Group()
    #bullets = pygame.sprite.Group()

    Enemy.containers = (enemies, updatable, drawable)
    #Asteroid.containers = (asteroids, updatable, drawable)
    #Shot.containers = (shots, updatable, drawable)
    
    Battlefield.containers = updatable
    battlefield = Battlefield()
    #AsteroidField.containers = updatable
    #asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    pause = False

    def draw_pause():
        pygame.draw.rect(surface, (128, 128, 128, 150), [0, 0, SCREEN_WIDTH, SCREEN_HEIGHT])
        pygame.draw.rect(surface, 'blue', [200, 150, 600, 50], 0, 10)
        reset = pygame.draw.rect(surface, 'white', [200, 220, 280, 50], 0, 10)
        save = pygame.draw.rect(surface, 'white', [520, 220, 280, 50], 0, 10)
        surface.blit(font.render('Game Paused: Space to Resume', True, "black"), (220, 160))
        surface.blit(font.render('Reset Game', True, "black"), (220, 230))
        surface.blit(font.render('Save Game', True, "black"), (540, 230))
        screen.blit(surface, (0,0))
        return reset, save

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if pause:
                        pause = False
                    else:
                        pause = True 
        screen.fill("green")
        #screen.blit(surface, (10, 10))
        #((f'dist: {distance} m', True, 'black'), (10, 10))
        #pause = False
        if pause:
            restart, saves = draw_pause()
            #pygame.display.update()

        if not pause:
            updatable.update(dt)
            

        #while pause is False:
            #updatable.update(dt)
        for entity in drawable:
            entity.draw(screen)

        for enemy in enemies:
            if enemy.collision(player):
                #write("Game Paused", 500, 150)
                #write("Press 'space bar' to continue", 500, 250)
                #pygame.display.update()
                #pause()
                enemy.kill()
                pause = True

                
                # Draw pause screen
                #if pause:
                    #pygame.draw.rect(surface, (128, 128, 128, 150), [0, 0, SCREEN_WIDTH, SCREEN_HEIGHT])
                    #pygame.draw.rect(surface, 'blue', [200, 150, 600, 50], 0, 10)
                    #reset = pygame.draw.rect(surface, 'white', [200, 220, 280, 50], 0, 10)
                    #save = pygame.draw.rect(surface, 'white', [520, 220, 280, 50], 0, 10)
                    #screen.blit(surface, (0,0))
                #if pause:
                    
                #font = pygame.font.Font(None, 36)
                #text = font.render("Game Over!", True, "black")
                #text_rect = text.get_rect(center=(SCREEN_WIDTH / 2, 175))
                #surface.blit(text, text_rect)
                

                #if event.type == pygame.KEYDOWN:
                    #if event.key == pygame.K_SPACE and not pause:
                        #if pause:
                            #pause = False
                        #else:
                            #pause = True
                #screen.fill("black")

                #pause = True
                #dt = clock.tick(0)  # seconds
                #updatable.update(dt + 1)  # freeze the game
                
                #print("Game Over!")
                #pygame.quit()
                #sys.exit()


        pygame.display.flip()

        dt = clock.tick(60) / 1000  # seconds
    print ("  *** Welcome to Dragon Tactics! ***  ")
    print ("\n")
    print ("  Use the arrow keys to move your dragon around the screen.  ")
    print ("  *** Thank you for playing! ***  ")
    print (f"Screen width: {SCREEN_WIDTH}")
    print (f"Screen height: {SCREEN_HEIGHT}")
    

if __name__ == "__main__":
    main()
