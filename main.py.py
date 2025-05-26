import pygame
ymport
import sys

pygame.init()

screen = pygame.display.set_mode(size=(720,900))

def calculate_result(text):
    pass
def calculate_level(text):
    pass

class Button():
    def __init__(self,x,y,text,color,size):
        self.text_font = pygame.font.SysFont("Arial",size)
        self.surface = self.text_font.render(text,True,color)
        self.rect = self.surface.get_rect()
        self.rect.topleft = (x,y)
        self.text = text
        self.color=color

    def checkForInput(self):
        pos=pygame.mouse.get_pos()
        return pos[0] in range(self.rect.left,self.rect.right)  and pos[1] in range(self.rect.top,self.rect.bottom)

    def draw(self):
        if self.checkForInput():
            self.surface = self.text_font.render(self.text,True,"red")
        else:
            self.surface = self.text_font.render(self.text,True,self.color)

        screen.blit(self.surface, (self.rect.x,self.rect.y))



def main_menu():
    pygame.display.set_caption("Menu")
    screen.fill("black")

    button_play = Button(100,0,"Jouer","blue",30)
    button_quit = Button(100,100,"Quitter","blue",30)
    running=True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT :
                pygame.quit()
                sys.exit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                if button_play.checkForInput():
                    calculator()
                elif button_quit.checkForInput():
                    running=False
                    pygame.quit()

        screen.fill("black")

        button_play.draw()
        button_quit.draw()


        pygame.display.update()

def calculator():
    pygame.display.set_caption("Calculatrice")
    screen.fill("black")
    button_menu = Button(100,0,"Revenir au Menu","blue",25)
    button_enter = Button(250,650,'Calculer',"green",50)
    button_writing= Button(80,80,"","white",30)

    buttons=[]
    for i in range(3):
        for j in range(3):
            buttons.append(Button(150*(j+1),100*(i+1)+100,str(3*i+j),"blue",100))
    buttons.append(Button(150*(0+1),100*(3+1)+100,"9","blue",100))
    buttons.append(Button(150*(0+2),100*(3+1)+100,".","blue",100))
    buttons.append(Button(150*(0+3),100*(3+1)+100,"x","blue",100))
    buttons.append(Button(560,200,"+","green",100))
    buttons.append(Button(570,300,"-","green",100))
    buttons.append(Button(570,400,"*","green",100))
    buttons.append(Button(570,500,"/","green",100))



    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT :
                pygame.quit()
                sys.exit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                if button_menu.checkForInput():
                    main_menu()

                for button in buttons :
                    if button.checkForInput():
                        if button.text == "x":
                            length = len(button_writing.text)
                            button_writing.text=(button_writing.text)[0:(length-1)]

                        else:
                            button_writing.text=button_writing.text + button.text


                if button_enter.checkForInput():
                    button_writing.text = calculate_result(button_writing.text)
                    #debut animation
                    pygame.time.delay(500)
                    #fin animation
                    #calcul niveau
                    level = calculate_level(button_writing.text)
                    #lancer le jeu
                    game_mode(level)

        screen.fill("black")

        for button in buttons:
            button.draw()
        button_menu.draw()
        button_enter.draw()
        button_writing.draw()
        pygame.display.update()



def game_level1():
    pass


def game_mode(level):
    pass


main_menu()
pygame.quit()