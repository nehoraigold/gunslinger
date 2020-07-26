import unittest
from src.actions.Action import Action, ActionType
from src.actions.data_types.move.MoveDirection import MoveDirection


class ActionTests(unittest.TestCase):
    def test_get_type(self):
        action_type = ActionType.LOOK
        action = Action(action_type)

        self.assertEqual(action.GetType(), action_type)
        self.assertIsNone(action.GetData())

    def test_get_random_string_data(self):
        action_type = ActionType.LOOK
        action_data = "random data"

        action = Action(action_type, action_data)

        self.assertEqual(action.GetData(), action_data)

    def test_get_move_action_data(self):
        action_type = ActionType.MOVE
        action_data = MoveDirection.LEFT

        action = Action(action_type, action_data)

        self.assertEqual(action.GetData(), action_data)

    def test_get_look_action_data(self):
        action = Action(ActionType.LOOK)
        self.assertIsNone(action.GetData())
