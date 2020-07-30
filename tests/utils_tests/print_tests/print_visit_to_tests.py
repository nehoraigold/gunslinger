import unittest
from src.utils import Print
from src.models.environment.Room import Room


class PrintVisitToTests(unittest.TestCase):
    def test_print_visit_to_room_contains_room_name(self):
        room = Room("name")
        message = Print.VisitTo(room)
        self.assertIn(str(room), message)

    def test_print_visit_to_room_with_empty_description_should_be_the_same_always(self):
        room = Room("name")

        first_visit_message = Print.VisitTo(room)
        room.Visit()
        second_visit_message = Print.VisitTo(room)

        self.assertEqual(first_visit_message, second_visit_message)

    def test_print_visit_to_room_with_description_contains_description_before_visited(self):
        room = Room("room")
        description = "A description of the room."
        room.SetDescription(description)

        message = Print.VisitTo(room)

        self.assertIn(description, message)

    def test_print_visit_to_room_with_description_does_not_contain_description_after_visit(self):
        room = Room("room")
        description = "A description of the room."
        room.SetDescription(description)

        room.Visit()
        message = Print.VisitTo(room)

        self.assertNotIn(description, message)

    def test_print_visit_to_room_does_not_change_visited_state(self):
        room = Room("room")
        Print.VisitTo(room)
        self.assertFalse(room.HasVisited())
