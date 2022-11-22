"""
Author: Logan Maupin
Date: 11/21/2022

The purpose of this script is to test the input & output of each function to make sure the returned values are what
we want them to be.
"""

import unittest
from unittest.mock import patch
import io
from contextlib import redirect_stdout
import WordleSeeker
from WordleSeeker import *


class TestWordleSeeker(unittest.TestCase):

    def test_read_txt_file(self):
        self.assertEqual(read_txt_file("word_list_test.txt"), ["this", "is", "a", "test"])
        self.assertIsNotNone(read_txt_file("word_list_test.txt"))

    def test_create_good_letters_dict(self):
        with patch('builtins.input', side_effect=['y', '2', 'g', '1', 'h', '2']):
            self.assertEqual(create_good_letters_dict(), {'g': 0, 'h': 1})

        with patch('builtins.input', side_effect=['n']):
            self.assertEqual(create_good_letters_dict(), {})

    def test_filter_by_letters_positional(self):
        good_letters_dict = {'h': 1}
        test_word_list = ['ghost', 'shave', 'heard']
        self.assertEqual(filter_by_letters_positional(test_word_list, good_letters_dict), ['ghost', 'shave'])

    def test_create_good_and_bad_letter_lists(self):

        example_dict = {'g': 0}
        with patch('builtins.input', side_effect=['g, h, o', 'a, v']):
            good_letters, bad_letters = create_good_and_bad_letter_lists(example_dict)
            self.assertEqual(good_letters, ['g', 'h', 'o'])
            self.assertEqual(bad_letters, ['a', 'v'])

        example_dict = {}
        with patch('builtins.input', side_effect=['g, h, o', 'a, v']):
            good_letters, bad_letters = create_good_and_bad_letter_lists(example_dict)
            self.assertEqual(good_letters, ['g', 'h', 'o'])
            self.assertEqual(bad_letters, ['a', 'v'])

    def test_filter_words_by_letters_non_positional(self):

        example_word_list_to_use = ["ghost", "shave", "think", "power"]
        good_letters = ["a", "e"]
        bad_letters = ["t"]
        self.assertEqual(filter_words_by_letters_non_positional(example_word_list_to_use, good_letters, bad_letters), ["shave"])

        good_letters = ["h", "t"]
        bad_letters = []
        self.assertEqual(filter_words_by_letters_non_positional(example_word_list_to_use, good_letters, bad_letters), ["ghost", "think"])

        good_letters = []
        bad_letters = []
        self.assertEqual(filter_words_by_letters_non_positional(example_word_list_to_use, good_letters, bad_letters), example_word_list_to_use)

    def test_format_list_response(self):

        example_word_list_to_use = ["ghost", "shave", "power"]
        expected_output = "ghost\nshave\npower\nThis search has resulted in 3 matches to your query.\n"

        with io.StringIO() as fake_out, redirect_stdout(fake_out):
            WordleSeeker.format_list_response(example_word_list_to_use)
            self.assertEqual(fake_out.getvalue(), expected_output)

        example_word_list_to_use = ["ghost"]
        expected_output = "ghost\nThis search has resulted in 1 match to your query.\n"

        with io.StringIO() as fake_out, redirect_stdout(fake_out):
            WordleSeeker.format_list_response(example_word_list_to_use)
            self.assertEqual(fake_out.getvalue(), expected_output)
