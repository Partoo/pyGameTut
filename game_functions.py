import sys
import pygame


def check_events(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # ship.rect.centerx += 1
                ship.moving_right = True
                ship.moving_left = False
            elif event.key == pygame.K_LEFT:
                ship.moving_right = False
                ship.moving_left = True
        elif event.type == pygame.KEYUP:
            ship.moving_left, ship.moving_right = False, False


def update_screen(ai_settings, screen, ship):
    screen.fill(ai_settings.bg_color)

    ship.blitme()

    pygame.display.flip()
