## This code was created by Logan Maupin - Student at the university of Arizona Online. Studying computer science for AI & data science. 
## If you would like to reach out to me directly, please just use my student email which is -- lmaupin@email.arizona.edu -- Thank you. Enjoy! :) 


# open and read the dictionary txt file
f = open('words_alpha_5only.txt', 'r')
with open('words_alpha_5only.txt') as f:
    lines = f.readlines() # lines variable reads all lines in dictionary file
    stripped_lines = [s.strip() for s in lines] # stripped lines represents all words minus the \n line break
# if you print(stripped_lines) you will print all 5 letter words without any filteration... and yes if you are wondering the master list contains 15,920 words. 

#create loop to hold everything. Break loop if all bottom conditions are a success. 
running = True
while running:

    filtered = [] #creates another empty list for the user input letters
    #input up to 5 lines of string combos. Can not exceed more than 5 total characters (duh). use one line for each letter or set of letters (set meaning letters next to each other).
    good_list = [str(x).lower() for x in input("Enter any letters you know that are in the word - (separate letters with a comma and space): \n").split(', ')]
    
    #the purpose of this for loop is to add up all the string elements letter by letter
    for letters in good_list:
        len(letters)
    length_of_all_good = len(elements) #defining the variable that will be used below, wanted to make sure this variable gets defined outside of the loop just in case. 

    #Input all the bad letters and put them in their own list for later use. 
    bad_list = [str(letters).lower() for letters in input("Enter any letters that you know are NOT in the list - (separate letters with a comma and space, also if you don't know any bad letters just hit space and then enter):  \n").split(', ')]

#if length_of_all_good inputs is more than 5 then tell the user they are a moron, if not proceed with stripping word list.
    if length_of_all_good <= 5:
            for string in stripped_lines:
            # this next line is basically saying look for all strings in the latter 5 (or less) user inputs, and search them against the 5 letter word list
                if all(letters in string for letters in good_list) and not any(letters in string for letters in bad_list): #compare good list to master list and compare bad list to master list. 
                    filtered.append(string)  # modify the word list to *only* include words that contain the matching letters from the (up to) 5 inputs.
                    running = False #break out of the loop -- success!
    else: #tell the user they are a moron and to try again.
        print("Too many characters! Total of all 5 lines must be less than or equal to 5! Please try again:")
        continue

# print the output of all words matching the str texts from the previous if (success) function
print('\n'.join(map(str, filtered)))  # print final output of 5 letter words matching the letters provided in the user input
number_of_items = len(filtered) # number of words in the search result
print("This search has resulted in " + str(number_of_items) + " match(es) to your query.") # prints number string plus var plus string
