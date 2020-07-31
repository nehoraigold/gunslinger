from src.actions.handlers.abstract.IActionHandler import IActionHandler, Action, IRoom


class InteractActionHandler(IActionHandler):
    def __init__(self):
        pass

    def Handle(self, action: Action, current_room: IRoom) -> None:
        raise NotImplementedError("InteractActionHandler received action with data {}".format(action.GetData()))
