import unittest
from src.models.interactables.items.Item import Item


class ItemBasicFunctionsTests(unittest.TestCase):
    def test_value_initialized_at_default_value(self):
        default_value = 0
        item = Item("water canteen")
        self.assertEqual(item.GetValue(), default_value)

    def test_set_value_returns_newly_set_value(self):
        item = Item("water canteen")

        new_value = 20
        item.SetValue(new_value)

        self.assertEqual(item.GetValue(), new_value)

    def test_is_takeable_always_returns_true(self):
        item = Item("water canteen")
        self.assertTrue(item.IsTakeable())
