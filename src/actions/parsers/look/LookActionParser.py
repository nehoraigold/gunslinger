import typing
from src.actions.parsers.abstract.IActionParser import IActionParser


class LookActionParser(IActionParser):
    @staticmethod
    def GetWords() -> typing.List[str]:
        return ["look", "describe", "observe"]

    @staticmethod
    def ParseToData(string: str) -> None:
        return None
