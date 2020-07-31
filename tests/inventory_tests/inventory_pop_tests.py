import unittest
from src.Inventory import Inventory, Item


class InventoryPopTests(unittest.TestCase):
    def test_pop_item_from_empty_inventory_returns_none(self):
        inventory = Inventory()
        self.assertIsNone(inventory.Pop("key"))

    def test_pop_item_that_does_not_exist_returns_none(self):
        inventory = Inventory()
        inventory.Add(Item("key"))
        self.assertIsNone(inventory.Pop("gun"))

    def test_pop_item_in_inventory_returns_the_same_item(self):
        item_name = "key"
        item = Item(item_name)
        inventory = Inventory()
        inventory.Add(item)
        self.assertEqual(item, inventory.Pop(item_name))

    def test_pop_item_in_inventory_based_on_alt_name_returns_same_item(self):
        item_name = "small key"
        item = Item(item_name)
        alt_name = "key"
        item.AddAlternativeName(alt_name)

        inventory = Inventory()
        inventory.Add(item)

        self.assertEqual(item, inventory.Pop(alt_name))

    def test_pop_item_in_inventory_removes_the_item_from_inventory(self):
        item_name = "key"
        item = Item(item_name)

        inventory = Inventory()
        inventory.Add(item)

        self.assertEqual(item, inventory.Pop(item_name))
        self.assertIsNone(inventory.Pop(item_name))
        self.assertIsNone(inventory.Pop(item_name))
