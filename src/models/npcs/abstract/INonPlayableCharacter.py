import typing
from abc import abstractmethod
from src.interfaces.Talker import Talker, Dialogue
from src.models.Player import Player


class INonPlayableCharacter(Talker):
    @abstractmethod
    def GetName(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def GetDescription(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def SetDescription(self, description: str) -> None:
        raise NotImplementedError

    @abstractmethod
    def GetAllNames(self) -> typing.List[str]:
        raise NotImplementedError

    @abstractmethod
    def AddAlternativeName(self, name: str) -> None:
        raise NotImplementedError

    @abstractmethod
    def SetDefaultDialogue(self, default_dialogue: str) -> None:
        raise NotImplementedError

    @abstractmethod
    def TalkTo(self, player: Player, dialogue: Dialogue) -> Dialogue:
        raise NotImplementedError

    @abstractmethod
    def __repr__(self) -> str:
        raise NotImplementedError
