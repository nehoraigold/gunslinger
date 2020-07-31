import unittest
from src.actions.parsers.take.TakeActionParser import TakeActionParser, ParseException


class TakeActionParserParseToDataTests(unittest.TestCase):
    def test_single_word_take_action_raises_parse_exception(self):
        invalid_take_action = "take"
        with self.assertRaises(ParseException):
            TakeActionParser.ParseToData(invalid_take_action)

    def test_two_word_take_action_results_in_data_being_second_word(self):
        valid_take_action = "grab key"
        verb, noun = valid_take_action.split(' ')

        data = TakeActionParser.ParseToData(valid_take_action)

        self.assertEqual(data, noun)

    def test_more_than_two_word_take_action_joins_remaining_words(self):
        three_word_take_action = "take small key"
        verb, adjective, noun = three_word_take_action.split(' ')
        expected_data = ' '.join([adjective, noun])

        data = TakeActionParser.ParseToData(three_word_take_action)

        self.assertEqual(data, expected_data)
