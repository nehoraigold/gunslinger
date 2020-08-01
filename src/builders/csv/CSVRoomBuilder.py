import typing
from src.builders.abstract.IBuilder import IBuilder
from src.models.Room import Room, MoveDirection
from src.utils import Utils


class CSVRoomBuilder(IBuilder):
    INNER_CELL_DELIMITER = ";"
    NAME_INDEX = 0

    def __init__(self, csv_file_path: str, blocker_builder: IBuilder, item_builder: IBuilder):
        self.csv_file_path = csv_file_path
        self.blocker_builder = blocker_builder
        self.item_builder = item_builder

    def Build(self, room_name: str) -> Room:
        for row in Utils.LoadCSV(self.csv_file_path):
            if room_name == row[self.NAME_INDEX]:
                return self.get_room_from_row(row)

    def get_room_from_row(self, row: typing.List[str]) -> Room:
        name, description, first_time_event, items, npcs, *blockers = tuple(row)
        room = Room(name)
        self.set_description(room, description)
        self.set_items(room, items)
        if any(blockers):
            self.set_blockers(room, blockers)
        return room

    def set_description(self, room: Room, description: str) -> None:
        if description and len(description.strip()) != 0:
            room.SetDescription(description)

    def set_items(self, room: Room, items: str) -> None:
        item_names = [name.strip().lower() for name in items.split(self.INNER_CELL_DELIMITER) if len(name.strip()) != 0]
        room_inventory = room.GetInventory()
        for item_name in item_names:
            room_inventory.Add(self.item_builder.Build(item_name))

    def set_blockers(self, room: Room, blockers: typing.List[str]) -> None:
        BLOCKER_ORDER = [MoveDirection.UP, MoveDirection.DOWN, MoveDirection.LEFT, MoveDirection.RIGHT]
        for i, blocker in enumerate(blockers):
            if len(blocker.strip()) != 0:
                blocker = self.blocker_builder.Build(blocker.strip())
                room.AddBlocker(BLOCKER_ORDER[i], blocker)
