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
    screen3 = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
    surface2 = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
    surface3 = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
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
    show_a_text = False
    show_b_text = False
    show_c_text = False
    show_d_text = False

    def draw_pause():
        pygame.draw.rect(surface, (128, 128, 128, 150), [0, 0, SCREEN_WIDTH, SCREEN_HEIGHT])
        pygame.draw.rect(surface, 'blue', [200, 150, 600, 50], 0, 10)
        reset = pygame.draw.rect(surface, 'white', [200, 220, 280, 50], 0, 10)
        save = pygame.draw.rect(surface, 'white', [520, 220, 280, 50], 0, 10)
        surface.blit(font.render('Game Paused: Space to Resume', True, "black"), (220, 160))
        surface.blit(font.render('Reset Game', True, "black"), (220, 230))
        surface.blit(font.render('Save Game', True, "black"), (540, 230))
        screen.blit(surface, (0,0))
        #creates a new window for the pause screen, allowing the main game window to be frozen while the pause screen is displayed
        screen2.fill((0, 0, 0, 0))  # Clear the second screen
        surface2.fill((0, 0, 0, 0))  # Clear the surface for the second screen
        #creates text for the new window
        surface2.blit(font.render('An enemy appears:', True, "white"), (220, 160))
        surface2.blit(font.render('Press Space to Resume', True, "white"), (220, 380))
        surface2.blit(font.render('A to Attack', True, "white"), (800, 160))
        surface2.blit(font.render('B to Defend', True, "white"), (800, 260))
        surface2.blit(font.render('C to Spell', True, "white"), (800, 360))
        surface2.blit(font.render('D to Heal', True, "white"), (800, 460))
        #surface2.blit(font.render('Heal!', True, "white"), (220, 480))
        # creates an enemy sprite on the new window
        pygame.draw.circle(screen2, "white", (400, 300), 20, 2)
        #enemy = Enemy(400, 300, 20)
        #surface2.blit(font.render('Game Paused: Space to Resume', True, "white"), (220, 160))
        screen2.blit(surface2, (0,0))
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
                #if the a key is pressed during pause, display "Attack!" on the second screen
                #if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    if pause:
                        #img = font.render('You chose to Attack!', True, "white"), (220, 160)
                        #surface3.blit(font.render('The enemy takes damage!', True, "white"), (220, 260))
                        #screen3.blit(img, (300,250))
                        show_a_text = True
                    else:
                        show_a_text = False
                    #surface2.blit(font.render('Attack!', True, "white"), (220, 480))
                    #screen2.blit(surface2, (0,0))
                    #if pause:
                        #show_a_text = True
                    #else:
                        #show_a_text = False
            #if the b key is pressed during pause, display "Defend!" on the second
            #if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    if pause:
                        show_b_text = True
                    else:
                        show_b_text = False
            #if the c key is pressed during pause, display "Spell!" on the second screen
            #if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    if pause:
                        show_c_text = True
                    else:
                        show_c_text = False
            #if the d key is pressed during pause, display "Heal!" on the second screen
            #if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    if pause:
                        show_d_text = True
                    else:
                        show_d_text = False

        if show_a_text:
            img = font.render('You chose to Attack!', True, "white")
            #surface3.blit(font.render('The enemy takes damage!', True, "white"), (220, 260))
            screen3.blit(img, (220, 260))
            #show_a_text = True
            #surface2.blit(font.render('Attack!', True, "white"), (220, 480))
            #screen2.blit(surface2, (0,0))
        if show_b_text:
            surface2.blit(font.render('Defend!', True, "white"), (220, 480))
            screen2.blit(surface2, (0,0))
        if show_c_text:
            surface2.blit(font.render('Spell!', True, "white"), (220, 480))
            screen2.blit(surface2, (0,0))
        if show_d_text:
            surface2.blit(font.render('Heal!', True, "white"), (220, 480))
            screen2.blit(surface2, (0,0))

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
