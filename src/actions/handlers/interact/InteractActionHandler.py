import typing
from src.actions.data_types.interaction.InteractionData import InteractionData
from src.actions.handlers.abstract.IActionHandler import IActionHandler, Action, IRoom
from src.models.abstract.IInteractable import IInteractable
from src.models.Player import Player
from src.utils import Print


class InteractActionHandler(IActionHandler):
    def __init__(self, player: Player):
        self.player = player

    def Handle(self, action: Action, current_room: IRoom) -> None:
        interaction_data = action.GetData()
        interactable = self.get_interactable(interaction_data, current_room)
        interaction_message = self.interact_with(interactable, interaction_data)
        Print.Message(interaction_message)

    def get_interactable(self, interaction_data: InteractionData, current_room: IRoom) -> IInteractable:
        item = current_room.GetInventory().Peek(interaction_data.GetNoun())
        if item is None:
            item = self.player.GetInventory().Peek(interaction_data.GetNoun())
        if item is None:
            for blocker in current_room.GetAllBlockers():
                if str(blocker) == interaction_data.GetNoun():
                    item = blocker
                    break
        return item

    def interact_with(self, interactable: IInteractable, interaction_data: InteractionData) -> str:
        if interactable is None:
            return "No {} found.".format(interaction_data.GetNoun())
        message = interactable.Interact(interaction_data.GetVerb(), self.player)
        if message is None:
            message = "You cannot {} the {}.".format(interaction_data.GetVerb(), str(interactable))
        return message
