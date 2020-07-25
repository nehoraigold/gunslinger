from src.actions.move.MoveActionDataFactory import MoveActionDataFactory
from src.actions.Action import Action, ActionType
from src.utils.ParseException import ParseException


class ActionFactory:
    ACTION_DATA_FACTORIES = {
        ActionType.MOVE: MoveActionDataFactory
    }

    @staticmethod
    def Create(string: str) -> Action:
        if len(string) < 1:
            raise ParseException("Unable to parse action from empty string")
        verb = ActionFactory.get_first_word(string)
        for action_type, factory in ActionFactory.ACTION_DATA_FACTORIES.items():
            if verb in factory.GetWords():
                return Action(action_type, factory.CreateData(string))
        raise ParseException("Unable to parse action {}".format(string))

    @staticmethod
    def get_first_word(string: str) -> str:
        return string.split(' ')[0]
