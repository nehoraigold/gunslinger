import typing
from src.builders.abstract.IBuilder import IBuilder
from src.models.environment.Room import Room, MoveDirection
from src.utils import utils


class CSVRoomBuilder(IBuilder):
    NAME_INDEX = 0
    BLOCKER_ORDER = [
        MoveDirection.UP,
        MoveDirection.DOWN,
        MoveDirection.LEFT,
        MoveDirection.RIGHT
    ]

    def __init__(self, csv_file_path: str, blocker_builder: IBuilder):
        self.csv_file_path = csv_file_path
        self.blocker_builder = blocker_builder

    def Build(self, room_name: str) -> Room:
        for row in utils.LoadCSV(self.csv_file_path):
            if room_name == row[self.NAME_INDEX]:
                return self.get_room_from_row(row)

    def get_room_from_row(self, row: typing.List[str]) -> Room:
        name, description, first_time_event, interactables, items, *blockers = tuple(row)
        room = Room(name)
        self.set_room_description(room, description)
        if any(blockers):
            self.set_room_blockers(room, blockers)
        return room

    def set_room_description(self, room: Room, description: str) -> None:
        if description and len(description.strip()) != 0:
            room.SetDescription(description)

    def set_room_blockers(self, room: Room, blockers: typing.List[str]) -> None:
        for i, blocker in enumerate(blockers):
            if len(blocker.strip()) != 0:
                blocker = self.blocker_builder.Build(blocker.strip())
                room.AddBlocker(CSVRoomBuilder.BLOCKER_ORDER[i], blocker)
