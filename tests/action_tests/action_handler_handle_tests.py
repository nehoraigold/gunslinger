import unittest
from src.actions.ActionHandler import ActionHandler, World, Player, Room, Action, ActionType, MoveDirection


class ActionHandlerHandleTests(unittest.TestCase):
    def setUp(self) -> None:
        self.player = Player()
        self.world = World()
        self.world.board = {
            (0, 0): Room("Room 1", "This is room 1."),
            (1, 0): Room("Room 2", "This is room 2."),
            (0, 1): Room("Room 3", "This is room 3."),
            (1, 1): Room("Room 4", "This is room 4.")
        }

        self.handler = ActionHandler(self.world, self.player)

    def test_handle_valid_move_action(self):
        pre_move_room = self.world.GetRoom(self.player.GetLocation())

        action = Action(ActionType.MOVE, MoveDirection.DOWN)
        self.handler.Handle(action, pre_move_room)
        post_move_room = self.world.GetRoom(self.player.GetLocation())

        self.assertNotEqual(pre_move_room, post_move_room)

    def test_handle_invalid_move_action(self):
        pre_move_room = self.world.GetRoom(self.player.GetLocation())

        action = Action(ActionType.MOVE, MoveDirection.UP)
        self.handler.Handle(action, pre_move_room)
        post_move_room = self.world.GetRoom(self.player.GetLocation())

        self.assertEqual(pre_move_room, post_move_room)
