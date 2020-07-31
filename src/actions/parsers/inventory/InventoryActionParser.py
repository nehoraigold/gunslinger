import typing
from src.actions.parsers.abstract.IActionParser import IActionParser


class InventoryActionParser(IActionParser):
    @staticmethod
    def GetWords() -> typing.List[str]:
        return ["i", "inventory"]

    @staticmethod
    def ParseToData(string: str) -> None:
        return None
