from abc import abstractmethod
from src.models.Player import Player
from src.interfaces.Interactable import Interactable


class IBlocker(Interactable):
    DEFAULT_BLOCK_MESSAGE = "You can't go that way."

    @abstractmethod
    def AllowsPassage(self, player: Player = None) -> bool:
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

    @abstractmethod
    def __repr__(self):
        raise NotImplementedError
