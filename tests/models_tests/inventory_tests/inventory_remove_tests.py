import unittest
from src.models.Inventory import Inventory, Item


class InventoryRemoveTests(unittest.TestCase):
    def test_inventory_remove_nonexistent_item_returns_false(self):
        inventory = Inventory()
        item = Item("key")
        self.assertFalse(inventory.Remove(item))

    def test_inventory_remove_existing_item_once_returns_true(self):
        inventory = Inventory()
        item = Item("key")
        inventory.Add(item)

        self.assertTrue(inventory.Remove(item))

    def test_inventory_remove_same_item_multiple_times_returns_false(self):
        inventory = Inventory()
        item = Item("key")
        inventory.Add(item)

        inventory.Remove(item)
        self.assertFalse(inventory.Remove(item))
