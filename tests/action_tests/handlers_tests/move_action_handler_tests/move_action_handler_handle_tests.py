import unittest
from src.actions.Action import ActionType, Action
from src.actions.data_types.move.MoveDirection import MoveDirection
from src.actions.handlers.move.MoveActionHandler import MoveActionHandler, World, Player
from src.Room import Room, Blocker


class MoveActionHandlerHandleTests(unittest.TestCase):
    def setUp(self) -> None:
        self.player = Player()
        self.world = World()
        self.world.board = {
            (0, 0): Room("Room 1", "This is room 1."),
            (1, 0): Room("Room 2", "This is room 2."),
            (0, 1): Room("Room 3", "This is room 3."),
            (1, 1): Room("Room 4", "This is room 4.")
        }

        self.move_action_handler = MoveActionHandler(self.world, self.player)

    def test_handle_valid_move_action(self):
        initial_location = self.player.GetLocation()

        action = Action(ActionType.MOVE, MoveDirection.DOWN)
        self.move_action_handler.Handle(action, self.world.GetRoom(initial_location))

        ending_location = self.player.GetLocation()
        self.assertNotEqual(initial_location, ending_location)

    def test_handle_no_adjacent_room(self):
        initial_location = self.player.GetLocation()

        action = Action(ActionType.MOVE, MoveDirection.UP)
        self.move_action_handler.Handle(action, self.world.GetRoom(initial_location))

        ending_location = self.player.GetLocation()
        self.assertEqual(initial_location, ending_location)

    def test_handle_unable_to_move_in_room_with_blocker(self):
        initial_location = self.player.GetLocation()
        room = self.world.GetRoom(initial_location)

        blocker = Blocker("wall", "It's a normal, nondescript wall.")
        direction = MoveDirection.DOWN
        room.AddBlocker(direction, blocker)

        action = Action(ActionType.MOVE, direction)

        self.move_action_handler.Handle(action, room)

        ending_location = self.player.GetLocation()
        self.assertEqual(initial_location, ending_location)

    def test_handle_able_to_move_in_room_with_blocker_in_different_direction(self):
        initial_location = self.player.GetLocation()
        room = self.world.GetRoom(initial_location)

        blocker = Blocker("wall", "It's a normal, nondescript wall.")
        room.AddBlocker(MoveDirection.DOWN, blocker)

        action = Action(ActionType.MOVE, MoveDirection.RIGHT)

        self.move_action_handler.Handle(action, room)

        ending_location = self.player.GetLocation()
        self.assertNotEqual(initial_location, ending_location)