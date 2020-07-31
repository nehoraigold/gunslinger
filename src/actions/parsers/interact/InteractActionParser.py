import typing
from src.actions.parsers.abstract.IActionParser import IActionParser


class InteractActionParser(IActionParser):
    @staticmethod
    def GetWords() -> typing.List[str]:
        raise NotImplementedError("InteractActionParser: Verbs evaluated for match in ActionHandler")

    @staticmethod
    def ParseToData(string: str) -> any:
        words = string.split(' ')
        return {"verb": words[0], "args": words[1:]}
