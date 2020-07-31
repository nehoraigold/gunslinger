import typing
from abc import ABCMeta, abstractmethod
from src.models.interactables.items.Item import Item, Interactable
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

    @abstractmethod
    def ContainsItem(self, name: str) -> typing.Union[None, Item]:
        raise NotImplementedError

    @abstractmethod
    def RemoveItem(self, item: Item) -> None:
        raise NotImplementedError

    @abstractmethod
    def AddItem(self, item: Item) -> None:
        raise NotImplementedError
