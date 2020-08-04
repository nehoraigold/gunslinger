import typing
from src.models.Inventory import Inventory, Item
from src.models.npcs.abstract.INonPlayableCharacter import INonPlayableCharacter
from src.models.abstract.IRoom import IRoom, MoveDirection, IBlocker


class Room(IRoom):
    def __init__(self, name: str):
        self.name: str = name
        self.description: str = ""
        self.has_visited: bool = False
        self.blockers: typing.Dict[MoveDirection, IBlocker] = {}
        self.inventory: Inventory = Inventory()
        self.npcs: typing.List[INonPlayableCharacter] = []

    def HasVisited(self) -> bool:
        return self.has_visited

    def Visit(self) -> None:
        self.has_visited = True

    def GetDescription(self) -> str:
        return self.description

    def SetDescription(self, description: str) -> None:
        self.description = description

    def GetBlocker(self, direction: MoveDirection) -> typing.Union[None, IBlocker]:
        return self.blockers.get(direction)

    def GetAllBlockers(self) -> typing.List[IBlocker]:
        return list(self.blockers.values())

    def AddBlocker(self, direction: MoveDirection, blocker: IBlocker) -> None:
        self.blockers[direction] = blocker

    def AddNonPlayableCharacter(self, npc: INonPlayableCharacter) -> None:
        if npc.GetName() not in [character.GetName() for character in self.npcs]:
            self.npcs.append(npc)

    def GetNonPlayableCharacter(self, npc_name: str) -> typing.Union[INonPlayableCharacter, None]:
        for character in self.npcs:
            if npc_name.lower() in [name.lower() for name in character.GetAllNames()]:
                return character
        return None

    def Take(self, item: Item) -> None:
        self.inventory.Add(item)

    def Drop(self, item: Item) -> None:
        self.inventory.Remove(item)

    def Has(self, item_name: str) -> Item:
        return self.inventory.Peek(item_name)

    def __repr__(self) -> str:
        return self.name
