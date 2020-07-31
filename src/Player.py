import typing
from src.utils import Utils
from src.Inventory import Inventory
from src.actions.data_types.move.MoveDirection import MoveDirection


class Player:
    def __init__(self, starting_location: typing.Tuple[int, int] = (0, 0), name: str = "Roland"):
        self.name = name
        self.coordinate = starting_location
        self.inventory = Inventory()

    def GetLocation(self) -> typing.Tuple[int, int]:
        return self.coordinate

    def Move(self, direction: MoveDirection) -> None:
        self.coordinate = Utils.AddCoordinates(self.coordinate, direction.value)
