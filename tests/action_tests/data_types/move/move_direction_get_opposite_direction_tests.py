import unittest
from src.actions.data_types.move.MoveDirection import MoveDirection


class MoveDirectionGetOppositeDirectionTests(unittest.TestCase):
    def test_get_opposite_direction_of_left(self):
        self.assertEqual(MoveDirection.GetOppositeDirection(MoveDirection.LEFT), MoveDirection.RIGHT)

    def test_get_opposite_direction_of_right(self):
        self.assertEqual(MoveDirection.GetOppositeDirection(MoveDirection.RIGHT), MoveDirection.LEFT)

    def test_get_opposite_direction_of_up(self):
        self.assertEqual(MoveDirection.GetOppositeDirection(MoveDirection.UP), MoveDirection.DOWN)

    def test_get_opposite_direction_of_down(self):
        self.assertEqual(MoveDirection.GetOppositeDirection(MoveDirection.DOWN), MoveDirection.UP)
