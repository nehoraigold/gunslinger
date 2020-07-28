import unittest
from src.world.World import World
from tests.utils_tests.load_csv_tests import create_csv_file, delete_csv_file


class WorldGetRoomTests(unittest.TestCase):
    def setUp(self) -> None:
        self.map_file_path = "tests/world_tests/world_map.csv"
        self.room_descriptions_file_path = "tests/world_tests/room_desc.csv"
        self.map_data = [["Room1", "Room2"],
                         ["Room3", "Room4"]]
        self.room_descriptions_data = [["Room1", "Description for room 1."],
                                       ["Room2", "Description for room 2."],
                                       ["Room3", "Description for room 3."],
                                       ["Room4", "Description for room 4."]]
        create_csv_file(self.map_file_path, self.map_data)
        create_csv_file(self.room_descriptions_file_path, self.room_descriptions_data)

    def tearDown(self) -> None:
        delete_csv_file(self.map_file_path)
        delete_csv_file(self.room_descriptions_file_path)

    def test_get_valid_room_correct_name(self):
        coord = (1, 1)
        room_name = self.map_data[coord[0]][coord[1]]
        world = World(self.map_file_path, self.room_descriptions_file_path)

        room = world.GetRoom(coord)

        self.assertEqual(room_name, str(room))

    def test_get_valid_room_correct_description(self):
        coord = (1, 0)
        description = self.room_descriptions_data[1][1]

        world = World(self.map_file_path, self.room_descriptions_file_path)
        room = world.GetRoom(coord)

        self.assertIn(description, room.Describe())

    def test_get_room_invalid_coordinate(self):
        invalid_coord = (5, 7)

        world = World(self.map_file_path, self.room_descriptions_file_path)
        room = world.GetRoom(invalid_coord)

        self.assertIsNone(room)
