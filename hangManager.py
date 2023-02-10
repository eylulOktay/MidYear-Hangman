from tkinter import *
from hangmanOpeningGui import Screen_Opening
from hangmanGUI import Hangman_Game_Screen

class GameManager(object):

    def __init__(self):
        self.root = Tk()
        self.current_screen = None
    
    def setup_openingscreen(self):
        self.root.title ("Hangman!")
        self.root.geometry ("1185x505")
        self.current_screen = Screen_Opening (master = self.root, callback_on_play = self.onclose_openingscreen)
    
    def setup_greetingscreen(self): 
        introducingImg = PhotoImage(file="images/opening.pdf")
        w = Label (self,
                        image = introducingImg, borderwidth=0
                         )
        w.photo = introducingImg
        w.grid (row = 0, column = 1, columnspan = 4)
    
    def onclose_greetscreen(self): 
        self.current_screen.destroy()
        self.setup_openingscreen()

    def onclose_openingscreen(self):
        self.current_screen.destroy()
        self.setup_gameGUI()

    def setup_gameGUI(self):
        self.root.title ("Hangman!")
        self.root.geometry ("900x900")
        self.current_screen = Hangman_Game_Screen (master = self.root, callback_on_exit = self.onclose_gameGUI)

    def onclose_gameGUI(self):
        self.current_screen.destroy()
        self.setup_openingscreen()

def main():
    game = GameManager()
    game.setup_openingscreen()
    game.root.mainloop()
main()
