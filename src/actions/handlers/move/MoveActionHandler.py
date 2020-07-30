from src.actions.handlers.abstract.IActionHandler import IActionHandler, Action, Room
from src.models.environment.World import World
from src.Player import Player
from src.utils import Utils
from src.utils import Print


class MoveActionHandler(IActionHandler):
    def __init__(self, world: World, player: Player):
        self.world = world
        self.player = player

    def Handle(self, action: Action, room: Room) -> None:
        blocker = room.GetBlocker(action.GetData())
        if blocker is not None:
            Print.Message(blocker.GetBlockMessage())
            return
        new_room = self.get_new_room(action)
        if new_room is not None:
            self.player.Move(action.GetData())
            Print.VisitTo(new_room)
            new_room.Visit()

    def get_new_room(self, action: Action):
        return self.world.GetRoom(Utils.AddCoordinates(self.player.GetLocation(), action.GetData().value))
