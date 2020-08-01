import typing
from src.actions.parsers.abstract.IActionParser import IActionParser
from src.actions.parsers.ParseException import ParseException


class DropActionParser(IActionParser):
    @staticmethod
    def GetWords() -> typing.List[str]:
        return ["drop"]

    @staticmethod
    def ParseToData(string: str) -> any:
        try:
            return DropActionParser.get_item_name(string.split(" ")[1:])
        except IndexError:
            raise ParseException("Unable to parse take action \"{}\"".format(string))

    @staticmethod
    def get_item_name(word_list: typing.List[str]) -> str:
        words = [word.strip().lower() for word in word_list if not word.isspace()]
        if not words:
            raise ParseException("Unable to parse drop action of item with no name")
        return ' '.join(words)
