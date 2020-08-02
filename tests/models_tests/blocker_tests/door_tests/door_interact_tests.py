import unittest
from src.models.Item import Item
from src.models.blockers.Door import Door, Player


class DoorInteractTests(unittest.TestCase):
    def test_interact_with_words_other_than_unlock_returns_none(self):
        # Arrange
        door = Door("door")
        player = Player()

        # Act + Assert
        self.assertIsNone(door.Interact("", player))
        self.assertIsNone(door.Interact("lock", player))
        self.assertIsNone(door.Interact("invalid", player))

    def test_interact_with_no_context_returns_none(self):
        # Arrange
        door = Door("door")

        # Act + Assert
        self.assertIsNone(door.Interact(""))
        self.assertIsNone(door.Interact("lock"))
        self.assertIsNone(door.Interact("unlock"))

    def test_unlock_when_player_has_no_key_means_door_stays_locked(self):
        # Arrange
        door = Door("door")
        player = Player()

        # Act
        message = door.Interact("unlock", player)

        # Assert
        self.assertIsNotNone(message)
        self.assertFalse(door.AllowsPassage())

    def test_unlock_when_player_has_key_results_in_door_unlocked_and_key_gone(self):
        # Arrange
        door = Door("door")
        player = Player()
        player.Take(Item("small key"))

        # Act
        message = door.Interact("unlock", player)

        # Assert
        self.assertIsNotNone(message)
        self.assertTrue(door.AllowsPassage())
        self.assertIsNone(player.Has("small key"))

    def test_unlock_when_player_has_multiple_keys_only_gets_rid_of_one(self):
        # Arrange
        door = Door("door")
        player = Player()
        player.Take(Item("small key"))
        player.Take(Item("small key"))

        # Act
        door.Interact("unlock", player)

        # Assert
        self.assertIsNotNone(player.Has("small key"))
