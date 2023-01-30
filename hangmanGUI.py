from tkinter import *
from hangmain import *

bg_color = "#E5E0FF"
class Hangman_Game_Screen(Frame):

    def __init__(self, master, callback_on_exit):
        super().__init__(master, bg = bg_color)

        self.callback_on_exit = callback_on_exit

        self.create_widgets()
        self.grid()

    #def setup_grid(self):
        #self.grid1 = Grid()

    #def display_grid(self):
        #for row in range(0):
        #row = 0
        #for row in range(0,4):
            #rowonetext = ""
            #for col in range(0,4):
                #if self.grid1.grid[row][col] == None:
                    #rowonetext += "  x  "
                #else:
                    #rowonetext += "   " + str(self.grid1.grid[row][col])

            #self.rowtexts[row].set(rowonetext)

    def create_widgets(self):
        Label(self, text = "HANGMAN", font = "Georgia 25 bold", fg = "black", bg = bg_color).grid(row = 0, column = 1)

        #imageSmall = PhotoImage(file="images/hanger.gif")
        #w = Label (self,
                        #image = imageSmall, borderwidth=0
                         #)
        #w.photo = imageSmall
        #w.grid (row = 3, column = 1)
        #Label(self, text = "2048", font = "Georgia 25 bold", fg = "Hot Pink").grid(row = 0, column = 1)
        #Label(self, text = "\n\n\n\n\n\n\n").grid(row = 1)

        #Label(self, text = "Score:", font = "Georgia 15", fg = "Hot Pink"). grid (row = 0, column = 2)

        #self.rowtexts = []
        #for row in range(0,4):
            #rowtext = StringVar()
            #rowtext.set("")
            #Label(self, textvariable = rowtext).grid(row = row + 2, column = 1)
            #self.rowtexts.append(rowtext)

        #Button(self, text = "Exit", font = "Courier 12 bold", fg = "Maroon3", command = self.callback_on_exit
        #).grid(row = 6, column = 1) */

    def selected_exit(self):
        self.callback_on_exit()