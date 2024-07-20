"""
Author: Logan Maupin
Date: 11/10/2022

This script is made for the purpose of trying to provide (possible) answer solution hints to the game
Wordle.

How this script works:
When you run this script, it will ask if you know any letters positions in the target word. If so, we need to know
what letters and where at. If not, then we need to know if you know any letters in the word and any letters not in the
word.

If you do know any letters positions, as you type them, the script will filter words out of the original list if they
don't contain that letter at that position.

if you know any good letters (letters we know are in the target word), then the script will check to make sure that ALL
of your good letters are in each word or else it will remove them from the list.

if you know any bad letters, (letters we know that aren't in the word), then the script will check to make sure that ANY
of the bad letters are not in any words in the list or else it will remove them from the list.

Finally, it will print the results to you as well as how many results are in your query.

From my own statistical info gathering, Arise and Until are the best starting words because they use
the top 9 most used letters in the alphabet for five-letter words.
"""
from typing import Generator


def get_word_from_txt_file(word_list_file_name: str) -> list[str]:
    """
    This function basically just creates the word list. Even though the word list never really changes, I do want to
    keep reading it from the text file because it helps with creating testable code and also lets users modify their
    word lists at any time if they want.

    Paremeters:
    word_list_file_name: This is the txt file that contains your word list. Whatever it is, just make sure it's
    in the same directory as this script and contains five-letter words. PREFERABLY ONLY FIVE-LETTER-WORDS.
    If you need help, you can download the word list I supply in the GitHub repo, that's the ideal file here.

    Returns: word list without the "\n" at the end of their words.
    """
    with open(word_list_file_name) as text_file:
        # this line.strip() part here is what removes the "\n" new line character after each word.
        for line in text_file:

            # converting this to a generator function so that we can enhance memory optimization
            yield line.strip()
    

def get_whether_user_knows_letter_positions() -> bool:
    '''
    This function asks a user whether or not they know letter positions in the target word.

    Returns: True if the user knows the positions, False otherwise. 
    '''
    while True:
        
        user_knows_letter_positions = input("Do you know any letter positions in the target word? (Y/N) ").upper()

        if user_knows_letter_positions == 'Y':
            return True
        
        elif user_knows_letter_positions == 'N':
            return False

        else:
            print("I didn't quite catch that. Do you know where any letter positions are? ")


def get_how_many_letter_positions_they_know() -> int:
    '''
    This function asks the user how many letter positions in the word that they know.
    It will verify their answer is an int before returning its value as an integer.

    Returns: user-input value as an integer data type.
    '''
    while True:
        amount_of_letters_known = input("How many letter positions do you know? ")

        if amount_of_letters_known.isdigit(): 
            if 0 < int(amount_of_letters_known) < 5:
                return int(amount_of_letters_known)
            
            else:
                print("Please enter a number between 0 and 5")

        else:
            print("Please enter the number of how many letter positions you know. ")


def create_good_letters_dict() -> dict[str: int]:
    """
    This function asks for the user's input to build a dictionary of letters we know and their positions in the word.

    Returns: dictionary of good letters and their positions
    """

    good_letters_dict = {}

    while True:
        user_knows_letter_positions = get_whether_user_knows_letter_positions()

        if not user_knows_letter_positions:
            return good_letters_dict
        
        amount_of_letters_known = get_how_many_letter_positions_they_know()

        # To ensure the user does in fact know letter positions after they just said that they did. lol
        if not amount_of_letters_known:
            return good_letters_dict

        for i in range(amount_of_letters_known):

            what_letter = str(input("What letter do you know the position of? ")).lower()

            that_letters_index = int(input("Where at, in the word's position, "
                                        "is that letter located in the word? (1-5) ")) - 1

            good_letters_dict[what_letter] = that_letters_index

        return good_letters_dict


def filter_by_letters_positional(word_list: Generator[str, None, None], dictionary_of_good_letters: dict) -> list[str]:
    """
    This function takes the list of words and the dictionary of good letter objects, then filters the list of words
    to only include the good words. This algorithm's Big O(n) notation is closer to linear since it only iterates through
    each word in the list one time. My previous implementation kept iterating over the words again and again.

    Parameters:
    word_list: list of strings that are the words it will iterate through.
    dictionary_of_good_letters: dictionary object where the letters of the word are the keys and their index in
    the word are the values.
    Returns: list of words that only contain the right letters at the right positions in those words.
    """
    filtered_list = []

    for word in word_list:

        '''
        this all() list comp basically checks to make sure every letter & its position in the word
        match what should be in the target word. So say for example you know the word starts with
        g, then the dict would have an entry of {'g': 0} and it would check that word[0] == g.
        '''
        is_valid_word = all(word[position] == letter for letter, position in dictionary_of_good_letters.items())

        # we're building a new list of only words that contain all matching target letters & positions
        if is_valid_word:
            filtered_list.append(word)

    return filtered_list


def get_good_letters() -> list[str]:
    '''
    This function asks the user whether or not they know other good letters
    in the word. 

    Returns: list[str] of good_letters like this: ["a", "b", "c"]
    '''
    while True:

        user_knows_other_good_letters = False

        user_response = input('Do you know any other (yellow) letters in the word? (Y/N) ').upper()

        if user_response == 'Y':
            user_knows_other_good_letters = True

        elif user_response == 'N':
            return []

        if user_knows_other_good_letters:

            good_list_user_input = input('Enter any other letters you know that are in the word \n'
                                        '(separate letters with a comma): ')

            if not good_list_user_input:
                return []

            formatted_response = list(good_list_user_input.lower().replace(" ", ""))

            if len(formatted_response) > 5:
                print("You have entered more than 5 letters. Please enter each letter with a comma after it. "
                  "For example 'G, H, O, S, T' (Note it is not case sensitive). ")
                continue
            
            # never modify the exact thing you are iterating through
            for character in formatted_response.copy():
                if not character.isalpha():
                    formatted_response.remove(character)

            return formatted_response
        

def create_good_letter_list(good_letter_dict: dict[str, int], other_good_letters_list: list[str]) -> list[str]: 
    '''
    This function creates a good letter list, basically a list of letters
    that we know are in the word, which includes the ones that we know the positions of.
    So it's basically ALL the good letters, in the context of wordle this is all the yellow
    and green letters.

    Parameters:
    good_letter_dict: dictionary of good letters and their indexes in the target word. like {"g": 1}
    other_good_letters_dict: other list of good letters (the yellow letters in this case).
    
    Returns: list[str] a list of good letters that can be used for word filtering.
    '''
    green_letters = list(good_letter_dict.keys())

    yellow_letters = other_good_letters_list

    # combine these 2 lists into a single list. 
    # use set() to remove duplicates, then flip it back to a list

    if green_letters and yellow_letters:
        green_letters.extend(yellow_letters)
        return list(set(green_letters))

    elif green_letters and not yellow_letters:
        return green_letters
    
    elif yellow_letters and not green_letters:
        return yellow_letters
    
    else:
        return []

# in most cases they generally do, due to the nature of the game.
def get_whether_user_knows_bad_letters() -> bool:
    '''
    This function calls user input to ask whether the user knows if there 
    are any letters that are for sure not in the word (grey letters). If so, return True. 

    Returns: True if the user knows any grey letters. False otherwise. 
    '''
    while True:
        user_response = input("Do you know of any bad (grey) letters that are not in the target word? (Y/N) ").upper().strip()

        if user_response == 'Y':
            return True
        
        elif user_response == 'N':
            return False


def create_bad_letter_lists() -> list[str]:
    """
    The goal of this function is to capture user input so that we know what letters 
    the user knows are not in the word.

    Returns: list[str] list of letters that are not in the word, used for filtering word lists.
    """

    bad_list = []
    while True:

        user_knows_grey_letters = get_whether_user_knows_bad_letters()

        if user_knows_grey_letters:

            bad_list = input('Enter any letters that you know are NOT in the word - '
                            '(separate letters with a comma and space): \n').lower().replace(" ", "").split(',')

            # if the user inputs an empty string, then just make it an empty list which evaluates to False.
            if bad_list == ['']:
                bad_list = []
                return bad_list

        return bad_list


def filter_words_by_letters_non_positional(word_list: list[str], good_letters: list[str], bad_letters: list[str]) -> list[str]:
    """
    This function removes words from the original list if they contain bad letters or don't contain all the good ones.

    Parameters:
    word_list: it's the list of words we're going to search through. like ['ghost', 'flame']
    good_letters: list of good letters to compare against like if the word is ghost, and you know g and h, it
    would be ['g', 'h']
    bad_letters: list of bad letters to compare against. like if you know p and j aren't in the word, it would
    be like ['p', 'j']

    Returns: modified copy of the original word list
    """

    filtered_word_list = []

    for word in word_list:

        if good_letters and not bad_letters:

            # make sure the word list only contains words with the good letters in it
            if all(letters in word for letters in good_letters):
                filtered_word_list.append(word)

        if bad_letters:

            if not good_letters:
                
                # if not any bad letters in the word, just add it
                if not any(letters in word for letters in bad_letters):
                    if word not in filtered_word_list:
                        filtered_word_list.append(word)

            # if there are good letters in the word but also bad, then
            # we need to make sure we filter for BOTH before adding it to 
            # the word list.
            if good_letters:
                good_letters_in_word = all(letters in word for letters in good_letters)
                bad_letters_not_in_word = not any(letters in word for letters in bad_letters)

                # make sure to only add the word if it contains both the good letters
                # and not any of the bad ones
                if all([good_letters_in_word, bad_letters_not_in_word]):
                    filtered_word_list.append(word)

    return filtered_word_list


def format_list_response(filtered_list: list[str]) -> None:
    """
    This function takes our final output list and prints the results of our output in an ideal format that is
    human-readable.

    Parameters: 
    filtered_list: the final copy of the original word list, like ['ghost', 'ghoul'] (assuming you only know that
    "gho" is the first 3 letters, and no other bad letters or good letters in the word are known.
    
    Returns: None
    """

    if not filtered_list:
        print("There are no words in our word list that match this criteria. :(")
        return
    
    matching_search_string = "Your matching search results are: "
    length_of_matching_string = len(matching_search_string)

    print()
    print(length_of_matching_string * "-")
    print(matching_search_string)
    print(length_of_matching_string * "-")
    print()

    # print each word in the final list one by one on its own line.
    for word in filtered_list:
        print(word)

    number_of_items = len(filtered_list)  # number of words in the search result

    if number_of_items != 1:
        print("\nThis search has resulted in " + str(number_of_items) + " matches to your query.")  # prints number string plus var plus string
    else:
        print("\nThis search has resulted in " + str(number_of_items) + " match to your query.")


def search_again() -> bool:
    '''
    This function asks the user whether they want to start their search over or not.
    If not just stop exeuction. If so, start the process over. 

    Returns: True if user wants to start again, False otherwise. 
    '''
    while True:

        search_again = input("\nDo you want to search again? (Y/N): ").upper()

        if search_again == "Y":
            return True

        elif search_again == "N":
            return False

        else:
            print("\nI don't understand. Do you want to search again? (y/n): ")
            continue


def filter_words_main() -> None:
    """
    This function defines the order in which to run all the above functions. It serves as the primary function logic
    for the entire script.

    Parameters:
    word_list: a word list from the text file, but also, preferably a sorted word list, already sorted
    alphabetically.
    Returns: None
    """

    user_wants_to_search_again = True

    while user_wants_to_search_again:

        # alternative word list (they are pretty close in size, 
        # alt is bigger by 1k words or so)
        # word_list_text_filename = 'words_alpha_5only.txt'
        word_list_text_filename = 'official_wordle_word_list.txt'
        
        original_word_list = get_word_from_txt_file(word_list_text_filename)
        good_letter_dict = create_good_letters_dict()
        word_list = filter_by_letters_positional(original_word_list, good_letter_dict)
        other_letters = get_good_letters()
        good_list = create_good_letter_list(good_letter_dict, other_letters)
        bad_list = create_bad_letter_lists()
        word_list = filter_words_by_letters_non_positional(word_list, good_list, bad_list)
        word_list = list(set(word_list))
        word_list.sort()
        format_list_response(word_list)

        # ask if they wanna search once more
        user_wants_to_search_again = search_again()

if __name__ == "__main__":
    filter_words_main()
