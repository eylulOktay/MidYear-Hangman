from tkinter import *
from hangman_object import *

bg_color = "#E5E0FF"
class Hangman_Game_Screen(Frame):

    def __init__(self, master, callback_on_exit):
        super().__init__(master, bg = bg_color)

        self.callback_on_exit = callback_on_exit

        self.create_hangman()
        self.create_widgets()
        self.grid()
        self.display_word()

        master.bind("<KeyRelease>", self.keyRelease)

    def keyRelease(self, e):
        self.currentInc = self.incorrectChars.get()
        self.currentInc += e.char
        self.incorrectChars.set(self.currentInc)

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
        Label(self, text = "HANGMAN", font = "Georgia 25 bold", fg = "black", bg = bg_color).grid(row = 1, column = 0)

        self.incorrectChars = StringVar()
        self.wordChars = StringVar()
        string1 = ""
        wordlen = len(self.hangman.word)
        for int in range(wordlen):
            string1 += "_"
        self.wordChars.set(string1)
        
        Label(self, textvariable = self.wordChars, fg = "black").grid(row = 5, column = 2)
        Label(self, textvariable = self.incorrectChars, fg = "black").grid(row = 6, column = 2)
        Label(self, text = self.hangman.word, fg = "black").grid(row = 7, column = 2)

        #displaying the dash_array
        self.imagelabels = []
        for col in range(len(self.hangman.word)):
            image = PhotoImage(file="images/1Letter/letter_zdash.gif")
            piclabel = Label(self, image = image)
            self.imagelabels.append(piclabel)
            piclabel.photo = image
            piclabel.grid(row = 10, column = col + 1)
        
        #Adding hanger pieces
        #imageSmall = PhotoImage(file="images/hanger.gif")
        #w = Label (self,
                        #image = imageSmall, borderwidth=0
                         #)
        #w.photo = imageSmall
        #w.grid (row = 9, column = 1)
    def create_hangman(self):
        self.hangman = Hangman('wordbank.txt')

    def display_word(self):
        #assigning images to letters
        for char in range(len(self.hangman.dash_array)):
            w = self.imagelabels[char]
            if(char== "_"):
                image = PhotoImage(file="images/1Letter/letterDash.gif")
            else:
                image = PhotoImage(file="images/1letter/letter_" + self.hangman.dash_array[char] + ".gif")
            w.configure(image = image)
            w.image = image
            
    

        Button(self, text = "Exit", font = "Courier 12 bold", fg = "Maroon3", command = self.selected_exit
        ).grid(row = 11, column = 1) 

    def losing_screen(self):
        pass
        #self.no_guesses = False
        #if guesses == 0:
            #self.no_guesses = True

        #if self.no_guesses == True:
            #image = PhotoImage(file="images/ResspassMad.png")
            #piclabel = Label(self, image = image, bg = "", borderwidth = "50px")
            #self.imagelabels.append(piclabel)
            #piclabel.photo = image
            #piclabel.grid(row = 3, column = 1, columnspan = 4, rowspan = 4)
            #Label(self, text = "You Lose!", bg = "Hot Pink", font = "Georgia 24", fg = "white").grid(row = 6, column = 2, columnspan = 2)
    def selected_exit(self):
        self.callback_on_exit()

    def update_correct(self):
        pass 

    def take_input(self):
        pass

    def winning_screen(self):
        pass

    def selected_exit(self):
        self.callback_on_exit()