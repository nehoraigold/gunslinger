import unittest
from src.actions.parsers.drop.DropActionParser import DropActionParser, ParseException


class TakeActionParserParseToDataTests(unittest.TestCase):
    def test_single_word_drop_action_raises_parse_exception(self):
        invalid_take_action = "drop"
        with self.assertRaises(ParseException):
            DropActionParser.ParseToData(invalid_take_action)

    def test_two_word_drop_action_results_in_data_being_second_word(self):
        valid_take_action = "drop key"
        verb, noun = valid_take_action.split(' ')

        data = DropActionParser.ParseToData(valid_take_action)

        self.assertEqual(data, noun)

    def test_more_than_two_word_drop_action_joins_remaining_words(self):
        three_word_take_action = "drop small key"
        verb, adjective, noun = three_word_take_action.split(' ')
        expected_data = ' '.join([adjective, noun])

        data = DropActionParser.ParseToData(three_word_take_action)

        self.assertEqual(data, expected_data)
