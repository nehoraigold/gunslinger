import unittest
from src.Inventory import Inventory, Item


class InventorySizeTests(unittest.TestCase):
    def test_empty_inventory_has_size_zero(self):
        inventory = Inventory()
        self.assertEqual(0, inventory.Size())

    def test_size_cannot_be_less_than_zero(self):
        inventory = Inventory()
        item = Item("name")
        inventory.Add(item)

        inventory.Remove(item)
        inventory.Remove(item)
        inventory.Remove(item)
        inventory.Remove(item)

        self.assertEqual(0, inventory.Size())

    def test_adding_item_increases_inventory_size(self):
        inventory = Inventory()
        size_before_add = inventory.Size()

        inventory.Add(Item("key"))
        self.assertEqual(size_before_add + 1, inventory.Size())

    def test_removing_item_decreases_inventory_size(self):
        inventory = Inventory()
        item = Item("key")
        inventory.Add(item)
        size_before_remove = inventory.Size()

        inventory.Remove(item)
        self.assertEqual(size_before_remove - 1, inventory.Size())

    def test_popping_item_decreases_inventory_size(self):
        inventory = Inventory()
        item = Item("key")
        inventory.Add(item)
        size_before_pop = inventory.Size()

        inventory.Pop("key")
        self.assertEqual(size_before_pop - 1, inventory.Size())

    def test_peeking_item_does_not_decrease_inventory_size(self):
        inventory = Inventory()
        item = Item("key")
        inventory.Add(item)
        size_before_peek = inventory.Size()

        inventory.Peek("key")
        self.assertEqual(size_before_peek, inventory.Size())
