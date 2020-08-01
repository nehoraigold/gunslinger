from src.actions.handlers.abstract.IActionHandler import IActionHandler, Action, IRoom
from src.utils import Print
from src.models.Player import Player


class DropActionHandler(IActionHandler):
    def __init__(self, player: Player):
        self.player = player

    def Handle(self, action: Action, current_room: IRoom) -> None:
        item_name = action.GetData()
        item = self.player.GetInventory().Peek(item_name)
        if item is None:
            message = "You don't have a {}.".format(item_name)
        else:
            current_room.AddItem(item)
            self.player.Drop(item)
            message = "You dropped the {}.".format(str(item))

        Print.Message(message)
