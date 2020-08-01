import typing


class Item:
    EXAMINE_INTERACTION = "examine"

    def __init__(self, name: str):
        self.name = name
        self.value = 0
        self.is_transferable = False
        self.alternative_names = []
        self.interactions = {
            self.EXAMINE_INTERACTION: ""
        }

    def GetName(self) -> str:
        return self.name

    def GetDescription(self) -> str:
        return self.Interact(self.EXAMINE_INTERACTION)

    def SetDescription(self, description: str) -> None:
        self.AddInteraction(self.EXAMINE_INTERACTION, description)

    def GetValue(self) -> int:
        return self.value

    def SetValue(self, value: int) -> None:
        self.value = value

    def SetTransferability(self, is_takeable: bool) -> None:
        self.is_transferable = is_takeable

    def IsTransferable(self) -> bool:
        return self.is_transferable

    def GetAllNames(self) -> typing.List[str]:
        return [self.name] + self.alternative_names

    def AddAlternativeName(self, name: str) -> None:
        if name not in self.GetAllNames():
            self.alternative_names.append(name)

    def AddInteraction(self, interaction: str, interaction_description: str) -> None:
        self.interactions[interaction] = interaction_description

    def Interact(self, interaction: str) -> str:
        return self.interactions.get(interaction)

    def __repr__(self):
        return self.name
