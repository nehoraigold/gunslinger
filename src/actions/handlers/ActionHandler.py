from src.actions.Action import Action, ActionType
from src.actions.handlers.abstract.IActionHandler import IActionHandler, Room
from src.actions.handlers.move.MoveActionHandler import MoveActionHandler, World, Player
from src.actions.handlers.look.LookActionHandler import LookActionHandler
from src.actions.handlers.quit.QuitActionHandler import QuitActionHandler


class ActionHandler(metaclass=IActionHandler):
    def __init__(self, world: World, player: Player):
        self.switcher = {
            ActionType.MOVE: MoveActionHandler(world, player),
            ActionType.LOOK: LookActionHandler(),
            ActionType.QUIT: QuitActionHandler()
        }

    def Handle(self, action: Action, current_room: Room) -> None:
        if action is None:
            return
        handler = self.switcher.get(action.GetType(), None)
        if handler is not None:
            handler.Handle(action, current_room)
