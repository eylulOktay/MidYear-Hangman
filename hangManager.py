from tkinter import *
from hangmanOpeningGui import Screen_Opening
from hangmanGUI import Hangman_Game_Screen
from greetingsGUI import Image_Opening

class GameManager(object):

    def __init__(self):
        self.root = Tk()
        self.current_screen = None
    
    def setup_openingImage(self): 
        self.root.title ("Hangman!")
        self.root.geometry ("500x500")
        self.current_screen = Image_Opening (master = self.root, callback_on_exit = self.onclose_openingImage)

    def onclose_openingImage(self):
        self.current_screen.destroy()
        self.setup_openingscreen()
    
    def setup_openingscreen(self):
        self.root.title ("Hangman!")
        self.current_screen = Screen_Opening (master = self.root, callback_on_play = self.onclose_openingscreen)

    def greetingScreen(self): 
        self.hangman = "images/hangman.png"

    def onclose_openingscreen(self):
        self.current_screen.destroy()
        self.setup_gameGUI()

    def setup_gameGUI(self):
        self.root.title ("Hangman!")
        self.root.geometry ("1200x735")
        self.current_screen = Hangman_Game_Screen (master = self.root, callback_on_exit = self.onclose_gameGUI)

    def onclose_gameGUI(self):
        self.current_screen.destroy()
        self.setup_openingscreen()

def main():
    game = GameManager()
    game.setup_openingscreen()
    game.root.mainloop()
main()
