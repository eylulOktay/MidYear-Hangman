import random

class Hangman:
    def __init__ (self, filename):
        self.dash_array = []
        self.char_array = []
        self.guessed_array = []
        self.input_arr = []
        self.inc_letters = []
        self.num_wrong = 0
        self.num_guesses = 7

        letter_counter = 0
        
        words = (open(filename)).read() # reading the file
        word_list = words.split("\n")
            
        word_num = random.randrange(0,len(word_list))
        self.word = word_list[word_num]

        for letter in self.word:
            self.char_array.append(letter)
            letter_counter += 1

        counter = 0
        while (counter < letter_counter):
            self.dash_array.append("_")
            counter += 1 

      
      
    def checker(self, letter): 
        result = False
        # if full word 
        if letter in self.inc_letters or letter.isalpha() == False: 
            return False 
        else: 
            if len(letter) > 1: 
                for x in letter: 
                    self.input_arr.append(x)
                if (self.input_arr == self.char_array):
                    self.dash_array = self.char_array
                    result = True
                else:
                    self.num_wrong += 1
                    self.inc_letters.append(letter)
                    self.num_guesses -= 1
            else: 
                # if single letter 
                for i in range(0, len(self.char_array)): 
                    if self.char_array[i] == letter: 
                        self.dash_array[i] = letter
                        result = True
                if result == False: 
                    self.num_wrong += 1
                    self.inc_letters.append(letter)
                    self.num_guesses -= 1
            self.guessed_array.append(letter)

            return result  


    def dashes_rem(self):
        # walk through dash array, check if there's any dashes left
        num_dashes = 0
        for i in self.dash_array: 
            if i == '_': 
                num_dashes += 1

        return num_dashes