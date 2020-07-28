import unittest
from src.environment.Room import Room


class VisitRoomTests(unittest.TestCase):
    def test_visit_room_first_time(self):
        name = "name"
        description = "description"
        room = Room(name, description)

        first_visit_description = room.Visit()

        self.assertIn(name, first_visit_description)
        self.assertIn(description, first_visit_description)

    def test_visit_room_second_time(self):
        name = "name"
        description = "description"
        room = Room(name, description)

        room.Visit()
        second_visit_description = room.Visit()

        self.assertIn(name, second_visit_description)
        self.assertNotIn(description, second_visit_description)

    def test_visit_room_without_description(self):
        name = "name"
        room = Room(name)

        visit_description = room.Visit()

        self.assertIn(name, visit_description)
