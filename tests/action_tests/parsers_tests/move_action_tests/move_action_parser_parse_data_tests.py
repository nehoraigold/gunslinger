import unittest
from src.actions.parsers.move.MoveActionParser import MoveActionParser, MoveDirection, ParseException


class MoveActionParserParseToDataTests(unittest.TestCase):
    def test_parse_to_data_from_empty_string(self):
        with self.assertRaises(ParseException):
            MoveActionParser.ParseToData("")

    def test_parse_to_data_from_irrelevant_string(self):
        irrelevant_string = "#Faas83(%@o.0bi9}"
        with self.assertRaises(ParseException):
            MoveActionParser.ParseToData(irrelevant_string)

    def test_parse_to_data_from_single_word_but_no_direction_string(self):
        for word in MoveActionParser.MOVE_WORDS:
            with self.assertRaises(ParseException):
                MoveActionParser.ParseToData(word)

    def test_all_valid_direction_one_word_strings(self):
        valid_words = {
            MoveDirection.UP: MoveActionParser.UP_WORDS,
            MoveDirection.DOWN: MoveActionParser.DOWN_WORDS,
            MoveDirection.LEFT: MoveActionParser.LEFT_WORDS,
            MoveDirection.RIGHT: MoveActionParser.RIGHT_WORDS
        }

        for direction, words in valid_words.items():
            for word in words:
                self.assertEqual(direction, MoveActionParser.ParseToData(word))

    def test_all_valid_two_word_strings(self):
        first_words = MoveActionParser.MOVE_WORDS
        valid_words = {
            MoveDirection.UP: MoveActionParser.UP_WORDS,
            MoveDirection.DOWN: MoveActionParser.DOWN_WORDS,
            MoveDirection.LEFT: MoveActionParser.LEFT_WORDS,
            MoveDirection.RIGHT: MoveActionParser.RIGHT_WORDS
        }

        for first_word in first_words:
            for direction, second_words in valid_words.items():
                for second_word in second_words:
                    self.assertEqual(direction,
                                     MoveActionParser.ParseToData("{} {}".format(first_word, second_word)))

    def test_parse_to_data_from_relevant_two_word_string(self):
        valid_two_word_string = "go north"
        expected_direction = MoveDirection.UP

        move_action_data = MoveActionParser.ParseToData(valid_two_word_string)

        self.assertEqual(move_action_data, expected_direction)
