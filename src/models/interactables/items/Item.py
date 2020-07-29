from src.models.interactables.Interactable import Interactable


class Item(Interactable):
    def __init__(self, name: str):
        super().__init__(name)
        self.value = 0

    def GetValue(self) -> int:
        return self.value

    def SetValue(self, value: int) -> None:
        self.value = value

    def IsTakeable(self) -> bool:
        return True
