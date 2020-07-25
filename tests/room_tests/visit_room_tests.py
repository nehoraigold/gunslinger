import unittest
from src.Room import Room


class VisitRoomTests(unittest.TestCase):
    def test_visit_room_first_time(self):
        name = "name"
        description = "description"
        room = Room(name, description)

        first_visit_description = room.Visit()
        self.assertTrue(name in first_visit_description and description in first_visit_description)

    def test_visit_room_second_time(self):
        name = "name"
        description = "description"
        room = Room(name, description)

        room.Visit()
        second_visit_description = room.Visit()
        self.assertTrue(name in second_visit_description and description not in second_visit_description)
