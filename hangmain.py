# in the case of only one word in file

word = (open("wordBank.txt")).read() # reading the file 

letter_counter = 0
dash_array = []
char_array = []

for letter in word:
    char_array.append(letter)
    letter_counter += 1

counter = 0
while (counter < letter_counter):
    dash_array.append("_")
    counter += 1

while ()