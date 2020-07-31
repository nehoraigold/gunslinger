import unittest
from src.actions.parsers.quit.QuitActionParser import QuitActionParser


class QuitActionParserParseToDataTests(unittest.TestCase):
    def test_data_always_returns_none(self):
        self.assertIsNone(QuitActionParser.ParseToData(""))
        self.assertIsNone(QuitActionParser.ParseToData("quit"))
        self.assertIsNone(QuitActionParser.ParseToData("invalid string"))
