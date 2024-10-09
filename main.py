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
        if event.type == pygame.QUIT:
            run = False


level_chosen = False
run = True
def menu():
    global level_chosen, run
    pygame.init()
    handle_events()
    while run:
        draw_message("Click Space to Continue", consts.FONT_SIZE, (255,255,255), consts.MSG_LOCATION)
        while not level_chosen:
            event = pygame.event.wait()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    level_chosen = True





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    menu()
    # main_game()
