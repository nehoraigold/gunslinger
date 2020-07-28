from src.actions.parsers.move.MoveActionParser import MoveActionParser
from src.actions.parsers.look.LookActionParser import LookActionParser
from src.actions.parsers.quit.QuitActionParser import QuitActionParser
from src.actions.parsers.ParseException import ParseException
from src.actions.Action import Action, ActionType


class ActionParser:
    PARSERS = {
        ActionType.MOVE: MoveActionParser,
        ActionType.LOOK: LookActionParser,
        ActionType.QUIT: QuitActionParser
    }

    @staticmethod
    def Parse(string: str) -> Action:
        if len(string) < 1:
            raise ParseException("Unable to parse action from empty string")
        string = string.strip().lower()
        verb = ActionParser.get_first_word(string)
        for action_type, parser in ActionParser.PARSERS.items():
            if verb in parser.GetWords():
                return Action(action_type, parser.ParseToData(string))
        raise ParseException("Unable to parse action {}".format(string))

    @staticmethod
    def get_first_word(string: str) -> str:
        return string.split(' ')[0]
