import unittest
from src.utils import Print


class PrintNewLineTests(unittest.TestCase):
    def test_print_new_line_always_prints_new_line(self):
        new_line = Print.NewLine()
        self.assertEqual(new_line, "\n")
