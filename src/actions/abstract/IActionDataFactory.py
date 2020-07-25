import typing
from abc import ABCMeta


class IActionDataFactory(ABCMeta):
    @staticmethod
    def GetWords() -> typing.List[str]:
        raise NotImplementedError

    @staticmethod
    def CreateData(string: str):
        raise NotImplementedError
