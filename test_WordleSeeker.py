"""
Author: Logan Maupin
Date: 11/21/2022

The purpose of this script is to test the input & output of each function to make sure the returned values are what
we want them to be.
"""

import unittest
from unittest.mock import patch

from WordleSeeker import *

class TestWordleSeeker(unittest.TestCase):

    def test_read_txt_file(self):
        self.assertEqual("word_list_test.txt", ["this", "is", "a", "test"])
        self.assertIsNotNone(read_txt_file("word_list_test.txt"))

    def test_filter_by_letters_positional(self):
        word_list = ["ghost", "think"]
