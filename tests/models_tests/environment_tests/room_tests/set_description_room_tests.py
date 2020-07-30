import unittest
from src.models.environment.Room import Room


class SetDescriptionRoomTests(unittest.TestCase):
    def test_set_description(self):
        room = Room("name")
        description = "description"
        self.assertNotIn(description, room.GetDescription())

        room.SetDescription(description)

        self.assertIn(description, room.GetDescription())

    def test_set_description_before_first_visit(self):
        room = Room("name")
        description = "description"

        room.SetDescription(description)

        self.assertIn(description, room.Visit())

    def test_set_description_after_first_visit(self):
        room = Room("name")
        description = "description"
        room.Visit()

        room.SetDescription(description)

        self.assertNotIn(description, room.Visit())
