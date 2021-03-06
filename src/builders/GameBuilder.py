import typing
import re

from src.configs.ConfigsLoader import ConfigsLoader
from src.builders.csv.CSVBlockerBuilder import IBlocker, CSVBlockerBuilder
from src.builders.csv.CSVRoomBuilder import Room, CSVRoomBuilder, IBuilder
from src.builders.csv.CSVItemBuilder import Item, CSVItemBuilder
from src.builders.csv.CSVWorldBuilder import World, CSVWorldBuilder
from src.builders.csv.CSVPlayerBuilder import Player, CSVPlayerBuilder
from src.builders.csv.CSVNonPlayableCharacterBuilder import CSVNonPlayableCharacterBuilder, INonPlayableCharacter


def BuildWorld(configs: ConfigsLoader) -> World:
    world_builder = create_builder(configs, World)
    return world_builder.Build()


def BuildPlayer(configs: ConfigsLoader) -> Player:
    player_builder = create_builder(configs, Player)
    return player_builder.Build()


def create_builder(configs: ConfigsLoader, builder_type: typing.Type) -> IBuilder:
    return SWITCHER.get(builder_type)(configs)


def create_world_builder(configs: ConfigsLoader) -> IBuilder:
    file_path = configs.Get("worldFilePath")
    for pattern, builder in WORLD_BUILDERS.items():
        if re.search(pattern, file_path):
            return builder(file_path, create_builder(configs, Room))


def create_room_builder(configs: ConfigsLoader) -> IBuilder:
    file_path = configs.Get("roomFilePath")
    for pattern, builder in ROOM_BUILDERS.items():
        if re.search(pattern, file_path):
            return builder(file_path,
                           create_builder(configs, IBlocker),
                           create_builder(configs, Item),
                           create_builder(configs, INonPlayableCharacter))


def create_blocker_builder(configs: ConfigsLoader) -> IBuilder:
    file_path = configs.Get("blockerFilePath")
    for pattern, builder in BLOCKER_BUILDERS.items():
        if re.search(pattern, file_path):
            return builder(file_path)


def create_item_builder(configs: ConfigsLoader) -> IBuilder:
    file_path = configs.Get("itemFilePath")
    for pattern, builder in ITEM_BUILDER.items():
        if re.search(pattern, file_path):
            return builder(file_path)


def create_player_builder(configs: ConfigsLoader) -> IBuilder:
    file_path = configs.Get("playerFilePath")
    for pattern, builder in PLAYER_BUILDER.items():
        if re.search(pattern, file_path):
            return builder(file_path, create_builder(configs, Item))


def create_npc_builder(configs: ConfigsLoader) -> IBuilder:
    file_path = configs.Get("npcFilePath")
    for pattern, builder in NPC_BUILDER.items():
        if re.search(pattern, file_path):
            return builder(file_path)


CSV_TYPE = r'\.csv$'
JSON_TYPE = r'\.json$'

SWITCHER = {
    World: create_world_builder,
    Room: create_room_builder,
    IBlocker: create_blocker_builder,
    Item: create_item_builder,
    Player: create_player_builder,
    INonPlayableCharacter: create_npc_builder
}

WORLD_BUILDERS = {
    CSV_TYPE: CSVWorldBuilder
}

ROOM_BUILDERS = {
    CSV_TYPE: CSVRoomBuilder
}

BLOCKER_BUILDERS = {
    CSV_TYPE: CSVBlockerBuilder
}

ITEM_BUILDER = {
    CSV_TYPE: CSVItemBuilder
}

PLAYER_BUILDER = {
    CSV_TYPE: CSVPlayerBuilder
}

NPC_BUILDER = {
    CSV_TYPE: CSVNonPlayableCharacterBuilder
}