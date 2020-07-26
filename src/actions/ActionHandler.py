import typing
from src.Player import Player, MoveDirection
from src.World import World, Room
from src.actions.Action import Action, ActionType


class ActionHandler:
    def __init__(self, world: World, player: Player):
        self.world = world
        self.player = player
        self.switcher = {
            ActionType.MOVE: self.handle_move,
            ActionType.LOOK: self.handle_look
        }

    def Handle(self, action: Action, current_room: Room) -> None:
        if action is None:
            return
        handler = self.switcher.get(action.GetType(), None)
        if handler is not None:
            handler(action, current_room)

    def handle_move(self, action: Action, old_room: Room) -> None:
        self.player.Move(action.GetData())
        new_room = self.world.GetRoom(self.player.GetLocation())
        if new_room is None:
            opposite_direction = MoveDirection.GetOppositeDirection(action.GetData())
            self.player.Move(opposite_direction)
            new_room = old_room
        if new_room != old_room:
            print(new_room.Visit())

    @staticmethod
    def handle_look(action: Action, current_room: Room) -> None:
        print(current_room.Describe())
