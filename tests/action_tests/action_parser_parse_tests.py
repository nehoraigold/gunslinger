import unittest
from src.actions.ActionParser import ActionParser, ParseException, ActionType


class ActionParserParseTests(unittest.TestCase):
    def test_parse_action_with_empty_string_input(self):
        with self.assertRaises(ParseException):
            ActionParser.Parse("")

    def test_parse_action_with_invalid_string_input(self):
        invalid_input = "invalid input"
        with self.assertRaises(ParseException):
            ActionParser.Parse(invalid_input)

    def test_parse_valid_move_action(self):
        valid_move_action = "move right"
        action = ActionParser.Parse(valid_move_action)
        self.assertEqual(action.GetType(), ActionType.MOVE)
