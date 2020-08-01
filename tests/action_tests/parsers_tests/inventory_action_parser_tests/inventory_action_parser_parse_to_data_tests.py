import unittest
from src.actions.parsers.inventory.InventoryActionParser import InventoryActionParser


class InventoryActionParserParseToDataTests(unittest.TestCase):
    def test_data_always_returns_none(self):
        self.assertIsNone(InventoryActionParser.ParseToData(""))
        self.assertIsNone(InventoryActionParser.ParseToData("inventory"))
        self.assertIsNone(InventoryActionParser.ParseToData("invalid string"))
