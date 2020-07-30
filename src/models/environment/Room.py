import typing
from src.utils import Utils
from src.models.environment.abstract.IRoom import IRoom, MoveDirection, Blocker


class Room(IRoom):
    def __init__(self, name: str):
        self.name = name
        self.description = ""
        self.has_visited = False
        self.blockers = {}

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

    def __repr__(self) -> str:
        return self.name
