import unittest
from src.actions.parsers.transfer.TransferActionParser import TransferActionParser, ParseException, TransferType


class TransferActionParserParseToDataTests(unittest.TestCase):
    def test_single_word_transfer_action_raises_parse_exception(self):
        invalid_transfer_action = "transfer"
        with self.assertRaises(ParseException):
            TransferActionParser.ParseToData(invalid_transfer_action)

    def test_two_word_take_action_results_in_correct_transfer_type(self):
        valid_take_action = "grab key"
        transfer_data = TransferActionParser.ParseToData(valid_take_action)
        self.assertEqual(transfer_data.GetTransferType(), TransferType.TAKE)

    def test_two_word_drop_action_results_in_correct_transfer_type(self):
        valid_take_action = "drop key"
        transfer_data = TransferActionParser.ParseToData(valid_take_action)
        self.assertEqual(transfer_data.GetTransferType(), TransferType.DROP)

    def test_two_word_take_action_results_in_correct_item_name(self):
        valid_take_action = "grab key"
        verb, item_name = valid_take_action.split(' ')

        transfer_data = TransferActionParser.ParseToData(valid_take_action)

        self.assertEqual(transfer_data.GetItemName(), item_name)

    def test_more_than_two_word_take_action_joins_remaining_words(self):
        three_word_take_action = "take small key"
        verb, adjective, noun = three_word_take_action.split(' ')
        expected_data = ' '.join([adjective, noun])

        transfer_data = TransferActionParser.ParseToData(three_word_take_action)

        self.assertEqual(transfer_data.GetItemName(), expected_data)
