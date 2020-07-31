import typing
from src.actions.parsers.abstract.IActionParser import IActionParser
from src.actions.parsers.ParseException import ParseException


class TakeActionParser(IActionParser):
    @staticmethod
    def GetWords() -> typing.List[str]:
        return ["take", "grab"]

    @staticmethod
    def ParseToData(string: str) -> any:
        try:
            return TakeActionParser.get_item_name(string.split(" ")[1])
        except IndexError:
            raise ParseException("Unable to parse take action \"{}\"".format(string))

    @staticmethod
    def get_item_name(string: str) -> str:
        item = string.strip().lower()
        if len(item) == 0:
            raise ParseException("Unable to parse take action of item with no name")
        return item
