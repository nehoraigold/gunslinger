import unittest
from src.actions.parsers.interact.InteractActionParser import InteractActionParser, ParseException


class TakeActionParserParseToDataTests(unittest.TestCase):
    def test_single_word_interact_action_raises_parse_exception(self):
        invalid_take_action = "word"
        with self.assertRaises(ParseException):
            InteractActionParser.ParseToData(invalid_take_action)

    def test_two_word_interact_action_results_in_first_word_verb_second_word_noun(self):
        valid_take_action = "grab key"
        verb, noun = valid_take_action.split(' ')

        data = InteractActionParser.ParseToData(valid_take_action)

        self.assertEqual(data.GetVerb(), verb)
        self.assertEqual(data.GetNoun(), noun)

    def test_more_than_two_word_interact_action_results_in_first_word_verb_rest_noun(self):
        three_word_take_action = "transfer small key"
        verb, adjective, noun = three_word_take_action.split(' ')
        noun = ' '.join([adjective, noun])

        data = InteractActionParser.ParseToData(three_word_take_action)

        self.assertEqual(data.GetVerb(), verb)
        self.assertEqual(data.GetNoun(), noun)
