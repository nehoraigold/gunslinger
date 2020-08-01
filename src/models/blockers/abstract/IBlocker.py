from abc import abstractmethod
from src.models.abstract.IInteractable import IInteractable


class IBlocker(IInteractable):
    @abstractmethod
    def Allow(self) -> bool:
        raise NotImplementedError

    @abstractmethod
    def SetBlockMessage(self, block_message: str) -> None:
        raise NotImplementedError

    @abstractmethod
    def GetBlockMessage(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def Interact(self, interaction: str, context: any = None) -> str:
        raise NotImplementedError
