import unittest
from src.Inventory import Inventory, Item


class InventoryHasTests(unittest.TestCase):
    def test_empty_inventory_has_item_returns_false(self):
        inventory = Inventory()
        self.assertFalse(inventory.Has("item"))

    def test_inventory_does_not_have_item_returns_false(self):
        inventory = Inventory()
        inventory.Add(Item("small key"))
        self.assertFalse(inventory.Has("key"))

    def test_inventory_has_item_returns_true(self):
        item_name = "small key"
        item = Item(item_name)

        inventory = Inventory()
        inventory.Add(item)

        self.assertTrue(inventory.Has(item_name))

    def test_inventory_has_item_requested_with_alternate_name_returns_true(self):
        item_name = "small key"
        item = Item(item_name)
        alt_name = "key"
        item.AddAlternativeName(alt_name)

        inventory = Inventory()
        inventory.Add(item)
        self.assertTrue(inventory.Has(alt_name))

