import typing
from src.models.abstract.IWorld import IWorld, Room


class World(IWorld):
    def __init__(self, board: typing.Dict[typing.Tuple[int, int], Room]):
        self.board = board

    def GetRoom(self, coordinate: typing.Tuple[int, int]) -> typing.Union[None, Room]:
        return self.board.get(coordinate, None)
