import typing


class Interactable:
    INTERACTION_NOT_FOUND_DESCRIPTION = "You cannot {} the {}."
    EXAMINE_INTERACTION = "examine"

    @staticmethod
    def GetInteractionNotFoundDescription(interaction: str, interactable: "Interactable") -> str:
        return Interactable.INTERACTION_NOT_FOUND_DESCRIPTION.format(interaction, str(interactable))

    def __init__(self, name: str):
        self.name = name
        self.description = ""
        self.alternative_names = []
        self.interactions = {
            self.EXAMINE_INTERACTION: self.description
        }

    def GetName(self) -> str:
        return self.name

    def GetDescription(self) -> str:
        return self.description

    def SetDescription(self, description: str) -> None:
        self.description = description
        self.AddInteraction(self.EXAMINE_INTERACTION, self.description)

    def GetAllNames(self) -> typing.List[str]:
        return [self.name] + self.alternative_names

    def AddAlternativeName(self, name: str) -> None:
        if name not in self.GetAllNames():
            self.alternative_names.append(name)

    def AddInteraction(self, interaction: str, interaction_description: str) -> None:
        self.interactions[interaction] = interaction_description

    def Interact(self, interaction: str) -> str:
        return self.interactions.get(interaction, self.GetInteractionNotFoundDescription(interaction, self))

    def IsTakeable(self) -> bool:
        return False

    def __repr__(self):
        return self.name
