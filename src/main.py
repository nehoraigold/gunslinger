from src.Player import Player
from src.configs.ConfigsLoader import ConfigsLoader
from src.actions.parsers.ActionParser import ActionParser, ParseException
from src.actions.handlers.ActionHandler import ActionHandler
from src.builders.WorldBuilder import BuildWorld
from src.utils import Print


def main():
    configs = ConfigsLoader("config.json")
    world = BuildWorld(configs)
    player = Player((1, 6))
    action_handler = ActionHandler(world, player)
    room = world.GetRoom(player.GetLocation())
    Print.VisitTo(room)
    room.Visit()
    while True:
        try:
            action = ActionParser.Parse(input())
        except ParseException:
            Print.Message("Invalid action.")
            continue
        Print.NewLine()
        action_handler.Handle(action, room)
        room = world.GetRoom(player.GetLocation())


if __name__ == "__main__":
    main()
