import typing
from src.models.interactables.items.Item import Item


class Inventory:
    def __init__(self):
        self.items = []

    def Has(self, name: str) -> bool:
        return any([name in item.GetAllNames() for item in self.items])

    def Add(self, item: Item) -> None:
        self.items.append(item)

    def Peek(self, name: str) -> typing.Union[None, Item]:
        for item in self.items:
            if name in item.GetAllNames():
                return item
        return None

    def Pop(self, name: str) -> typing.Union[None, Item]:
        item = self.Peek(name)
        if item:
            self.Remove(item)
        return item

    def Remove(self, item: Item) -> bool:
        try:
            self.items.remove(item)
            return True
        except ValueError:
            return False

    def Size(self):
        return len(self.items)
