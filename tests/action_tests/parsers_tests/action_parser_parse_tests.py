import unittest
from src.actions.parsers.ActionParser import ActionParser, ParseException, ActionType


class ActionParserParseTests(unittest.TestCase):
    def test_parse_action_with_empty_string_input(self):
        with self.assertRaises(ParseException):
            ActionParser.Parse("")

    def test_parse_action_with_unknown_string_input_returns_interact_action_by_default(self):
        invalid_input = "invalid input"
        action = ActionParser.Parse(invalid_input)
        self.assertEqual(action.GetType(), ActionType.INTERACT)

    def test_parse_valid_move_action(self):
        valid_move_action = "move right"
        action = ActionParser.Parse(valid_move_action)
        self.assertEqual(action.GetType(), ActionType.MOVE)

    def test_parse_valid_look_action(self):
        valid_look_action = "look"
        action = ActionParser.Parse(valid_look_action)
        self.assertEqual(action.GetType(), ActionType.LOOK)

    def test_parse_valid_quit_action(self):
        valid_quit_action = "q"
        action = ActionParser.Parse(valid_quit_action)
        self.assertEqual(action.GetType(), ActionType.QUIT)

    def test_parse_valid_transfer_action(self):
        valid_take_action = "grab item"
        action = ActionParser.Parse(valid_take_action)
        self.assertEqual(action.GetType(), ActionType.TRANSFER)
