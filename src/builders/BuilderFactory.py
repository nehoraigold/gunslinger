import typing
import re
from src.configs.ConfigsLoader import ConfigsLoader
from src.builders.csv.CSVBlockerBuilder import Blocker, CSVBlockerBuilder
from src.builders.csv.CSVRoomBuilder import Room, CSVRoomBuilder, IBuilder
from src.builders.csv.CSVInteractableBuilder import Interactable, CSVInteractableBuilder
from src.builders.csv.CSVWorldBuilder import World, CSVWorldBuilder


def Create(configs: ConfigsLoader, builder_type: typing.Type) -> IBuilder:
    return SWITCHER.get(builder_type)(configs)


def create_world_builder(configs: ConfigsLoader) -> IBuilder:
    file_path = configs.Get("worldFilePath")
    for pattern, builder in WORLD_BUILDERS.items():
        if re.search(pattern, file_path):
            return builder(file_path, Create(configs, Room))


def create_room_builder(configs: ConfigsLoader) -> IBuilder:
    file_path = configs.Get("roomFilePath")
    for pattern, builder in ROOM_BUILDERS.items():
        if re.search(pattern, file_path):
            return builder(file_path, Create(configs, Blocker))


def create_blocker_builder(configs: ConfigsLoader) -> IBuilder:
    file_path = configs.Get("blockerFilePath")
    for pattern, builder in BLOCKER_BUILDERS.items():
        if re.search(pattern, file_path):
            return builder(file_path)


def create_interactable_builder(configs: ConfigsLoader) -> IBuilder:
    file_path = configs.Get("interactableFilePath")
    for pattern, builder in INTERACTABLE_BUILDER.items():
        if re.search(pattern, file_path):
            return builder(file_path)


SWITCHER = {
    World: create_world_builder,
    Room: create_room_builder,
    Blocker: create_blocker_builder,
    Interactable: create_interactable_builder
}

CSV_TYPE = r'\.csv$'
JSON_TYPE = r'\.json$'

WORLD_BUILDERS = {
    CSV_TYPE: CSVWorldBuilder
}

ROOM_BUILDERS = {
    CSV_TYPE: CSVRoomBuilder
}

BLOCKER_BUILDERS = {
    CSV_TYPE: CSVBlockerBuilder
}

INTERACTABLE_BUILDER = {
    CSV_TYPE: CSVInteractableBuilder
}
