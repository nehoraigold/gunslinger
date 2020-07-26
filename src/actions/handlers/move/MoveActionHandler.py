from src.actions.handlers.abstract.IActionHandler import IActionHandler, Action, Room
from src.actions.data_types.move.MoveDirection import MoveDirection
from src.World import World
from src.Player import Player


class MoveActionHandler(metaclass=IActionHandler):
    def __init__(self, world: World, player: Player):
        self.world = world
        self.player = player

    def Handle(self, action: Action, old_room: Room) -> None:
        self.player.Move(action.GetData())
        new_room = self.world.GetRoom(self.player.GetLocation())
        if new_room is None:
            opposite_direction = MoveDirection.GetOppositeDirection(action.GetData())
            self.player.Move(opposite_direction)
            new_room = old_room
        if new_room != old_room:
            print(new_room.Visit())
