import unittest
import typing
import os
from tests.mocks.MockBuilder import MockBuilder
from src.builders.csv.CSVRoomBuilder import CSVRoomBuilder, MoveDirection
from src.models.Item import Item
from src.models.blockers.Blocker import Blocker
from tests.utils_tests.utils_tests.load_csv_tests import delete_csv_file, create_csv_file


class CSVRoomBuilderBuildTests(unittest.TestCase):
    DEFAULT_NAME = "Dungeon"
    DEFAULT_DESC = "A damp, dark dungeon. Pretty gloomy, all in all."
    DEFAULT_FIRST_TIME_EVENT = ""
    DEFAULT_GOLD = ""
    DEFAULT_INTERACTABLES = []
    DEFAULT_ITEMS = []
    DEFAULT_NPCS = []
    DEFAULT_BLOCKERS = {}

    @staticmethod
    def create_csv_row(name: str, desc: str, first_time_event: str, gold: str,
                       item_names: typing.List[str], npc_names: typing.List[str],
                       blockers: typing.Dict[MoveDirection, str]) -> typing.List[str]:
        return [name, desc, first_time_event, gold,
                '; '.join(item_names),
                '; '.join(npc_names),
                blockers.get(MoveDirection.UP, ""),
                blockers.get(MoveDirection.DOWN, ""),
                blockers.get(MoveDirection.LEFT, ""),
                blockers.get(MoveDirection.RIGHT, "")]

    def create_default_room_csv_row(self):
        return self.create_csv_row(self.DEFAULT_NAME,
                                   self.DEFAULT_DESC,
                                   self.DEFAULT_FIRST_TIME_EVENT,
                                   self.DEFAULT_GOLD,
                                   self.DEFAULT_ITEMS,
                                   self.DEFAULT_NPCS,
                                   self.DEFAULT_BLOCKERS)

    def create_room_csv_file(self, rows: typing.List[typing.List[str]]):
        header_row = ["name", "description", "first time event", "items", "npcs",
                      "blocker up", "blocker down", "blocker left", "blocker right"]
        rows.insert(0, header_row)
        create_csv_file(self.file_path, rows)

    def setUp(self) -> None:
        self.file_path = str(os.path.join(os.getcwd(), "rooms.csv"))

        self.DEFAULT_INTERACTABLES.clear()
        self.DEFAULT_ITEMS.clear()
        self.DEFAULT_BLOCKERS.clear()

        self.blocker_builder = MockBuilder()
        self.item_builder = MockBuilder()
        self.npc_builder = MockBuilder()

    def tearDown(self) -> None:
        if os.path.isfile(self.file_path):
            delete_csv_file(self.file_path)

    def test_build_room_with_only_name_and_description(self):
        self.create_room_csv_file([self.create_default_room_csv_row()])
        csv_room_builder = CSVRoomBuilder(self.file_path, self.blocker_builder, self.item_builder, self.npc_builder)
        room = csv_room_builder.Build(self.DEFAULT_NAME)

        self.assertEqual(self.DEFAULT_NAME, str(room))
        self.assertEqual(self.DEFAULT_DESC, room.GetDescription())

    def test_build_room_with_no_blockers(self):
        self.create_room_csv_file([self.create_default_room_csv_row()])

        self.blocker_builder.Build = lambda name: Blocker(name)
        csv_room_builder = CSVRoomBuilder(self.file_path, self.blocker_builder, self.item_builder, self.npc_builder)
        room = csv_room_builder.Build(self.DEFAULT_NAME)

        self.assertIsNone(room.GetBlocker(MoveDirection.UP))
        self.assertIsNone(room.GetBlocker(MoveDirection.DOWN))
        self.assertIsNone(room.GetBlocker(MoveDirection.LEFT))
        self.assertIsNone(room.GetBlocker(MoveDirection.RIGHT))

    def test_build_room_with_one_blocker(self):
        blocker_name = "wall"
        direction = MoveDirection.UP
        other_directions = [MoveDirection.DOWN, MoveDirection.LEFT, MoveDirection.RIGHT]
        self.DEFAULT_BLOCKERS[direction] = blocker_name
        self.create_room_csv_file([self.create_default_room_csv_row()])

        self.blocker_builder.Build = lambda name: Blocker(name)
        csv_room_builder = CSVRoomBuilder(self.file_path, self.blocker_builder, self.item_builder, self.npc_builder)
        room = csv_room_builder.Build(self.DEFAULT_NAME)

        self.assertEqual(blocker_name, str(room.GetBlocker(direction)))
        self.assertTrue(all([room.GetBlocker(move_direction) is None for move_direction in other_directions]))

    def test_build_room_with_multiple_blockers(self):
        self.DEFAULT_BLOCKERS[MoveDirection.UP] = "wall"
        self.DEFAULT_BLOCKERS[MoveDirection.LEFT] = "door"
        self.create_room_csv_file([self.create_default_room_csv_row()])

        self.blocker_builder.Build = lambda name: Blocker(name)
        csv_room_builder = CSVRoomBuilder(self.file_path, self.blocker_builder, self.item_builder, self.npc_builder)
        room = csv_room_builder.Build(self.DEFAULT_NAME)

        for blocker_dir, blocker_name in self.DEFAULT_BLOCKERS.items():
            self.assertEqual(str(room.GetBlocker(blocker_dir)), blocker_name)

    def test_build_room_with_no_items(self):
        self.create_room_csv_file([self.create_default_room_csv_row()])
        item_name = "small key"

        self.item_builder.Build = lambda name: Item(name)
        csv_room_builder = CSVRoomBuilder(self.file_path, self.blocker_builder, self.item_builder, self.npc_builder)
        room = csv_room_builder.Build(self.DEFAULT_NAME)

        self.assertIsNone(room.Has(item_name))

    def test_build_room_with_one_item(self):
        item_name = "small key"
        self.DEFAULT_ITEMS.append(item_name)
        self.create_room_csv_file([self.create_default_room_csv_row()])

        self.item_builder.Build = lambda name: Item(name)
        csv_room_builder = CSVRoomBuilder(self.file_path, self.blocker_builder, self.item_builder, self.npc_builder)
        room = csv_room_builder.Build(self.DEFAULT_NAME)

        item = room.Has(item_name)
        self.assertEqual(str(item), item_name)

    def test_build_room_with_multiple_items(self):
        item_name_1 = "small key"
        item_name_2 = "piano"
        self.DEFAULT_ITEMS.append(item_name_1)
        self.DEFAULT_ITEMS.append(item_name_2)
        self.create_room_csv_file([self.create_default_room_csv_row()])

        self.item_builder.Build = lambda name: Item(name)
        csv_room_builder = CSVRoomBuilder(self.file_path, self.blocker_builder, self.item_builder, self.npc_builder)
        room = csv_room_builder.Build(self.DEFAULT_NAME)

        item_1 = room.Has(item_name_1)
        self.assertEqual(str(item_1), item_name_1)
        item_2 = room.Has(item_name_2)
        self.assertEqual(str(item_2), item_name_2)

    def test_build_room_with_first_time_event(self):
        pass
