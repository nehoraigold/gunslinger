import unittest
from src.models.environment.Room import Room


class NameAndDescriptionRoomTests(unittest.TestCase):
    def test_stringifying_room_returns_its_name(self):
        room_name = "Room 1"
        room = Room(room_name)
        self.assertEqual(room_name, str(room))

    def test_default_description_is_blank(self):
        room = Room("name")
        self.assertEqual(room.GetDescription(), "")

    def test_set_description(self):
        room = Room("name")
        description = "description"
        self.assertNotIn(description, room.GetDescription())

        room.SetDescription(description)

        self.assertEqual(description, room.GetDescription())

    def test_default_has_visited_returns_false(self):
        room = Room("name")
        self.assertFalse(room.HasVisited())

    def test_has_visited_after_visit_returns_true(self):
        room = Room("name")
        room.Visit()
        self.assertTrue(room.HasVisited())
