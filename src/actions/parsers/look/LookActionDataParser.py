import typing
from src.actions.parsers.abstract.IActionDataParser import IActionDataParser


class LookActionDataParser(IActionDataParser):
    @staticmethod
    def GetWords() -> typing.List[str]:
        return ["look", "describe", "observe"]

    @staticmethod
    def ParseToData(string: str) -> None:
        return None
