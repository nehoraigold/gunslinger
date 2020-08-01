import typing
from src.actions.parsers.abstract.IActionParser import IActionParser
from src.actions.data_types.interaction.InteractionData import InteractionData


class InteractActionParser(IActionParser):
    @staticmethod
    def GetWords() -> typing.List[str]:
        raise NotImplementedError("InteractActionParser: Verbs evaluated for match in ActionHandler")

    @staticmethod
    def ParseToData(string: str) -> any:
        words = string.split(' ')
        return InteractionData(words[0], " ".join(words[1:]))
