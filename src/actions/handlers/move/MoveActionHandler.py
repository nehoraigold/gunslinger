from src.actions.handlers.abstract.IActionHandler import IActionHandler, Action, IRoom
from src.models.World import World
from src.models.Player import Player, MoveDirection
from src.utils import Utils
from src.utils import Print


class MoveActionHandler(IActionHandler):
    def __init__(self, world: World, player: Player):
        self.world = world
        self.player = player

    def Handle(self, action: Action, room: IRoom) -> None:
        direction = action.GetData()
        blocker = room.GetBlocker(direction)
        if blocker is not None:
            Print.Message(blocker.GetBlockMessage())
            return
        new_room = self.get_new_room(direction)
        if new_room is not None:
            self.player.Move(direction)
            Print.VisitTo(new_room)
            new_room.Visit()

    def get_new_room(self, direction: MoveDirection):
        return self.world.GetRoom(Utils.AddCoordinates(self.player.GetLocation(), direction.value))
