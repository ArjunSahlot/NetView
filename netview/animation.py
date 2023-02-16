import pygame
from image import generate_image

FPS = 90

# Window Management
a = generate_image([3, 6, 10, 4], False)
width, height = a[0], a[1]
WINDOW = pygame.display.set_mode(a, pygame.RESIZABLE)
pygame.display.set_caption("Game")


def main(window):
    pygame.init()
    clock = pygame.time.Clock()
    resized = False

    while True:
        clock.tick(FPS)
        window.fill((255, 255, 255))
        events = pygame.event.get()
        keys = pygame.key.get_pressed()
        ctrl_pressed = keys[pygame.K_LCTRL] or keys[pygame.K_RCTRL]
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q and ctrl_pressed:
                    pygame.quit()
                    return

            elif event.type == pygame.VIDEORESIZE:
                last_width, last_height = width, height
                width, height = event.w, event.h
                resized = True

            elif event.type == pygame.ACTIVEEVENT and resized and width != last_width and height != last_height:
                window = pygame.display.set_mode((width, height), pygame.RESIZABLE)
                resized = False

        pygame.display.update()


main(WINDOW)
