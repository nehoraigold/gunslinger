from src.models.Player import Player
from src.configs.ConfigsLoader import ConfigsLoader
from src.actions.parsers.ActionParser import ActionParser, ParseException
from src.actions.handlers.ActionHandler import ActionHandler
from src.builders.GameBuilder import BuildWorld, BuildPlayer
from src.utils import Print


def main():
    configs = ConfigsLoader("config.json")
    world = BuildWorld(configs)
    player = BuildPlayer(configs)
    action_handler = ActionHandler(world, player)
    room = world.GetRoom(player.GetLocation())
    Print.VisitTo(room)
    room.Visit()
    while True:
        try:
            action = ActionParser.Parse(input())
            Print.NewLine()
            action_handler.Handle(action, room)
            room = world.GetRoom(player.GetLocation())
        except ParseException:
            Print.Message("Invalid action.")
            continue


if __name__ == "__main__":
    main()
