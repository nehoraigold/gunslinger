import typing


class Interactable:
    def __init__(self, name: str, description: str = None):
        self.name = name
        self.description = description
        self.alternative_names = []
        self.interactions = {
            "examine": self.description
        }

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

    def AddInteraction(self, interaction: str, interaction_description: str) -> None:
        self.interactions[interaction] = interaction_description

    def Interact(self, interaction: str) -> str:
        return self.interactions.get(interaction, "You cannot {} the {}.".format(interaction, self.name))

    def IsTakeable(self):
        return False

    def __repr__(self):
        return self.name
