import typing
from src.actions.handlers.abstract.IActionHandler import IActionHandler, Action, IRoom
from src.models.Player import Player
from src.utils import Print


class InventoryActionHandler(IActionHandler):
    def __init__(self, player: Player):
        self.player = player

    def Handle(self, action: Action, room: IRoom) -> None:
        inventory_summary = self.player.GetInventorySummary()
        if len(inventory_summary) == 0:
            Print.Message("You don't have anything right now.")
        else:
            Print.Message("You have:", False)
            Print.UnorderedList(self.stringify_inventory_summary(inventory_summary))

    def stringify_inventory_summary(self, inventory_summary: typing.Dict[str, int]) -> typing.List[str]:
        inventory_list = []
        for item_name, quantity in inventory_summary.items():
            if quantity == 1:
                inventory_list.append("{} {}".format(str(quantity), item_name))
                continue
            inventory_list.append("{} {}s".format(str(quantity), item_name))
        return inventory_list
