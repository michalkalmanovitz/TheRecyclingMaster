import pygame
import consts

screen = pygame.display.set_mode(
    (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
def draw_message(message, font_size, color, location):
    font = pygame.font.SysFont(consts.FONT_NAME, font_size)
    text_img = font.render(message, True, color)
    screen.blit(text_img, location)
    pygame.display.flip()

level_chosen = False
def menu():
    global level_chosen
    pygame.init()
    draw_message("Hello world", consts.FONT_SIZE, (255,255,255), consts.MSG_LOCATION)
    pygame.time.delay(1000)
    while not level_chosen:
        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_2:
                level_chosen = True
            elif event.key == pygame.K_3:
                level_chosen = True
            elif event.key == pygame.K_4:
                level_chosen = True
            elif event.key == pygame.K_5:
                level_chosen = True



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    menu()
    # main_game()
