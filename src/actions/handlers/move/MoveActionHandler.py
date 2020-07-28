from src.actions.handlers.abstract.IActionHandler import IActionHandler, Action, Room
from src.world.World import World
from src.Player import Player
from src.utils import utils


class MoveActionHandler(metaclass=IActionHandler):
    def __init__(self, world: World, player: Player):
        self.world = world
        self.player = player

    def Handle(self, action: Action, room: Room) -> None:
        blocker = room.GetBlocker(action.GetData())
        if blocker is not None:
            print(blocker.GetBlockMessage())
            return
        new_room = self.get_new_room(action)
        if new_room is not None:
            self.player.Move(action.GetData())
            print(new_room.Visit())

    def get_new_room(self, action: Action):
        return self.world.GetRoom(utils.AddCoordinates(self.player.GetLocation(), action.GetData().value))
