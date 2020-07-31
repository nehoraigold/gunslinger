import typing
from src.actions.handlers.abstract.IActionHandler import IActionHandler, Action, IRoom
from src.utils import Print
from src.Player import Player


class TakeActionHandler(IActionHandler):
    def __init__(self, player: Player):
        self.player = player

    def Handle(self, action: Action, current_room: IRoom) -> None:
        item_name = action.GetData()
        item = current_room.ContainsItem(item_name)
        if item is None:
            message = "There is no {} for you to take.".format(item_name)
        elif not item.IsTakeable():
            message = "You cannot take the {}.".format(str(item))
        else:
            current_room.RemoveItem(item)
            self.player.Take(item)
            message = "You took the {}.".format(str(item))

        Print.Message(message)
