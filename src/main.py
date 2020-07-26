from src.World import World
from src.Player import Player
from src.configs_loader.ConfigsLoader import ConfigsLoader
from src.actions.ActionFactory import ActionFactory, ParseException
from src.actions.ActionType import ActionType


def main():
    configs = ConfigsLoader("config.json")
    world = World(configs.Get("mapFilePath"), configs.Get("roomFilePath"))
    player = Player((1, 6))
    while True:
        room = world.GetRoom(player.GetLocation())
        print(room.Visit())
        try:
            action = ActionFactory.Create(input().strip())
        except ParseException:
            print("Invalid action.")
            action = None
        print()
        if action is None:
            continue
        if action.GetType() == ActionType.MOVE:
            player.Move(action.GetData())


if __name__ == "__main__":
    main()
