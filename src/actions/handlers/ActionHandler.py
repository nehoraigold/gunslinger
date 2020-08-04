from src.actions.Action import Action, ActionType
from src.actions.handlers.abstract.IActionHandler import IActionHandler, IRoom
from src.actions.handlers.inventory.InventoryActionHandler import InventoryActionHandler
from src.actions.handlers.move.MoveActionHandler import MoveActionHandler, World, Player
from src.actions.handlers.look.LookActionHandler import LookActionHandler
from src.actions.handlers.quit.QuitActionHandler import QuitActionHandler
from src.actions.handlers.talk.TalkActionHandler import TalkActionHandler
from src.actions.handlers.transfer.TransferActionHandler import TransferActionHandler
from src.actions.handlers.interact.InteractActionHandler import InteractActionHandler


class ActionHandler(IActionHandler):
    def __init__(self, world: World, player: Player):
        self.switcher = {
            ActionType.MOVE: MoveActionHandler(world, player),
            ActionType.LOOK: LookActionHandler(),
            ActionType.TRANSFER: TransferActionHandler(player),
            ActionType.TALK: TalkActionHandler(player),
            ActionType.INTERACT: InteractActionHandler(player),
            ActionType.INVENTORY: InventoryActionHandler(player),
            ActionType.QUIT: QuitActionHandler()
        }

    def Handle(self, action: Action, current_room: IRoom) -> None:
        if action is None:
            return
        handler = self.switcher.get(action.GetType(), None)
        if handler is not None:
            handler.Handle(action, current_room)
