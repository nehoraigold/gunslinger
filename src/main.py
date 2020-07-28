from src.environment.World import World
from src.Player import Player
from src.configs.ConfigsLoader import ConfigsLoader
from src.actions.parsers.ActionParser import ActionParser, ParseException
from src.actions.handlers.ActionHandler import ActionHandler


def main():
    configs = ConfigsLoader("config.json")
    world = World(configs.Get("mapFilePath"), configs.Get("roomFilePath"))
    player = Player((1, 6))
    action_handler = ActionHandler(world, player)
    room = world.GetRoom(player.GetLocation())
    print(room.Visit())
    while True:
        try:
            action = ActionParser.Parse(input())
        except ParseException:
            print("Invalid action.")
            action = None
        print()
        action_handler.Handle(action, room)
        room = world.GetRoom(player.GetLocation())


if __name__ == "__main__":
    main()
