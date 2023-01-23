from tkinter import *

class Screen_Opening(Frame):
    def __init__(self, master, callback_on_play):
        super().__init__(master)

        self.callback_on_play = callback_on_play

        self.create_widgets()
        self.grid()

    def create_widgets(self):

        #title
        Label(self, text = "\n\n\n").grid(row = 0)
        Label(self, text = "Hangman", font = "Georgia 45 bold", fg = "Hot Pink").grid(row = 3, column = 1)
        Label(self, text = "").grid(row = 4)
        Label(self, text = "").grid(row = 6)
        Button(self, text = "Press to Play", 
                     font = "Courier 12 bold", fg = "Maroon3", command = self.selected_play
                     ).grid(row = 7, column = 1)

    def selected_play(self):
        self.callback_on_play()