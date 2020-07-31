import unittest
from src.models.Room import Room, Blocker, MoveDirection


class RoomGetAndSetBlockerTests(unittest.TestCase):
    def test_room_returns_no_blockers_if_none_set(self):
        room = Room("Room 1")

        self.assertIsNone(room.GetBlocker(MoveDirection.DOWN))
        self.assertIsNone(room.GetBlocker(MoveDirection.UP))
        self.assertIsNone(room.GetBlocker(MoveDirection.LEFT))
        self.assertIsNone(room.GetBlocker(MoveDirection.RIGHT))

    def test_blocker_returned_after_adding(self):
        room = Room("Room 1")
        blocker = Blocker("Wall")
        direction = MoveDirection.UP

        room.AddBlocker(direction, blocker)

        self.assertEqual(blocker, room.GetBlocker(direction))

    def test_blocker_overridden_when_added_in_same_direction(self):
        room = Room("Room 1")
        blocker = Blocker("Wall")
        direction = MoveDirection.UP

        room.AddBlocker(direction, blocker)

        new_blocker = Blocker("Cracked Wall")
        room.AddBlocker(direction, new_blocker)

        self.assertEqual(room.GetBlocker(direction), new_blocker)
