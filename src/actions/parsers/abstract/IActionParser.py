import typing
from abc import ABCMeta


class IActionParser(ABCMeta):
    @staticmethod
    def GetWords() -> typing.List[str]:
        raise NotImplementedError

    @staticmethod
    def ParseToData(string: str) -> any:
        raise NotImplementedError
