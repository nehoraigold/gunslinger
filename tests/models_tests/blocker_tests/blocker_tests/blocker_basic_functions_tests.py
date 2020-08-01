import unittest
from src.models.blockers.Blocker import Blocker


class BlockerBasicFunctionsTests(unittest.TestCase):
    def test_get_block_message_returns_default_block_message(self):
        blocker = Blocker("wall")
        self.assertEqual(blocker.GetBlockMessage(), Blocker.DEFAULT_BLOCK_MESSAGE)

    def test_get_block_message_after_setting(self):
        custom_block_message = "You can't go that way!"
        blocker = Blocker("wall")
        blocker.SetBlockMessage(custom_block_message)
        self.assertEqual(blocker.GetBlockMessage(), custom_block_message)

    def test_interact_returns_none(self):
        blocker = Blocker("wall")
        self.assertIsNone(blocker.Interact(""))
        self.assertIsNone(blocker.Interact("unlock"))
        self.assertIsNone(blocker.Interact("invalid"))

    def test_allow_always_returns_false(self):
        blocker = Blocker("wall")
        self.assertFalse(blocker.Allow())
