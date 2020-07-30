import unittest
from src.utils import Utils


class AddCoordinatesTests(unittest.TestCase):
    def test_add_one_coordinate_returns_same_coordinate(self):
        coordinate = (3, 2)
        self.assertEqual(Utils.AddCoordinates(coordinate), coordinate)

    def test_add_two_coordinates(self):
        coordinate_1 = (1, 2)
        coordinate_2 = (2, 4)
        expected_result = (coordinate_1[0] + coordinate_2[0], coordinate_1[1] + coordinate_2[1])

        self.assertEqual(Utils.AddCoordinates(coordinate_1, coordinate_2), expected_result)

    def test_add_negative_coordinates(self):
        coordinate_1 = (-3, 4)
        coordinate_2 = (4, -7)
        expected_result = (coordinate_1[0] + coordinate_2[0], coordinate_1[1] + coordinate_2[1])

        self.assertEqual(Utils.AddCoordinates(coordinate_1, coordinate_2), expected_result)

    def test_add_more_than_two_coordinates(self):
        coordinate_1 = (2, -3)
        coordinate_2 = (1, 2)
        coordinate_3 = (-3, 1)
        expected_result = (0, 0)

        self.assertEqual(Utils.AddCoordinates(coordinate_1, coordinate_2, coordinate_3), expected_result)
