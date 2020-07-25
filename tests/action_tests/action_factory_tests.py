import unittest
from src.actions.ActionFactory import ActionFactory, ParseException, ActionType


class ActionFactoryCreateTests(unittest.TestCase):
    def test_create_action_with_empty_string_input(self):
        with self.assertRaises(ParseException):
            ActionFactory.Create("")

    def test_create_action_with_invalid_string_input(self):
        invalid_input = "invalid input"
        with self.assertRaises(ParseException):
            ActionFactory.Create(invalid_input)

    def test_create_valid_move_action(self):
        valid_move_action = "move right"
        action = ActionFactory.Create(valid_move_action)
        self.assertEqual(action.GetType(), ActionType.MOVE)
