from src.actions.parsers.move.MoveActionDataParser import MoveActionDataParser
from src.actions.parsers.look.LookActionDataParser import LookActionDataParser
from src.actions.Action import Action, ActionType
from src.utils.ParseException import ParseException


class ActionParser:
    ACTION_DATA_FACTORIES = {
        ActionType.MOVE: MoveActionDataParser,
        ActionType.LOOK: LookActionDataParser
    }

    @staticmethod
    def Parse(string: str) -> Action:
        if len(string) < 1:
            raise ParseException("Unable to parse action from empty string")
        verb = ActionParser.get_first_word(string)
        for action_type, factory in ActionParser.ACTION_DATA_FACTORIES.items():
            if verb in factory.GetWords():
                return Action(action_type, factory.ParseToData(string))
        raise ParseException("Unable to parse action {}".format(string))

    @staticmethod
    def get_first_word(string: str) -> str:
        return string.split(' ')[0]
