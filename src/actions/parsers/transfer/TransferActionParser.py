import typing
from src.actions.parsers.abstract.IActionParser import IActionParser
from src.actions.parsers.ParseException import ParseException
from src.actions.data_types.transfer.TransferData import TransferData, TransferType


class TransferActionParser(IActionParser):
    TAKE_WORDS = ["take", "grab"]
    DROP_WORDS = ["drop"]

    @staticmethod
    def GetWords() -> typing.List[str]:
        return TransferActionParser.TAKE_WORDS + TransferActionParser.DROP_WORDS

    @staticmethod
    def ParseToData(string: str) -> any:
        try:
            return TransferActionParser.create_transfer_data(string)
        except IndexError:
            raise ParseException("Unable to parse transfer action \"{}\"".format(string))

    @staticmethod
    def create_transfer_data(string: str) -> TransferData:
        words = string.split(" ")
        transfer_type = TransferActionParser.get_transfer_type(words[0])
        item_name = TransferActionParser.get_item_name(words[1:])
        return TransferData(transfer_type, item_name)

    @staticmethod
    def get_transfer_type(verb: str) -> TransferType:
        if verb in TransferActionParser.TAKE_WORDS:
            return TransferType.TAKE
        elif verb in TransferActionParser.DROP_WORDS:
            return TransferType.DROP
        else:
            raise ParseException("Unable to parse transfer action '{}'".format(verb))

    @staticmethod
    def get_item_name(word_list: typing.List[str]) -> str:
        words = [word.strip().lower() for word in word_list if not word.isspace()]
        if not words:
            raise ParseException("Unable to parse transfer action of item with no name")
        return ' '.join(words)
