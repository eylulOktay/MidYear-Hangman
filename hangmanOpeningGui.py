from tkinter import *

bg_color = "#E5E0FF"
class Screen_Opening(Frame):
    def __init__(self, master, callback_on_play):
        super().__init__(master, bg = bg_color)

        self.callback_on_play = callback_on_play

        self.create_widgets()
        self.grid()

    def create_widgets(self):
        #self.bttn_hello = Button(self, )
        #self.bttn_hello["text"] = "Hangman!"

        #title
        Label(self, text = "\n\n\n").grid(row = 0)
        title = Label(self, text = "Hangman!", font = "Georgia 100 bold", fg = "#F67280", bg = bg_color)
        title.place(relx = 0.5, rely = 0.5, anchor='center')
        title.grid(row = 0, column = 0)
        
        #Label(self, text = "").grid(row = 0, column = 1, columnspan = 2)
        #Label(self, text = "").grid(row = 0, column = 2)
       
        instruction = Label(self, text = "How to Play:\n\nTry to find the word by guessing letters!\nEvery incorrect letter will draw a part of the Hangman\nTry to find the word in 6 guesses before the full Hangman is drawn!", 
                    font = "Helvetica 30 italic", fg = "#7286D3", bg = bg_color
                    )
        instruction.place(relx = 1, rely = 1, anchor='center')
        instruction.grid(row = 7, column = 0)
        
        Label(self, text = "").grid(row = 6)
        btn = Button(self, text = "Press to Play", 
                     font = "Courier 25 bold", fg = "#ACDDDE", bg = bg_color, command = self.selected_play
                     )
        btn.place(relx = 1, rely = 1, anchor='center')
        btn.grid(row = 15, column = 0)

        Label(self, text = "").grid(row = 6)
        Label(self, text = "").grid(row = 10)
        
    def selected_play(self):
        self.callback_on_play()

   