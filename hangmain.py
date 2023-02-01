# in the case of only one word in file

# reads in the file, creates dash and char array. 
# dash_array[] starts as an array of dashes; the len of this arr is the same as char_arr 
# char_array[] contains the correct word split into letters; 
import random

dash_array = []
char_array = []
inc_letters = []

# reads in file 
def read():
    words = (open("MidYear-Hangman/wordBank.txt")).read() # reading the file
    word_list = words.split("\n")
        
    word_num = random.randrange(0,len(word_list))
    word = word_list[word_num]

    letter_counter = 0
        
    for letter in word:
        char_array.append(letter)
        letter_counter += 1

    counter = 0
    while (counter < letter_counter):
        dash_array.append("_")
        counter += 1

def checker(letter): 
    global dash_array
    result = False
    input_arr = []
    if len(letter) > 1: 
        for x in letter: 
            input_arr.append(x)
        print(input_arr)
        if (input_arr == char_array):
            dash_array = char_array
            result = True
    else: 
        for i in range(0, len(char_array)): 
            if char_array[i] == letter: 
                dash_array[i] = letter
                result = True

    return result

def toString(array):
    same_string = ''
    for i in array:
        same_string += i
    return same_string

def main():
     guesses = 0
     num_wrong = 0
    
     read()
     print("Welcome to Hangman!")
     print(f"Your word has {len(dash_array)} letters.") 
     while char_array != dash_array:
         print(toString(dash_array))
         user_letter = input("Enter a letter or word! ")

         guesses += 1

         if checker(user_letter)==False:
             num_wrong += 1
             inc_letters.append(user_letter)
             if  user_letter.isalpha() == False: # have to check if it's a symbol ... 
                 print("This is not a valid input. Please input a letter or word.")
             else: 
                 print("Nope! Try Again")

         num_dashes = 0
         for x in dash_array: 
             if x == '_': 
                 num_dashes+=1
        
         if num_dashes == 1: 
             print("You're almost there!")
        

     print(toString(dash_array))
     print(f"You won! It took you {guesses} guesses, and you got {num_wrong} wrong.")
     print(f"Incorrect letters: {toString(inc_letters)}")


main()
