## This code was created by Logan Maupin - Student at the university of Arizona Online. Studying computer science for AI & data science.

from typing import Iterable

def read_txt_file(word_list):
# open and read the dictionary txt file
    open(word_list, 'r')
    with open(word_list) as f:
        lines = f.readlines()
        return [s.strip() for s in lines]

def find_word_for(collection: list[str], char: str, index: int) -> Iterable[str]:
    for word in collection:
        if len(word)>=index-1 and word[index]==char:
            yield word

def filter_by_letter_position(original_list):
    new_list = []
    running = True
    while running:
        letter_position_question = str(input("Do you know where any of the good letters' positions are? Y/N: ")).upper()
        if letter_position_question == "Y":
            what_letter = str(input("What is the first letter you know?")).lower()
            where_is_that_letter = int(input("Where is that letter located in the word? (1-5)"))
            for word in original_list:
                if word[where_is_that_letter-1] == what_letter:
                    new_list.append(word)
            filter_by_another_letter_question = str(input("Do you know the position of another letter? Y/N: ")).upper()
            if filter_by_another_letter_question == "Y":
                original_list = new_list
                continue

            elif filter_by_another_letter_question == "N":
                break

            else:
                print("I didn't quite catch that, do you know the position of another letter? Y or N: ")

        elif letter_position_question == "N":
            break

        else:
            print("I didn't quite catch that. Do you know where any letter positions are?")
            continue


def filter_list_by_letters():
    good_list = [str(x).lower() for x in input(
        'Enter any letters you know that are in the word - (separate letters with a comma and space): \n').split(', ')]
    length_of_all_good = len(good_list)

    bad_list = [str(letters).lower() for letters in input(
        'Enter any letters that you know are NOT in the list - (separate letters with a comma and space, also if you don\'t know any bad letters just hit space and then enter):  \n').split(', ')]
    return length_of_all_good, good_list, bad_list


def return_filtered_list_by_letters(original_list, good_letters, bad_letters):
    running = True
    while running:

        filtered = []

        if len(good_letters) <= 5:
            for string in original_list:

                if all(letters in string for letters in good_letters) and not any(letters in string for letters in bad_letters):  # compare good list to master list and compare bad list to master list.
                    filtered.append(string)

                running = False

        else:  # tell the user they are a moron and to try again.
            print("Too many characters! Total of all 5 lines must be less than or equal to 5! Please try again:")
            continue

    # print the output of all words matching the str texts from the previous if (success) function
    print('\n'.join(map(str, filtered)))
    number_of_items = len(filtered)  # number of words in the search result
    if number_of_items != 1:
        print("This search has resulted in " + str(number_of_items) + " matches to your query.")  # prints number string plus var plus string
    else:
        print("This search has resulted in " + str(number_of_items) + " match to your query.")
    return filtered


def main():
    original_list = read_txt_file('words_alpha_5only.txt')
    filter_by_letter_position(original_list)
    print(len(new_list))
    print(new_list)


if __name__ == "__main__":
    main()
