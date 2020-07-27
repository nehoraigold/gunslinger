from src.interactables.base.Interactable import Interactable


class Item(Interactable):
    def __init__(self, name: str, description: str = None, value: int = 0):
        super().__init__(name, description)
        self.value = value

    def GetValue(self) -> int:
        return self.value

    def SetValue(self, value: int) -> None:
        self.value = value

    def IsTakeable(self) -> bool:
        return True
