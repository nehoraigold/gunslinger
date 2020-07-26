import typing
from abc import ABCMeta


class IActionDataParser(ABCMeta):
    @staticmethod
    def GetWords() -> typing.List[str]:
        raise NotImplementedError

    @staticmethod
    def ParseToData(string: str) -> any:
        raise NotImplementedError
