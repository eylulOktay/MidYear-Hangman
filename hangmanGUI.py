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
        self.displayHangman()
        self.winning_screen()
        self.losing_screen()


        master.bind("<KeyRelease>", self.keyRelease)

    def keyRelease(self, e):
        self.inval = self.hangman.checker("" + (e.char).lower())
        self.incorrectChars.set(self.hangman.dash_array)
        self.wordChars.set(self.hangman.inc_letters)
        self.display_word()
        self.display_incorrect()
        self.displayHangman()
        self.winning_screen()
        self.losing_screen()


    def create_widgets(self):
        #Label(self, text = "HANGMAN", font = "Georgia 24 bold", fg = "black", bg = bg_color).grid(row = 1, column = 2)

        self.incorrectChars = StringVar()
        self.wordChars = StringVar()
        #string1 = ""
        #wordlen = len(self.hangman.word)
        #for int in range(wordlen):
            #string1 += "_"
        #self.wordChars.set(string1)
        
        #Label(self, textvariable = self.incorrectChars, fg = "black").grid(row = 16, column = 2)
        #Label(self, textvariable = self.wordChars, fg = "black").grid(row = 2, column = 2)
        #Label(self, text = self.hangman.word, fg = "black").grid(row = 7, column = 2)

        #displaying the dash_array
        self.dashImageLabels = []
        for col in range(len(self.hangman.dash_array)):
            image = PhotoImage(file="images/1Letter/letter_zdash.gif")
            piclabel = Label(self, image = image, borderwidth=0)
            self.dashImageLabels.append(piclabel)
            piclabel.photo = image
            piclabel.grid(row = 9, column = col + 8) 
        
        #displaying inc_letters
        self.incImageLabels = []
        for coll in range(7):
            img = PhotoImage(file="images/blank.gif")
            picturelabel = Label(self, image  = img, borderwidth=0)
            self.incImageLabels.append(picturelabel)
            picturelabel.photo = img
            picturelabel.grid(row = 6, column = coll + 7) 
        
        Button(self, text = "Exit to Home", font = "Courier 12 bold", fg = "#7286D3", command = self.selected_exit
        ).grid(row = 11, column = 10) 
        
        #Adding hanger pieces
        for num in range(4):
            imageSmall = PhotoImage(file="images/hanger/hangerHorizontal.gif")
            w = Label (self,
                    image = imageSmall, borderwidth=0
                        )
            w.photo = imageSmall
            w.grid (row = 6, column = num + 1)
            
        for numb in range(6):
            imageS = PhotoImage(file="images/hanger/hangerVertical.gif")
            y = Label (self,
                    image = imageS, borderwidth=0
                        )
            y.photo = imageS
            y.grid (row = numb + 7, column = 1)

        imageD = PhotoImage(file="images/blank.gif")
        d = Label (self,
                image = imageD, borderwidth=0
                    )
        d.photo = imageD
        d.grid (row = 8, column = 5)

        imageF = PhotoImage(file="images/blank.gif")
        f = Label (self,
                image = imageF, borderwidth=0
                    )
        f.photo = imageF
        f.grid (row = 10, column = 5)

    #creating object
    def create_hangman(self):
        self.hangman = Hangman('wordbank.txt')

    #update dash array
    def display_word(self):
        #assigning images to letters
        for char in range(len(self.hangman.dash_array)):
            w = self.dashImageLabels[char]
            if(self.hangman.dash_array[char] != '_'):
                image = PhotoImage(file="images/1letter/letter_" + self.hangman.dash_array[char] + ".gif")
                w.configure(image = image)
                w.image = image
            
    #update incorrect array 
    def display_incorrect(self):
        if(len(self.hangman.inc_letters) >= 8):
            return
        for letter in range(len(self.hangman.inc_letters)):
            x = self.incImageLabels[letter]
            
            img = PhotoImage(file="images/1letter/letter_" + self.hangman.inc_letters[letter] + ".gif")
            x.configure(image = img)
            x.img = img
        
    #inserting each hangman part for each wrong guess
    def displayHangman(self):
        if(self.hangman.num_guesses == 7):
            return

        
        #head
        imageS = PhotoImage(file="images/Body/body_head.gif")
        y = Label (self,
                image = imageS, borderwidth=0
                    )
        y.photo = imageS
        y.grid (row = 7, column = 4)

        if(self.hangman.num_guesses == 6):
            return
        #torso1
        imageA = PhotoImage(file="images/Body/body_torso1.gif")
        a = Label (self,
                image = imageA, borderwidth=0
                    )
        a.photo = imageA
        a.grid (row = 8, column = 4)

        if(self.hangman.num_guesses == 5):
            return

        #torso2
        imageB = PhotoImage(file="images/Body/body_torso2.gif")
        b = Label (self,
                image = imageB, borderwidth=0
                    )
        b.photo = imageB
        b.grid (row = 9, column = 4)

        if(self.hangman.num_guesses == 4):
            return

        #arm1
        imageC = PhotoImage(file="images/Body/body_arm1.gif")
        c = Label (self,
                image = imageC, borderwidth=0
                    )
        c.photo = imageC
        c.grid (row = 8, column = 3)

        if(self.hangman.num_guesses == 3):
            return

        #arm2
        imageD = PhotoImage(file="images/Body/body_arm1.gif")
        d = Label (self,
                image = imageD, borderwidth=0
                    )
        d.photo = imageD
        d.grid (row = 8, column = 5)

        if(self.hangman.num_guesses == 2):
            return

        #leg1
        imageE = PhotoImage(file="images/Body/body_leg1.gif")
        e = Label (self,
                image = imageE, borderwidth=0
                    )
        e.photo = imageE
        e.grid (row = 10, column = 3)

        if(self.hangman.num_guesses == 1):
            return

        #leg2
        imageF = PhotoImage(file="images/Body/body_leg2.gif")
        f = Label (self,
                image = imageF, borderwidth=0
                    )
        f.photo = imageF
        f.grid (row = 10, column = 5)


    def losing_screen(self):
        
        if(len(self.hangman.inc_letters) > 6):
            imageS = PhotoImage(file="images/blank.gif")
            y = Label (self,
                    image = imageS, bg = bg_color, borderwidth="500px"
                        )
            y.photo = imageS
            y.grid (row = 6, column = 0, rowspan = 6, columnspan = 20)

            image = PhotoImage(file="images/respassMad.gif")
            piclabel = Label(self, image = image, bg = bg_color, borderwidth = "40px")
            self.dashImageLabels.append(piclabel)
            piclabel.photo = image
            piclabel.grid(row = 1, column = 1, columnspan = 20)

            Label(self, text = "YOU LOST \n\nThe word was " + self.hangman.word + "!", font = "Courier 20 bold", fg = "#7286D3", bg = bg_color).grid(row = 5, column = 8)
            #Label(self, text = "The Word Was " + self.hangman.word + "!", font = "Courier 20 bold", fg = "#7286D3", bg = bg_color).grid(row = 6, column = 8)
            Button(self, text = "Exit to Home", font = "Courier 12 bold", fg = "#7286D3", command = self.selected_exit
            ).grid(row = 6, column = 8)
            
        
    def selected_exit(self):
        self.callback_on_exit()

    def winning_screen(self):
        if(self.hangman.dashes_rem() == 0):
            imageS = PhotoImage(file="images/blank.gif")
            y = Label (self,
                    image = imageS, bg = bg_color, borderwidth="500px"
                        )
            y.photo = imageS
            y.grid (row = 6, column = 0, rowspan = 6, columnspan = 20)

            image = PhotoImage(file="images/respassHappy.gif")
            w = Label (self,
                    image = image, bg = bg_color, borderwidth="50px"
                        )
            w.photo = image
            w.grid (row = 2, column = 1, rowspan = 2, columnspan = 20)

            Label(self, text = "YAY YOU WON!!!", font = "Courier 40 bold", fg = "#7286D3", bg = bg_color).grid(row = 5, column = 8)
            
            Button(self, text = "Exit to Home", font = "Courier 12 bold", fg = "#7286D3", command = self.selected_exit
            ).grid(row = 6, column = 8)


            
        """
        if(self.hangman.dashes_rem() == 0):
            image = PhotoImage(file="images/RespassHappy.gif")
            piclabel = Label(self, image = image, bg = bg_color, borderwidth = "100px")
            self.dashImageLabels.append(piclabel)
            piclabel.photo = image
            piclabel.grid(row = 6, column = 1, columnspan = 10, rowspan = 6)
            Label(self, text = "WOW!! YOU WON!!!", bg = bg_color, font = "Georgia 24", fg = "black").grid(row = 7, column = 7, columnspan = 2)
            """

    def selected_exit(self):
        self.callback_on_exit()