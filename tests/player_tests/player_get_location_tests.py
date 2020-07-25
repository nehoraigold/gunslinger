import unittest
from src.Player import Player


class PlayerGetLocationTests(unittest.TestCase):
    def test_get_initial_default_location(self):
        initial_default_location = (0, 0)
        player = Player()

        self.assertEqual(initial_default_location, player.GetLocation())

    def test_get_initial_defined_location(self):
        location = (7, 19)
        player = Player(location)

        self.assertEqual(location, player.GetLocation())
