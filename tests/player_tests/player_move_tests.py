import unittest
import typing
from src.Player import Player, MoveDirection


class PlayerMoveTests(unittest.TestCase):
    def base_test_move(self,
                       starting_location: typing.Tuple[int, int],
                       ending_location: typing.Tuple[int, int],
                       direction: MoveDirection):
        player = Player(starting_location)
        player.Move(direction)
        self.assertEqual(ending_location, player.GetLocation())

    def test_move_up(self):
        starting_location = (1, 3)
        location_after_move = (starting_location[0], starting_location[1] - 1)
        self.base_test_move(starting_location, location_after_move, MoveDirection.UP)

    def test_move_down(self):
        starting_location = (7, 2)
        location_after_move = (starting_location[0], starting_location[1] + 1)
        self.base_test_move(starting_location, location_after_move, MoveDirection.DOWN)

    def test_move_right(self):
        starting_location = (3, 9)
        location_after_move = (starting_location[0] + 1, starting_location[1])
        self.base_test_move(starting_location, location_after_move, MoveDirection.RIGHT)

    def test_move_left(self):
        starting_location = (4, 5)
        location_after_move = (starting_location[0] - 1, starting_location[1])
        self.base_test_move(starting_location, location_after_move, MoveDirection.LEFT)
