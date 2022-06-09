import pygame, sys
from button import Button  

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Sudoku Game Menu")

BG = pygame.image.load("assets/Background.png")

def get_font(size): 
    return pygame.font.Font("assets/font.ttf", size)
                 
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        OPTIONS_TEXT = get_font(40).render("SUDOKU Instructions", True, "gold") 
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 60))
        OPTIONS_TEXT1 = get_font(18).render("1. In Sudoku we can input number from 1-9 ", True, "white") 
        OPTIONS_RECT1 = OPTIONS_TEXT1.get_rect(center=(640, 160))
        OPTIONS_TEXT2 = get_font(18).render("2. Inputted number should not be repeated with respective column", True, "white") 
        OPTIONS_RECT2 = OPTIONS_TEXT2.get_rect(center=(640, 260))
        OPTIONS_TEXT3 = get_font(18).render("and row and its respective box.", True, "white") 
        OPTIONS_RECT3 = OPTIONS_TEXT3.get_rect(center=(640, 280)) 
        OPTIONS_TEXT4 = get_font(18).render("And That's it, Have fun :) ", True, "green") 
        OPTIONS_RECT4 = OPTIONS_TEXT4.get_rect(center=(640, 380))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)
        SCREEN.blit(OPTIONS_TEXT1, OPTIONS_RECT1) 
        SCREEN.blit(OPTIONS_TEXT2, OPTIONS_RECT2) 
        SCREEN.blit(OPTIONS_TEXT3, OPTIONS_RECT3) 
        SCREEN.blit(OPTIONS_TEXT4, OPTIONS_RECT4)

        OPTIONS_BACK = Button(image=None, pos=(640, 520), 
                            text_input="BACK", font=get_font(75), base_color="blue", hovering_color="red")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400), 
                            text_input="INSTRUCTIONS", font=get_font(48), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
     
        pygame.display.update()

def play():
    while True:
        from GUI import main
        SCREEN.fill("white") 
        main()
        pygame.quit()
main_menu()
pygame.quit()
