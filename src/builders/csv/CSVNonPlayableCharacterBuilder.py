import typing
from src.builders.abstract.IBuilder import IBuilder
from src.utils import Utils
from src.models.npcs.abstract.NPCFactory import NPCFactory, INonPlayableCharacter


class CSVNonPlayableCharacterBuilder(IBuilder):
    INNER_CELL_DELIMITER = ";"
    NAME_INDEX = 0

    def __init__(self, csv_file_path):
        self.csv_file_path = csv_file_path

    def Build(self, npc_name: str) -> INonPlayableCharacter:
        for row in Utils.LoadCSV(self.csv_file_path):
            if npc_name == row[self.NAME_INDEX].lower():
                return self.get_npc_from_row(row)

    def get_npc_from_row(self, row: typing.List[str]) -> INonPlayableCharacter:
        name, description, alt_names, default_dialogue = tuple(row)
        npc = NPCFactory.Create(name)
        self.set_description(npc, description)
        self.set_alternative_names(npc, alt_names)
        self.set_default_dialogue(npc, default_dialogue)
        return npc

    def set_description(self, npc: INonPlayableCharacter, description: str) -> None:
        description = description.strip()
        if len(description) != 0:
            npc.SetDescription(description)

    def set_alternative_names(self, npc: INonPlayableCharacter, alternative_names: str) -> None:
        for alt_name in alternative_names.split(self.INNER_CELL_DELIMITER):
            alt_name = alt_name.strip().lower()
            if len(alt_name) != 0:
                npc.AddAlternativeName(alt_name)

    def set_default_dialogue(self, npc: INonPlayableCharacter, dialogue: str) -> None:
        npc.SetDefaultDialogue(dialogue.strip())
