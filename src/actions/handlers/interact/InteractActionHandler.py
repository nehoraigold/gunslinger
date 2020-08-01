import typing
from src.actions.data_types.interaction.InteractionData import InteractionData
from src.actions.handlers.abstract.IActionHandler import IActionHandler, Action, IRoom
from src.models.Item import Item
from src.models.Player import Player
from src.utils import Print


class InteractActionHandler(IActionHandler):
    def __init__(self, player: Player):
        self.player = player

    def Handle(self, action: Action, current_room: IRoom) -> None:
        interaction_data = action.GetData()
        item = self.get_item(interaction_data, current_room)
        interaction_message = self.interact_with(item, interaction_data)
        Print.Message(interaction_message)

    def get_item(self, interaction_data: InteractionData, current_room: IRoom):
        item = current_room.GetInventory().Peek(interaction_data.GetNoun())
        if item is None:
            item = self.player.GetInventory().Peek(interaction_data.GetNoun())
        return item

    def interact_with(self, item: Item, interaction_data: InteractionData) -> str:
        if item is None:
            return "No {} found.".format(interaction_data.GetNoun())
        message = item.Interact(interaction_data.GetVerb())
        if message is None:
            message = "You cannot {} the {}.".format(interaction_data.GetVerb(), str(item))
        return message
