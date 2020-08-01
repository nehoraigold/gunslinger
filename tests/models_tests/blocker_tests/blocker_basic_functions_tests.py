import unittest
from src.models.Blocker import Blocker


class BlockerBasicFunctionsTests(unittest.TestCase):
    def test_get_block_message_returns_default_block_message(self):
        blocker = Blocker("wall")
        self.assertEqual(blocker.GetBlockMessage(), Blocker.DEFAULT_BLOCK_MESSAGE)

    def test_get_block_message_after_setting(self):
        custom_block_message = "You can't go that way!"
        blocker = Blocker("wall")
        blocker.SetBlockMessage(custom_block_message)
        self.assertEqual(blocker.GetBlockMessage(), custom_block_message)
