# Game Initialization
import pygame

pygame.init()


# Game Resolution
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))


# Text Renderer
def text_format(message, textSize, textColor):
    newFont = pygame.font.SysFont('arial', textSize)
    newText = newFont.render(message, 0, textColor)

    return newText


# Colors
white = (255, 255, 255)
black = (0, 0, 0)
gray = (50, 50, 50)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

# Game Fonts
font = pygame.font.SysFont('arial',42)

# Game Framerate
clock = pygame.time.Clock()
FPS = 30


# Main Menu
def start_menu():
    startmenu = True
    selected = "RA-Dec to ALT AZ"


    while startmenu:

        pos = pygame.mouse.get_pos()
        pressed = pygame.mouse.get_pressed()

        # Main Menu UI
        screen.fill(blue)
        title = text_format("Project RT", 90, yellow)
        if selected == "RA-Dec to ALT AZ":
            text_RAA = text_format("RA-Dec to ALT AZ", 75, white)
        else:
            text_RAA = text_format("RA-Dec to ALT AZ", 75, black)
        if selected == "Back":
            text_back = text_format("BACK", 75, white)
        else:
            text_back = text_format("BACK", 75, black)
        if selected == "quit":
            text_quit = text_format("QUIT", 75, white)
        else:
            text_quit = text_format("QUIT", 75, black)

        title_rect = title.get_rect()

        # Main Menu Text
        start_rect = text_RAA.get_rect()
        back_rect = text_back.get_rect()
        quit_rect = text_quit.get_rect()
        back_rect_1 = pygame.draw.rect(screen, black,
                                       (screen_width / 2 - (back_rect[2] / 2 + 20), 380, back_rect[2] + 40,
                                        back_rect[1] + 90))
        back_rect_2 = pygame.draw.rect(screen, blue,
                                       (screen_width / 2 - (back_rect[2] / 2 + 10), 390, back_rect[2] + 20,
                                        back_rect[1] + 70))
        Start_rect_1 = pygame.draw.rect(screen, black,
                                        (screen_width / 2 - (start_rect[2] / 2 + 20), 300, start_rect[2] + 40,
                                         start_rect[1] + 90))
        start_rect_2 = pygame.draw.rect(screen, blue,
                                        (screen_width / 2 - (start_rect[2] / 2 + 10), 310, start_rect[2] + 20,
                                         start_rect[1] + 70))
        quit_rect_1 = pygame.draw.rect(screen, black,
                                       (screen_width / 2 - (quit_rect[2] / 2 + 20), 460, quit_rect[2] + 40,
                                        quit_rect[1] + 90))
        quit_rect_2 = pygame.draw.rect(screen, blue,
                                       (screen_width / 2 - (quit_rect[2] / 2 + 10), 470, quit_rect[2] + 20,
                                        quit_rect[1] + 70))

        if back_rect_1.collidepoint(pos) and pressed:
            selected = "Back"


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if selected == "RA-Dec to ALT AZ":
                        selected = "quit"
                    elif selected == "Back":
                        selected = "RA-Dec to ALT AZ"
                    else:
                        selected = "Back"

                elif event.key == pygame.K_DOWN:
                    if selected == "RA-Dec to ALT AZ":
                        selected = "Back"
                    elif selected == "Back":
                        selected = "quit"
                    else:
                        selected = "RA-Dec to ALT AZ"
                if event.key == pygame.K_RETURN:
                    if selected == "RA-Dec to ALT AZ":
                        print("RA-Dec to ALT AZ")
                    elif selected == "Back":
                        print("Back")
                    elif selected == "quit":
                        pygame.quit()
                        quit()


        screen.blit(title, (screen_width / 2 - (title_rect[2] / 2), 80));    '''DONT CHANGE THIS LINE'''
        screen.blit(text_RAA, (screen_width / 2 - (start_rect[2] / 2), 300))
        screen.blit(text_back, (screen_width / 2 - (back_rect[2] / 2), 380))
        screen.blit(text_quit, (screen_width / 2 - (quit_rect[2] / 2), 460))


        pygame.display.update()
        clock.tick(FPS)
        pygame.display.set_caption("Python - Pygame Simple Main Menu Selection")
start_menu()
pygame.quit()
quit()


