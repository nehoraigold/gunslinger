import typing
from abc import ABCMeta, abstractmethod
from src.models.interactables.blockers.Blocker import Blocker
from src.actions.data_types.move.MoveDirection import MoveDirection


class IRoom(metaclass=ABCMeta):
    @abstractmethod
    def HasVisited(self) -> bool:
        raise NotImplementedError

    @abstractmethod
    def Visit(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def GetDescription(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def SetDescription(self, description: str) -> None:
        raise NotImplementedError

    @abstractmethod
    def GetBlocker(self, direction: MoveDirection) -> typing.Union[None, Blocker]:
        raise NotImplementedError

    @abstractmethod
    def AddBlocker(self, direction: MoveDirection, blocker: Blocker) -> None:
        raise NotImplementedError
