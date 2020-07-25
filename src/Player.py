import typing
from src.actions.move.MoveDirection import MoveDirection


class Player:
    def __init__(self, starting_location: typing.Tuple[int, int] = (0, 0), name: str = "Roland",):
        self.name = name
        self.coordinate = starting_location

    def GetLocation(self) -> typing.Tuple[int, int]:
        return self.coordinate

    def Move(self, direction: MoveDirection) -> None:
        self.coordinate = (self.coordinate[0] + direction.value[0], self.coordinate[1] + direction.value[1])
