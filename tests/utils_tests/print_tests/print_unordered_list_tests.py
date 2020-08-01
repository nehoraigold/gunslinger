import unittest
from src.utils import Print

class PrintUnorderedListTests(unittest.TestCase):
    def test_empty_list_returns_empty_string(self):
        message = Print.UnorderedList([])
        self.assertEqual("", message)

    def test_printed_message_contains_the_list_item(self):
        list_item = "item one"
        message = Print.UnorderedList([list_item])
        self.assertIn(list_item, message)

    def test_printed_message_uses_custom_bullets(self):
        list_item = "item one"
        custom_bullet = "==>"
        message = Print.UnorderedList([list_item], 1, custom_bullet)
        self.assertIn(custom_bullet, message)

    def test_printed_message_uses_right_number_of_tabs(self):
        list_item = "item one"
        number_of_tabs = 2
        message = Print.UnorderedList([list_item], number_of_tabs)
        self.assertIn("\t" * number_of_tabs, message)

    def test_list_stays_in_same_order(self):
        list_items = ["one", "two", "three"]
        message = Print.UnorderedList(list_items)
        self.assertTrue(message.find(list_items[2]) > message.find(list_items[1]) > message.find(list_items[0]))
