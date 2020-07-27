import unittest
from src.interactables.items.Item import Item, Interactable


class ItemIsInteractableTests(unittest.TestCase):
    def test_item_inherits_from_interactable(self):
        item = Item("item")
        self.assertTrue(isinstance(item, Interactable))
