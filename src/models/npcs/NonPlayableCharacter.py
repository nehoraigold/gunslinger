import typing
from src.models.npcs.abstract.INonPlayableCharacter import INonPlayableCharacter, Dialogue
from src.models.Player import Player


class NonPlayableCharacter(INonPlayableCharacter):
    def __init__(self, name: str):
        self.name = name
        self.description = ""
        self.alternative_names = []
        self.default_dialogue = ""

    def GetName(self) -> str:
        return self.name

    def GetDescription(self) -> str:
        return self.description

    def SetDescription(self, description: str) -> None:
        self.description = description

    def GetAllNames(self) -> typing.List[str]:
        return [self.name] + self.alternative_names

    def AddAlternativeName(self, name: str) -> None:
        if name not in self.GetAllNames():
            self.alternative_names.append(name)

    def SetDefaultDialogue(self, default_dialogue: str) -> None:
        self.default_dialogue = default_dialogue

    def TalkTo(self, player: Player, dialogue: Dialogue) -> Dialogue:
        return Dialogue(self.default_dialogue)

    def __repr__(self) -> str:
        return self.name
