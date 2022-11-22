"""
Author: Logan Maupin
Date: 11/10/2022

This script is made for the purpose of trying to provide (possible) answer solution hints to the game
Wordle.

About the game:
Wordle is a 5 letter game in which the goal is to guess five-letter words until you guess the right
word. But the game will tell you if some letters are in the word in general, or if not. If they are
in the word, the game will tell you if any of the letters in the word you guessed are in the same place
as the target word.

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

#######################################################################################################################

From my own statistical info gathering, Arise and Until are the best starting words because they use
the top 9 most used letters in the alphabet for five-letter words.
"""


def read_txt_file(word_list_file_name):
    """
    This function basically just creates the word list. Even though the word list never really changes, I do want to
    keep reading it from the text file because it helps with creating testable code and also lets users modify their
    word lists at any time if they want.

    :param word_list_file_name: This is the txt file that contains your word list. Whatever it is, just make sure it's
    in the same directory as this script and contains five-letter words. PREFERABLY ONLY FIVE-LETTER-WORDS.
    If you need help, you can download the word list I supply in the GitHub repo, that's the ideal file here.
    :returns: word list without the "\n" at the end of their words.
    """

# open and read the dictionary txt file
    with open(word_list_file_name) as text_file:
        lines = text_file.readlines()

        # this s.strip() part here is what removes the "\n" new line character after each word.
        return [line.strip() for line in lines]


def create_good_letters_dict():
    """
    This function asks for the user's input to build a dictionary of letters we know and their positions in the word.

    :returns: dictionary of good letters and their positions
    """

    good_letters_dict = {}

    running = True
    while running:
        letter_position_question = str(input("Do you know where any of the good letters' positions are? Y/N: ")).upper()

        if letter_position_question == "Y":

            amount_of_letters_known = input("How many letter positions do you know?")

            if amount_of_letters_known.isdigit():

                amount_of_letters_known = int(amount_of_letters_known)

                if 0 < amount_of_letters_known < 5:

                    for i in range(amount_of_letters_known):

                        what_letter = str(input("What letter do you know the position of?")).lower()

                        that_letters_index = int(input("Where at, in the word's position, "
                                                 "is that letter located in the word? (1-5)")) - 1

                        good_letters_dict[what_letter] = that_letters_index

                    running = False

            else:
                print("Please enter the number of how many letter positions you know.")
                continue

        elif letter_position_question == "N":
            break

        else:
            print("I didn't quite catch that. Do you know where any letter positions are?")
            continue

    return good_letters_dict


def filter_by_letters_positional(original_list: list[str], dictionary_of_good_letters: dict):

    original_list_copy = original_list.copy()

    for word in original_list:
        for key, value in dictionary_of_good_letters.items():

            current_character = word[value]
            if current_character != key:
                if word in original_list_copy:
                    original_list_copy.remove(word)

    return original_list_copy


def create_good_and_bad_letter_lists(good_letter_dict):
    """
    The goal of this function is to capture user input so that we know what letters the user knows are
    in the word and not in the word.

    :param good_letter_dict: This is the dictionary of good letter positions
    :returns: Good and bad letter list words.
    """

    while True:

        good_list = [str(x).lower() for x in input(
            'Enter any other letters you know that are in the word \n'
            'DO NOT ENTER ANY LETTERS IN THE WORD THAT YOU ALREADY LISTED ABOVE. \n'
            '(separate letters with a comma and space): \n').split(', ')]

        for letter in good_list:

            if letter in good_letter_dict:
                good_list.remove(letter)

        if len(good_list) <= 5:

            bad_list = [str(letters).lower() for letters in input(
                'Enter any letters that you know are NOT in the word - (separate letters with a comma and space, also if you don\'t know any bad letters just hit space and then enter):  \n').split(', ')]

        else:
            print("You have entered more than 5 letters. Please enter each letter with a comma after it. "
                  "For example 'G, H, O, S, T' (Note it is not case sensitive). ")

            continue

        for letter in good_letter_dict:
            good_list.append(letter)

        return good_list, bad_list


def filter_words_by_letters_non_positional(original_list, good_letters, bad_letters):
    """
    This function removes words from the original list if they contain bad letters or don't contain all the good ones.

    :param original_list: it's the list of words we're going to search through. like ['ghost', 'flame']
    :param good_letters: list of good letters to compare against like if the word is ghost, and you know g and h, it
    would be ['g', 'h']
    :param bad_letters: list of bad letters to compare against. like if you know p and j aren't in the word, it would
    be like ['p', 'j']
    :returns: modified copy of the original word list
    """

    original_list_copy = original_list.copy()

    for word in original_list:

        if not all(letters in word for letters in good_letters):
            original_list_copy.remove(word)

        elif any(letters in word for letters in bad_letters):  # compare good list to master list and compare bad list to master list.
            original_list_copy.remove(word)

    return original_list_copy


def format_list_response(filtered_list):
    """
    This function takes our final output list and prints the results of our output in an ideal format that is
    human-readable.
    :param filtered_list: the final copy of the original word list, like ['ghost', 'ghoul'] (assuming you only know that
    "gho" is the first 3 letters, and no other bad letters or good letters in the word are known.
    :returns: None
    """

    # print each word in the final list one by one on its own line.
    for word in filtered_list:
        print(word)

    number_of_items = len(filtered_list)  # number of words in the search result

    if number_of_items != 1:
        print("This search has resulted in " + str(number_of_items) + " matches to your query.")  # prints number string plus var plus string
    else:
        print("This search has resulted in " + str(number_of_items) + " match to your query.")


def main():
    """
    This function defines the order to run all the other functions in this script.
    If you want to know how this works, please read the top part of this script that explains the process of what the
    code is doing.

    :returns: None
    """

    original_list = read_txt_file('words_alpha_5only.txt')

    good_letter_dict = create_good_letters_dict()

    original_list = filter_by_letters_positional(original_list, good_letter_dict)

    good_list, bad_list = create_good_and_bad_letter_lists(good_letter_dict)

    original_list = filter_words_by_letters_non_positional(original_list, good_list, bad_list)

    format_list_response(original_list)


if __name__ == "__main__":
    main()
