
class Hangman:
    def __init__ (self, word):
        self.dash_array = []
        self.char_array = []
        self.guessed_array = []
        self.inc_letters = []

        letter_counter = 0
        
        for letter in word:
            self.char_array.append(letter)
            letter_counter += 1

        counter = 0
        while (counter < letter_counter):
            self.dash_array.append("_")
            counter += 1 

      
      
    def checker(self, letter): 
        result = False
        input_arr = []
        if len(letter) > 1: 
            for x in letter: 
                input_arr.append(x)
            print(input_arr)
            if (input_arr == self.char_array):
                self.dash_array = self.char_array
                result = True
        else: 
            for i in range(0, len(self.char_array)): 
                if self.char_array[i] == letter: 
                    self.dash_array[i] = letter
                    result = True
        self.guessed_array.append(letter)

        return result  


    def dashes_rem(self):
        # walk through dash array, check if there's any dashes left
        num_dashes = 0
        for i in self.dash_array: 
            if i == '_': 
                num_dashes += 1

        return num_dashes