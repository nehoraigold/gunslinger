import typing
from src.actions.parsers.abstract.IActionParser import IActionParser
from src.actions.parsers.ParseException import ParseException
from src.actions.data_types.interaction.InteractionData import InteractionData


class InteractActionParser(IActionParser):
    @staticmethod
    def GetWords() -> typing.List[str]:
        raise AttributeError("InteractActionParser: Verbs evaluated for match in InteractActionHandler!")

    @staticmethod
    def ParseToData(string: str) -> any:
        words = string.split(' ')
        if len(words) < 2:
            raise ParseException("Unable to parse interaction {}.".format(string))
        verb = words[0].lower()
        noun = " ".join(words[1:]).lower()
        return InteractionData(verb, noun)
