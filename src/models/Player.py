import typing
from src.utils import Utils
from src.interfaces.Transferor import Transferor
from src.interfaces.Talker import Talker, Dialogue
from src.models.Inventory import Inventory, Item
from src.actions.data_types.move.MoveDirection import MoveDirection


class Player(Transferor, Talker):
    def __init__(self, starting_location: typing.Tuple[int, int] = (0, 0), name: str = "Roland"):
        self.name = name
        self.gold = 0
        self.coordinate = starting_location
        self.inventory = Inventory()

    def GetLocation(self) -> typing.Tuple[int, int]:
        return self.coordinate

    def Take(self, item: Item) -> None:
        if str(item) == "gold":
            self.gold += item.GetValue()
        else:
            self.inventory.Add(item)

    def Drop(self, item: Item) -> None:
        self.inventory.Remove(item)

    def Has(self, item_name: str) -> Item:
        return self.inventory.Peek(item_name)

    def GetInventorySummary(self) -> typing.Dict[str, int]:
        summary = {"gold coin": self.gold}
        summary.update(self.inventory.GetSummary())
        return summary

    def Move(self, direction: MoveDirection) -> None:
        self.coordinate = Utils.AddCoordinates(self.coordinate, direction.value)

    def TalkTo(self, talker: Talker, dialogue: Dialogue) -> Dialogue:
        raw_input = input()
        try:
            selection = int(raw_input) - 1
        except ValueError:
            selection = None
        dialogue.SetPlayerSelection(selection)
        return dialogue

    def __repr__(self):
        return self.name
