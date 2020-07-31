import unittest
from src.models.Item import Item


class ItemAlternativeNamesTests(unittest.TestCase):
    def test_get_all_names_includes_name(self):
        name = "name"
        item = Item(name)
        self.assertIn(name, item.GetAllNames())

    def test_add_alternative_name_increases_all_names_list_length(self):
        name = "name 1"
        alternative_name = "name 2"
        item = Item(name)
        all_name_count = len(item.GetAllNames())

        item.AddAlternativeName(alternative_name)

        self.assertEqual(all_name_count + 1, len(item.GetAllNames()))

    def test_add_alternative_name_included_in_all_names_list(self):
        name = "name 1"
        alternative_name = "name 2"
        item = Item(name)
        self.assertNotIn(alternative_name, item.GetAllNames())

        item.AddAlternativeName(alternative_name)

        self.assertIn(alternative_name, item.GetAllNames())

    def test_add_alternative_name_does_not_add_same_name_twice(self):
        name = "name"
        item = Item(name)
        all_name_count = len(item.GetAllNames())

        item.AddAlternativeName(name)

        self.assertEqual(all_name_count, len(item.GetAllNames()))
