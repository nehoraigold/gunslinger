import typing
from src.builders.abstract.IBuilder import IBuilder
from src.models.Player import Player, Inventory
from src.utils import Utils


class CSVPlayerBuilder(IBuilder):
    INNER_CELL_DELIMITER = ";"

    def __init__(self, csv_file_path, item_builder: IBuilder):
        self.csv_file_path = csv_file_path
        self.item_builder = item_builder

    def Build(self, name: str = None) -> Player:
        for i, row in enumerate(Utils.LoadCSV(self.csv_file_path)):
            if i == 0:
                continue
            return self.create_player_from_row(*row)

    def create_player_from_row(self, name: str, x_coordinate: str, y_coordinate: str, gold: str, items: str) -> Player:
        coordinate = (int(x_coordinate), int(y_coordinate))
        player_name = name.strip().capitalize()
        player = Player(coordinate, player_name if len(player_name) != 0 else "Roland")
        self.add_items_to_player_inventory(player.GetInventory(), items.split(";"))
        return player

    def add_items_to_player_inventory(self, inventory: Inventory, items: typing.List[str]) -> None:
        for item_name in items:
            inventory.Add(self.item_builder.Build(item_name.strip().lower()))
