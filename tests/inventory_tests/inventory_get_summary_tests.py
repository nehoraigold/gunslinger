import unittest
from src.Inventory import Inventory, Item


class InventoryGetSummaryTests(unittest.TestCase):
    def test_get_empty_inventory_summary_should_return_empty_dict(self):
        inventory = Inventory()
        summary = inventory.GetSummary()
        self.assertEqual(len(summary), 0)
        self.assertIsInstance(summary, dict)

    def test_get_inventory_summary_should_match_item_names(self):
        items = ["key", "canteen", "gun"]
        inventory = Inventory()
        for name in items:
            inventory.Add(Item(name))

        summary = inventory.GetSummary()

        self.assertTrue(all(name in items for name in summary.keys()))

    def test_get_summary_should_return_correct_quantity_for_single_item(self):
        items = ["key", "canteen", "gun"]
        inventory = Inventory()
        for name in items:
            inventory.Add(Item(name))

        summary = inventory.GetSummary()

        self.assertEqual(summary.get("key"), 1)

    def test_get_summary_should_return_correct_quantity_for_multiple_of_the_same_item(self):
        items = ["gun", "gun", "medicine", "gun"]
        inventory = Inventory()
        for name in items:
            inventory.Add(Item(name))

        summary = inventory.GetSummary()

        self.assertEqual(summary.get("gun"), 3)

    def test_get_summary_after_item_has_been_removed_should_not_show_item(self):
        items = ["gun", "gun", "medicine", "gun"]
        inventory = Inventory()
        for name in items:
            inventory.Add(Item(name))

        inventory.Pop("medicine")
        summary = inventory.GetSummary()

        self.assertIsNone(summary.get("medicine"))

    def test_get_summary_after_item_has_been_removed_should_decrease_quantity_by_one(self):
        items = ["gun", "gun", "medicine", "gun"]
        inventory = Inventory()
        for name in items:
            inventory.Add(Item(name))

        inventory.Pop("gun")
        summary = inventory.GetSummary()

        self.assertTrue(summary.get("gun"), 2)
