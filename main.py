import pygame
import consts

screen = pygame.display.set_mode(
    (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))

def draw_message(message, font_size, color, location):
    font = pygame.font.SysFont(consts.FONT_NAME, font_size)
    text_img = font.render(message, True, color)
    screen.blit(text_img, location)
    pygame.display.flip()
def handle_events():
    global run
    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT:
            run = False


start_game = False
run = True


def menu():
    global start_game, run
    pygame.init()
    handle_events()
    while run:
        draw_message("Click Space to Continue", consts.FONT_SIZE, (255,255,255), consts.MSG_LOCATION)
        while not start_game:
            event = pygame.event.wait()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    start_game = True

        # pygame.display.update()

    pygame.quit()

def main_game():
    if __name__ == '__main__':
        menu()
    # main_game()
