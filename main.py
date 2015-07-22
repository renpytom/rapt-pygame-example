# Allow pygame_sdl2 to be imported as pygame.
import pygame_sdl2
pygame_sdl2.import_as_pygame()

import pygame
import os

def save_state(x, y):
    """
    Saves the game state.
    """

    with open("state.txt", "w") as f:
        f.write("{} {}".format(x, y))

def load_state():
    try:
        with open("state.txt", "r") as f:
            x, y = f.read().split()
            x = int(x)
            y = int(y)

        return x, y
    except:
        return None, None

def delete_state():

    if os.path.exists("state.txt"):
        os.unlink("state.txt")


def main():
    pygame.init()

    screen = pygame.display.set_mode((1280, 720))
    screen_w, screen_h = screen.get_size()

    icon = pygame.image.load("pygame-icon.png")
    icon = icon.convert_alpha()
    icon_w, icon_h = icon.get_size()

    font = pygame.font.Font("DejaVuSans.ttf", 24)
    text = font.render("Touch the screen.", True, (255, 255, 255, 255))
    text_w, text_h = text.get_size()

    sleeping = False

    # On startup, load state saved by APP_WILLENTERBACKGROUND, and the delete
    # that state.
    x, y = load_state()
    delete_state()

    while True:

        # If not sleeping, draw the screen.
        if not sleeping:
            screen.fill((0, 0, 0, 255))

            screen.blit(text, (screen_w / 2 - text_w / 2, screen_h / 2 - text_h / 2))

            if x is not None:
                screen.blit(icon, (x - icon_w / 2, y - icon_h / 2))

            pygame.display.flip()


        ev = pygame.event.wait()

        # Pygame quit.
        if ev.type == pygame.QUIT:
            break

        # Android back key.
        elif ev.type == pygame.KEYDOWN and ev.key == pygame.K_AC_BACK:
            break

        elif ev.type == pygame.MOUSEBUTTONDOWN:
            x, y  = ev.pos

        elif ev.type == pygame.APP_WILLENTERBACKGROUND:
            # The app is about to go to sleep. It should save state, cancel
            # any timers, and stop drawing the screen until an APP_DIDENTERFOREGROUND
            # event shows up.

            save_state(x, y)

            sleeping = True

        elif ev.type == pygame.APP_DIDENTERFOREGROUND:
            # The app woke back up. Delete the saved state (we don't need it),
            # restore any times, and start drawing the screen again.

            delete_state()
            sleeping = False

            # For now, we have to re-open the window when entering the
            # foreground.
            screen = pygame.display.set_mode((1280, 720))


if __name__ == "__main__":
    main()



