from colors import colors
import pygame



background = colors.cyan
framerate = 60
timer = pygame.time.Clock()
running = True

def update_ball_position():
    pass

while running:
    timer.tick(framerate)
    update_ball_position()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((background))

    pygame.draw.circle(screen, colors.geren, (circle_x, circle_y), 30, 5)

    pygame.display.flip()

pygame.quit()

