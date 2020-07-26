from src.actions.action_data.move.MoveActionDataFactory import MoveActionDataFactory
from src.actions.action_data.look.LookActionDataFactory import LookActionDataFactory
from src.actions.Action import Action, ActionType
from src.utils.ParseException import ParseException


class ActionParser:
    ACTION_DATA_FACTORIES = {
        ActionType.MOVE: MoveActionDataFactory,
        ActionType.LOOK: LookActionDataFactory
    }

    @staticmethod
    def Parse(string: str) -> Action:
        if len(string) < 1:
            raise ParseException("Unable to parse action from empty string")
        verb = ActionParser.get_first_word(string)
        for action_type, factory in ActionParser.ACTION_DATA_FACTORIES.items():
            if verb in factory.GetWords():
                return Action(action_type, factory.CreateData(string))
        raise ParseException("Unable to parse action {}".format(string))

    @staticmethod
    def get_first_word(string: str) -> str:
        return string.split(' ')[0]
