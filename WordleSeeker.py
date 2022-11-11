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
When you run this script, it will ask you if you know any of the letters in the word, and any letters
that you know are NOT in the word. From there, if you do know any letters in the word, we need to know
how many letters' positions that you know and what those letters are in those positions.

From my own statistical info gathering, Arise and Until are the best starting words because they use
the top 9 most used letters in the alphabet for 5 letter words.

"""

from typing import Iterable


def read_txt_file(word_list):
# open and read the dictionary txt file
    open(word_list, 'r')
    with open(word_list) as f:
        lines = f.readlines()
        return [s.strip() for s in lines]


# def find_word_for(collection: list[str], char: str, index: int) -> Iterable[str]:
#     for word in collection:
#         if len(word)>=index-1 and word[index]==char:
#             yield word


def create_good_letter_dictionary(original_list: list[str]):
    good_letters_dict = {}

    original_list_copy= original_list.copy()

    running = True
    while running:
        letter_position_question = str(input("Do you know where any of the good letters' positions are? Y/N: ")).upper()

        if letter_position_question == "Y":

            we_know_this_many_letters = input("How many letter positions do you know?")

            if we_know_this_many_letters.isdigit():

                we_know_this_many_letters = int(we_know_this_many_letters)

                if 1 < we_know_this_many_letters < 5:

                    for i in range(we_know_this_many_letters):

                        what_letter = str(input("What letter do you know the position of?")).lower()

                        that_letters_index = int(input("Where at, in the word's position, "
                                                 "is that letter located in the word? (1-5)")) - 1

                        good_letters_dict[what_letter] = that_letters_index

                        for i in range(len(original_list)):
                            if original_list[i][that_letters_index] != what_letter:
                                original_list_copy.remove(original_list[i])

                    running = False

            else:
                print("Please enter the number of how many letter positions you know.")
                continue

        elif letter_position_question == "N":
            break

        else:
            print("I didn't quite catch that. Do you know where any letter positions are?")
            continue

    return original_list_copy, good_letters_dict


def create_good_and_bad_letter_lists(good_letter_dict):
    """
    The goal of this function is to capture user input so that we know what letters the user knows are
    in the word and not in the word.

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

    original_list_copy = original_list.copy()

    for word in original_list:

        if not all(letters in word for letters in good_letters):
            original_list_copy.remove(word)

        elif any(letters in word for letters in bad_letters):  # compare good list to master list and compare bad list to master list.
            original_list_copy.remove(word)

    return original_list_copy


def filter_words_by_letters_positional(original_list, good_letter_dict):

    original_list_copy= original_list.copy()

    running = True
    while running:

        if good_letter_dict:

            for key in good_letter_dict:

                for word in original_list:

                    if key != word[good_letter_dict[key]]:

                        original_list_copy.remove(word)

            running = False

        else:

            running = False

    return original_list_copy


def format_list_response(filtered_list):

    # print the output of all words matching the str texts from the previous if (success) function
    for word in filtered_list:
        print(word)

    number_of_items = len(filtered_list)  # number of words in the search result

    if number_of_items != 1:
        print("This search has resulted in " + str(number_of_items) + " matches to your query.")  # prints number string plus var plus string
    else:
        print("This search has resulted in " + str(number_of_items) + " match to your query.")


def main():
    # original_list = read_txt_file('words_alpha_5only.txt')
    original_list = ['adept', 'adios', 'flame', 'fired', 'bears', 'ghost', 'agate']

    print(len(original_list))

    original_list, good_letter_dict = create_good_letter_dictionary(original_list)
    print(len(original_list))
    good_list, bad_list = create_good_and_bad_letter_lists(good_letter_dict)
    original_list = filter_words_by_letters_non_positional(original_list, good_list, bad_list)

    print(len(original_list))

    print("--------------------------------------------------------")
    final_list = filter_words_by_letters_positional(original_list, good_letter_dict)
    format_list_response(final_list)


if __name__ == "__main__":
    main()
