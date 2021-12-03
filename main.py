import pygame
from pygame.constants import K_ESCAPE, KEYDOWN, KEYUP, MOUSEBUTTONUP

pygame.init()
windowSize = [1280, 720]
window = pygame.display.set_mode(windowSize)
pygame.display.set_caption("Pygame Picross")

def main():
    EXIT = False
    clock = pygame.time.Clock()
    while not EXIT:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                EXIT = True
            elif event.type == KEYDOWN:
                # TODO Do stuff
                print("lol")
            elif event.type == KEYUP:
                if(event.key == K_ESCAPE):
                    EXIT = True
            elif event.type == MOUSEBUTTONUP:
                # TODO Do click stuff
                print("lol")
        clock.tick(30)
        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()