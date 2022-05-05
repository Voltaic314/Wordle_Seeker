# open and read the dictionary txt file
f = open('words_alpha_5only.txt', 'r')
with open('words_alpha_5only.txt') as f:
    lines = f.readlines() # lines variable reads all lines in dictionary file
    stripped_lines = [s.strip() for s in lines] # stripped lines represents all words minus the \n line break

five_letter_words = [] # creates an empty list to fill
for i in stripped_lines: # for loop
        five_letter_words.append(i) # fill the empty list with words from the text file

running = True
while running:

    filtered = [] #creates another empty list for the user input letters

    #input up to 5 lines of string combos. Can not exceed more than 5 total characters (duh). use one line for each letter or set of letters (set meaning letters next to each other).
    substring1 = input("Please enter the first letter you know: ").lower()
    substring2 = input("Please enter the second letter you know - (If you don't have a second, just hit enter): ").lower()
    substring3 = input("Please enter the third letter you know - (If you don't have a third, just hit enter): ").lower()
    substring4 = input("Please enter the fourth letter you know - (If you don't have a fourth, just hit enter): ").lower()
    substring5 = input("Please enter the fifth letter you know - (If you don't have a fifth, just hit enter): ").lower()

        print("\nWARNING: DO NOT HIT ENTER WITH NO INPUT ON THE NEXT INPUTS\n WARNING: DO NOT HIT ENTER WITH NO INPUT ON THE NEXT INPUTS\n WARNING: DO NOT HIT ENTER WITH NO INPUT ON THE NEXT INPUTS\n WARNING: DO NOT HIT ENTER WITH NO INPUT ON THE NEXT INPUTS\n WARNING: DO NOT HIT ENTER WITH NO INPUT ON THE NEXT INPUTS\n ")

    # Taking multiple inputs
    bad_1 = input("Please input a letter you know is not in the word - If you don't have one, type space and hit enter: ").lower()
    bad_2 = input("Please input a letter you know is not in the word - If you don't have one, type space and hit enter: ").lower()
    bad_3 = input("Please input a letter you know is not in the word - If you don't have one, type space and hit enter: ").lower()
    bad_4 = input("Please input a letter you know is not in the word - If you don't have one, type space and hit enter: ").lower()
    bad_5 = input("Please input a letter you know is not in the word - If you don't have one, type space and hit enter: ").lower()
    bad_6 = input("Please input a letter you know is not in the word - If you don't have one, type space and hit enter: ").lower()
    bad_7 = input("Please input a letter you know is not in the word - If you don't have one, type space and hit enter: ").lower()
    bad_8 = input("Please input a letter you know is not in the word - If you don't have one, type space and hit enter: ").lower()
    
    # adds up the length of characters from each input of the 5 user input lines
    length_of_all = len(substring1) + len(substring2) + len(substring3) + len(substring4) + len(substring5)

#if length of all 5 user inputs is more than 5...
    if length_of_all <= 5:
            for string in five_letter_words:
        # this next line is basically saying look for all strings in the latter 5 (or less) user inputs, and search them against the 5 letter word list
                if substring1 in string and substring2 in string and substring3 in string and substring4 in string and substring5 in string and bad_1 not in string and bad_2 not in string and bad_3 not in string and bad_4 not in string and bad_5 not in string and bad_6 not in string and bad_7 not in string and bad_8 not in string:
                    filtered.append(string)  # modify the word list to *only* include words that contain the matching letters from the (up to) 5 inputs.
                    running = False #break out of the loop -- success!
    else: #tell the user they are a moron and to try again.
        print("Too many characters! Total of all 5 lines must be less than or equal to 5! Please try again:")

# print the output of all words matching the str texts from the previous if (success) function
print('\n'.join(map(str, filtered)))  # print final output of 5 letter words matching the letters provided in the user input
