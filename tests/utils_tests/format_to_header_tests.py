import unittest
from src.utils import utils


class FormatToHeaderTests(unittest.TestCase):
    def test_format_to_header_empty_string(self):
        self.assertEqual(len(utils.FormatToHeader("")), 0)

    def test_format_to_header_contains_title(self):
        title = "rnag augh3ha;"
        self.assertIn(title, utils.FormatToHeader(title))

    def test_format_to_header_three_horizontal_lines(self):
        header = utils.FormatToHeader("Room Title")
        lines = header.split("\n")
        self.assertEqual(len(lines), 3)

    def test_format_to_header_equal_horizontal_line_length(self):
        header = utils.FormatToHeader("title")
        lines = header.split("\n")
        line_lengths = list(map(len, lines))
        self.assertTrue(all(each_length == line_lengths[0] for each_length in line_lengths))
