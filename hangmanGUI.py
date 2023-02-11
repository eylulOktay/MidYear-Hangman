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
        self.display_incorrect()

        master.bind("<KeyRelease>", self.keyRelease)

    def keyRelease(self, e):
        self.inval = self.hangman.checker("" + (e.char).lower())
        self.incorrectChars.set(self.hangman.dash_array)
        self.wordChars.set(self.hangman.inc_letters)
        self.display_word()
        self.display_incorrect()


    def create_widgets(self):
        #Label(self, text = "HANGMAN", font = "Georgia 24 bold", fg = "black", bg = bg_color).grid(row = 1, column = 2)

        self.incorrectChars = StringVar()
        self.wordChars = StringVar()
        #string1 = ""
        #wordlen = len(self.hangman.word)
        #for int in range(wordlen):
            #string1 += "_"
        #self.wordChars.set(string1)
        
        Label(self, textvariable = self.incorrectChars, fg = "black").grid(row = 16, column = 2)
        Label(self, textvariable = self.wordChars, fg = "black").grid(row = 2, column = 2)
        Label(self, text = self.hangman.word, fg = "black").grid(row = 7, column = 2)

        #displaying the dash_array
        self.dashImageLabels = []
        for col in range(len(self.hangman.dash_array)):
            image = PhotoImage(file="images/1Letter/letter_zdash.gif")
            piclabel = Label(self, image = image)
            self.dashImageLabels.append(piclabel)
            piclabel.photo = image
            piclabel.grid(row = 10, column = col + 7) 
        
        #displaying inc_letters
        self.incImageLabels = []
        for coll in range(len(self.hangman.inc_letters)):
            img = PhotoImage(file="images/blank.gif")
            picturelabel = Label(self, img  = img)
            self.incImageLabels.append(picturelabel)
            picturelabel.photo = img
            picturelabel.grid(row = 14, column = coll + 7) 
        
        Button(self, text = "Exit", font = "Courier 12 bold", fg = "Maroon3", command = self.selected_exit
        ).grid(row = 20, column = 1) 
        
        #Adding hanger pieces
        for num in range(4):
            imageSmall = PhotoImage(file="images/hanger/hangerHorizontal.gif")
            w = Label (self,
                    image = imageSmall, borderwidth=0
                        )
            w.photo = imageSmall
            w.grid (row = 9, column = num + 1)
            
        for numb in range(5):
            imageS = PhotoImage(file="images/hanger/hangerVertical.gif")
            y = Label (self,
                    image = imageS, borderwidth=0
                        )
            y.photo = imageS
            y.grid (row = numb + 1, column = 1)

    def create_hangman(self):
        self.hangman = Hangman('wordbank.txt')

    def display_word(self):
        #assigning images to letters
        for char in range(len(self.hangman.dash_array)):
            w = self.dashImageLabels[char]
            if(self.hangman.dash_array[char] != '_'):
                image = PhotoImage(file="images/1letter/letter_" + self.hangman.dash_array[char] + ".gif")
                w.configure(image = image)
                w.image = image
            
    def display_incorrect(self):
        for letter in range(len(self.hangman.inc_letters)):
            x = self.incImageLabels[letter]
            
            img = PhotoImage(file="images/1letter/letter_" + self.hangman.inc_letters[letter] + ".gif")
            x.configure(img = img)
            x.img = img

    def inval_input_screen(self):
        if(self.inval == False):
            image = PhotoImage(file="images/RespassMad.png")
            piclabel = Label(self, image = image, bg = "Hot Pink", borderwidth = "50px")
            self.imagelabels.append(piclabel)
            piclabel.photo = image
            piclabel.grid(row = 3, column = 1, columnspan = 4, rowspan = 2)
            Label(self, text = "Invalid!!", bg = "Hot Pink", font = "Georgia 24", fg = "white").grid(row = 3, column = 2, columnspan = 2)



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
        image = PhotoImage(file="images/RespassMad.png")
        piclabel = Label(self, image = image, bg = "Hot Pink", borderwidth = "50px")
        self.imagelabels.append(piclabel)
        piclabel.photo = image
        piclabel.grid(row = 3, column = 1, columnspan = 4, rowspan = 2)
        Label(self, text = "Invalid!!", bg = "Hot Pink", font = "Georgia 24", fg = "white").grid(row = 3, column = 2, columnspan = 2)

    def selected_exit(self):
        self.callback_on_exit()