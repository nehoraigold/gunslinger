import typing
from src.utils import utils
from src.room.abstract.IRoom import IRoom, MoveDirection, Blocker


class Room(IRoom):
    def __init__(self, name: str, description: str = None):
        self.name = name
        self.description = description
        self.has_visited = False
        self.blockers = {}

    def Visit(self) -> str:
        visit_description = self.get_name()
        if not self.has_visited:
            visit_description += self.get_description()
            self.has_visited = True
        return visit_description

    def Describe(self) -> str:
        return self.get_description()

    def SetDescription(self, description: str) -> None:
        self.description = description

    def GetBlocker(self, direction: MoveDirection) -> typing.Union[None, Blocker]:
        return self.blockers.get(direction, None)

    def AddBlocker(self, direction: MoveDirection, blocker: Blocker) -> None:
        self.blockers[direction] = blocker

    def get_name(self) -> str:
        return "{}\n".format(utils.FormatToHeader(self.name))

    def get_description(self) -> str:
        return "{}\n".format(self.description) if self.description is not None and len(self.description) > 0 else ""

    def __repr__(self) -> str:
        return self.name
