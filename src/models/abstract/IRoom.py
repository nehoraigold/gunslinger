import typing
from abc import abstractmethod
from src.interfaces.Transferor import Transferor
from src.models.blockers.abstract.IBlocker import IBlocker
from src.models.Item import Item
from src.actions.data_types.move.MoveDirection import MoveDirection


class IRoom(Transferor):
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
    def GetBlocker(self, direction: MoveDirection) -> typing.Union[None, IBlocker]:
        raise NotImplementedError

    @abstractmethod
    def GetAllBlockers(self) -> typing.List[IBlocker]:
        raise NotImplementedError

    @abstractmethod
    def AddBlocker(self, direction: MoveDirection, blocker: IBlocker) -> None:
        raise NotImplementedError

    @abstractmethod
    def Take(self, item: Item) -> None:
        raise NotImplementedError

    @abstractmethod
    def Drop(self, item: Item) -> None:
        raise NotImplementedError

    @abstractmethod
    def Has(self, item_name: str) -> Item:
        raise NotImplementedError


