import unittest
from src.actions.parsers.look.LookActionParser import LookActionParser


class LookActionParserParseToDataTests(unittest.TestCase):
    def test_parse_to_data_should_always_return_None(self):
        self.assertIsNone(LookActionParser.ParseToData(""))
        self.assertIsNone(LookActionParser.ParseToData("look"))
        self.assertIsNone(LookActionParser.ParseToData("invalid string"))
