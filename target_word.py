"""
Author: Logan Maupin

This is the script that will contain the Target Word object (class) and its subsequent properties and methods.
"""


class Target_Word:

    def __init__(self, letter_one=None, letter_two=None, letter_three=None, letter_four=None, letter_five=None, extra_letters=None):
        self.letter_one = letter_one
        self.letter_two = letter_two
        self.letter_three = letter_three
        self.letter_four = letter_four
        self.letter_five = letter_five
        self.extra_letters = extra_letters
