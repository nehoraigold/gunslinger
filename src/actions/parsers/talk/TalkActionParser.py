import typing
from src.actions.parsers.abstract.IActionParser import IActionParser
from src.actions.parsers.ParseException import ParseException


class TalkActionParser(IActionParser):
    @staticmethod
    def GetWords() -> typing.List[str]:
        return ["talk", "speak"]

    @staticmethod
    def ParseToData(string: str) -> str:
        return TalkActionParser.get_noun(string)

    @staticmethod
    def get_noun(string: str) -> str:
        words = TalkActionParser.remove_connector_words(string)
        if len(words) < 2:
            raise ParseException("Unable to parse talk action '{}'".format(string))
        noun = " ".join(words[1:])
        return noun

    @staticmethod
    def remove_connector_words(string):
        CONNECTOR_WORDS = ["to", "with"]
        return [word for word in string.split(" ") if word not in CONNECTOR_WORDS]
