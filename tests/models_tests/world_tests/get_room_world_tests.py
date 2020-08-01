import unittest
from src.models.World import World, Room


class WorldGetRoomTests(unittest.TestCase):
    def setUp(self) -> None:
        self.board = {
            (0, 0): Room("Room1"),
            (1, 0): Room("Room2"),
            (0, 1): Room("Room3"),
            (1, 1): Room("Room4")
        }

    def test_get_valid_room_correct_name(self):
        coord = (1, 1)
        room_name = str(self.board[coord])
        world = World(self.board)

        room = world.GetRoom(coord)

        self.assertEqual(room_name, str(room))

    def test_get_room_invalid_coordinate(self):
        invalid_coord = (5, 7)

        world = World(self.board)
        room = world.GetRoom(invalid_coord)

        self.assertIsNone(room)
