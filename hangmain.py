from hangman_object import Hangman 

def toString(array):
    same_string = ''
    for i in array:
        same_string += i
    return same_string

def main():

    h = Hangman("MidYear-Hangman/wordBank.txt")
    print(f"Welcome to Hangman! You have six guesses to guess the {len(h.char_array)} letter word!")
    print(f"Your word has {len(h.dash_array)} letters.") 
    while h.dashes_rem() != 0 and h.num_guesses > 0:
    
        print(toString(h.dash_array))
        user_letter = input("Enter a letter or word! ")
        print(h.num_guesses)

        if h.checker(user_letter)==False:
            if  user_letter.isalpha() == False: # have to check if it's a symbol ... 
                print("This is not a valid input. Please input a letter or word.")
            if h.num_guesses ==0: 
                print("Nope!")
            else: 
                print("Nope! Try Again")
            
        if h.dashes_rem == 1: 
            print("You're almost there!")
        print(h.guessed_array)
        

    if h.dash_array != h.char_array: 
        print(f"You lost. The word was {toString(h.char_array)}!")
    else: 
        print(f"You won! It took you {h.num_guesses} guesses, and you got {h.num_wrong} wrong.")
    print(f"Incorrect letters: {h.inc_letters}")


main()
