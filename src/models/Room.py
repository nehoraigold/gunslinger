import typing
from src.Inventory import Inventory, Item
from src.models.abstract.IRoom import IRoom, MoveDirection, Blocker


class Room(IRoom):
    def __init__(self, name: str):
        self.name: str = name
        self.description: str = ""
        self.has_visited: bool = False
        self.blockers: typing.Dict[MoveDirection, Blocker] = {}
        self.items: Inventory = Inventory()

    def HasVisited(self) -> bool:
        return self.has_visited

    def Visit(self) -> None:
        self.has_visited = True

    def GetDescription(self) -> str:
        return self.description

    def SetDescription(self, description: str) -> None:
        self.description = description

    def GetBlocker(self, direction: MoveDirection) -> typing.Union[None, Blocker]:
        return self.blockers.get(direction, None)

    def AddBlocker(self, direction: MoveDirection, blocker: Blocker) -> None:
        self.blockers[direction] = blocker

    def ContainsItem(self, name: str) -> typing.Union[None, Item]:
        return self.items.Peek(name)

    def AddItem(self, item: Item) -> None:
        self.items.Add(item)

    def RemoveItem(self, item: Item) -> None:
        self.items.Remove(item)

    def __repr__(self) -> str:
        return self.name
