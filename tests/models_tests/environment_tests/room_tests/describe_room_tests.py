import unittest
from src.models.environment.Room import Room


class DescribeRoomTests(unittest.TestCase):
    def test_describe_room(self):
        name = "name"
        description = "description"
        room = Room(name, description)

        self.assertTrue(description in room.Describe())
