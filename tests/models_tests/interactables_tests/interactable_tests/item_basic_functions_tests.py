import unittest
from src.models.Item import Item


class ItemBasicFunctionsTests(unittest.TestCase):
    def test_get_name_empty_string(self):
        empty_string = ""
        item = Item(empty_string)
        self.assertEqual(item.GetName(), empty_string)

    def test_get_name_normal_string(self):
        normal_string = "piano"
        item = Item(normal_string)
        self.assertEqual(item.GetName(), normal_string)

    def test_string_repr_returns_name(self):
        name = "piano"
        item = Item(name)
        self.assertEqual(str(item), name)

    def test_get_description_default_value_is_empty_string(self):
        item = Item("piano")
        self.assertEqual(item.GetDescription(), "")

    def test_set_description_normal_string(self):
        item = Item("piano")

        description = "An old, worn-out piano."
        item.SetDescription(description)

        self.assertEqual(item.GetDescription(), description)

    def test_is_takeable_always_returns_false(self):
        item = Item("piano")
        self.assertFalse(item.IsTakeable())

    def test_value_initialized_at_default_value(self):
        default_value = 0
        item = Item("water canteen")
        self.assertEqual(item.GetValue(), default_value)

    def test_set_value_returns_newly_set_value(self):
        item = Item("water canteen")

        new_value = 20
        item.SetValue(new_value)

        self.assertEqual(item.GetValue(), new_value)

    def test_is_takeable_is_false_by_default(self):
        item = Item("water canteen")
        self.assertFalse(item.IsTakeable())

    def test_is_takeable_changes_after_set_takeability(self):
        item = Item("water canteen")
        item.SetTakeability(True)
        self.assertTrue(item.IsTakeable())
