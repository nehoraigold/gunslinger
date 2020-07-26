from src.World import World
from src.Player import Player
from src.configs_loader.ConfigsLoader import ConfigsLoader
from src.actions.ActionParser import ActionParser, ParseException
from src.actions.ActionHandler import ActionHandler


def main():
    configs = ConfigsLoader("config.json")
    world = World(configs.Get("mapFilePath"), configs.Get("roomFilePath"))
    player = Player((1, 6))
    handler = ActionHandler(world, player)
    room = world.GetRoom(player.GetLocation())
    print(room.Visit())
    while True:
        try:
            action = ActionParser.Parse(input().strip())
        except ParseException:
            print("Invalid action.")
            action = None
        print()
        handler.Handle(action, room)
        room = world.GetRoom(player.GetLocation())


if __name__ == "__main__":
    main()
