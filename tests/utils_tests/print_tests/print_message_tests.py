import unittest
from src.utils import Print


class PrintMessageTests(unittest.TestCase):
    def test_print_empty_message(self):
        empty_message = ""
        string = Print.Message(empty_message)
        self.assertEqual(empty_message, string.strip())

    def test_print_standard_message(self):
        message = "You cannot go that way."
        string = Print.Message(message)
        self.assertEqual(message, string.strip())
