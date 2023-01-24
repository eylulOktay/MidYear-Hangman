# in the case of only one word in file

# reads in the file, creates dash and char array. 
# dash_array[] starts as an array of dashes; the len of this arr is the same as char_arr 
# char_array[] contains the correct word split into letters; 
dash_array = []
char_array = []
guesses = 0
def read():
    word = (open("wordBank.txt")).read() # reading the file 

    letter_counter = 0

    for letter in word:
        char_array.append(letter)
        letter_counter += 1

    counter = 0
    while (counter < letter_counter):
        dash_array.append("_")
        counter += 1

def checker(letter): 
    for i in len(char_array): 
        if char_array[i] == letter: 
            dash_array[i] = letter

def toString(array):
    same_string = ''
    for i in array:
        same_string += i
    return same_string

def main():
    read()
    while (char_array != dash_array):
        print(toString(dash_array))
        user_letter = input("Enter a letter!")
        checker(user_letter)
    print("You won!")

main()
