import unittest
from src.models.Inventory import Inventory, Item


class InventoryPeekTests(unittest.TestCase):
    def test_peek_item_in_empty_inventory_returns_none(self):
        inventory = Inventory()
        self.assertIsNone(inventory.Peek("key"))

    def test_peek_item_that_does_not_exist_returns_none(self):
        inventory = Inventory()
        inventory.Add(Item("key"))
        self.assertIsNone(inventory.Peek("gun"))

    def test_peek_item_name_in_inventory_returns_item(self):
        item_name = "key"
        item = Item(item_name)
        inventory = Inventory()
        inventory.Add(item)
        self.assertEqual(item, inventory.Peek(item_name))

    def test_peek_alternative_item_name_in_inventory_returns_item(self):
        item_name = "small key"
        item = Item(item_name)
        alt_name = "key"
        item.AddAlternativeName(alt_name)

        inventory = Inventory()
        inventory.Add(item)

        self.assertEqual(item, inventory.Peek(alt_name))

    def test_peek_item_name_multiple_times_returns_same_item(self):
        item_name = "key"
        item = Item(item_name)

        inventory = Inventory()
        inventory.Add(item)

        self.assertEqual(item, inventory.Peek(item_name))
        self.assertEqual(item, inventory.Peek(item_name))
        self.assertEqual(item, inventory.Peek(item_name))
