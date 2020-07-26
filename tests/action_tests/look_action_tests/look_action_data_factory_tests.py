import unittest
from src.actions.action_data.look.LookActionDataFactory import LookActionDataFactory


class LookActionDataFactoryCreateDataTests(unittest.TestCase):
    def test_create_data_should_always_return_None(self):
        self.assertIsNone(LookActionDataFactory.CreateData(""))
        self.assertIsNone(LookActionDataFactory.CreateData("invalid string"))
        self.assertIsNone(LookActionDataFactory.CreateData("look"))
