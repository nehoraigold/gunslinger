import typing
from src.utils import Utils
from src.models.Inventory import Inventory, Item
from src.actions.data_types.move.MoveDirection import MoveDirection


class Player:
    def __init__(self, starting_location: typing.Tuple[int, int] = (0, 0), name: str = "Roland"):
        self.name = name
        self.coordinate = starting_location
        self.inventory = Inventory()

    def GetLocation(self) -> typing.Tuple[int, int]:
        return self.coordinate

    def GetInventory(self) -> Inventory:
        return self.inventory

    def Take(self, item: Item) -> None:
        self.inventory.Add(item)

    def Drop(self, item: Item) -> None:
        self.inventory.Remove(item)

    def Move(self, direction: MoveDirection) -> None:
        self.coordinate = Utils.AddCoordinates(self.coordinate, direction.value)
