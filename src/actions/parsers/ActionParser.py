from src.actions.parsers.move.MoveActionParser import MoveActionParser
from src.actions.parsers.look.LookActionParser import LookActionParser
from src.actions.parsers.take.TakeActionParser import TakeActionParser
from src.actions.parsers.quit.QuitActionParser import QuitActionParser
from src.actions.parsers.interact.InteractActionParser import InteractActionParser
from src.actions.parsers.ParseException import ParseException
from src.actions.Action import Action, ActionType


class ActionParser:
    PARSERS = {
        ActionType.MOVE: MoveActionParser,
        ActionType.LOOK: LookActionParser,
        ActionType.TAKE: TakeActionParser,
        ActionType.QUIT: QuitActionParser
    }

    @staticmethod
    def Parse(string: str) -> Action:
        if len(string.strip()) < 1:
            raise ParseException("Unable to parse action from empty string")
        return ActionParser.get_action(string.strip().lower())

    @staticmethod
    def get_action(string: str) -> Action:
        verb = ActionParser.get_first_word(string)
        for action_type, parser in ActionParser.PARSERS.items():
            if verb in parser.GetWords():
                return Action(action_type, parser.ParseToData(string))
        return Action(ActionType.INTERACT, InteractActionParser.ParseToData(string))

    @staticmethod
    def get_first_word(string: str) -> str:
        return string.split(' ')[0]
