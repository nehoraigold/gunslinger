from src.actions.parsers.abstract.IActionParser import IActionParser


class QuitActionParser(metaclass=IActionParser):
    @staticmethod
    def GetWords():
        return ["quit", "exit", "q"]

    @staticmethod
    def ParseToData(string: str) -> None:
        return None
