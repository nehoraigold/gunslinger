import unittest
from src.actions.move.MoveActionDataFactory import MoveActionDataFactory, MoveDirection, ParseException


class MoveActionDataFactoryCreateDataTests(unittest.TestCase):
    def test_create_data_from_empty_string(self):
        with self.assertRaises(ParseException):
            MoveActionDataFactory.CreateData("")

    def test_create_data_from_irrelevant_string(self):
        irrelevant_string = "#Faas83(%@o.0bi9}"
        with self.assertRaises(ParseException):
            MoveActionDataFactory.CreateData(irrelevant_string)

    def test_create_data_from_single_word_but_no_direction_string(self):
        for word in MoveActionDataFactory.MOVE_WORDS:
            with self.assertRaises(ParseException):
                MoveActionDataFactory.CreateData(word)

    def test_all_valid_direction_one_word_strings(self):
        valid_words = {
            MoveDirection.UP: MoveActionDataFactory.UP_WORDS,
            MoveDirection.DOWN: MoveActionDataFactory.DOWN_WORDS,
            MoveDirection.LEFT: MoveActionDataFactory.LEFT_WORDS,
            MoveDirection.RIGHT: MoveActionDataFactory.RIGHT_WORDS
        }

        for direction, words in valid_words.items():
            for word in words:
                self.assertEqual(direction, MoveActionDataFactory.CreateData(word))

    def test_all_valid_two_word_strings(self):
        first_words = MoveActionDataFactory.MOVE_WORDS
        valid_words = {
            MoveDirection.UP: MoveActionDataFactory.UP_WORDS,
            MoveDirection.DOWN: MoveActionDataFactory.DOWN_WORDS,
            MoveDirection.LEFT: MoveActionDataFactory.LEFT_WORDS,
            MoveDirection.RIGHT: MoveActionDataFactory.RIGHT_WORDS
        }

        for first_word in first_words:
            for direction, second_words in valid_words.items():
                for second_word in second_words:
                    self.assertEqual(direction,
                                     MoveActionDataFactory.CreateData("{} {}".format(first_word, second_word)))

    def test_create_data_from_relevant_two_word_string(self):
        valid_two_word_string = "go north"
        expected_direction = MoveDirection.UP

        move_action_data = MoveActionDataFactory.CreateData(valid_two_word_string)

        self.assertEqual(move_action_data, expected_direction)
