import unittest
from src.actions.parsers.look.LookActionDataParser import LookActionDataParser


class LookActionDataParserParseToDataTests(unittest.TestCase):
    def test_parse_to_data_should_always_return_None(self):
        self.assertIsNone(LookActionDataParser.ParseToData(""))
        self.assertIsNone(LookActionDataParser.ParseToData("invalid string"))
        self.assertIsNone(LookActionDataParser.ParseToData("look"))
