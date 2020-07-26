import typing
from src.actions.action_data.abstract.IActionDataFactory import IActionDataFactory


class LookActionDataFactory(IActionDataFactory):
    @staticmethod
    def GetWords() -> typing.List[str]:
        return ["look", "describe", "observe"]

    @staticmethod
    def CreateData(string: str) -> None:
        return None
