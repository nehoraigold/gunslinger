from src.actions.handlers.abstract.IActionHandler import IActionHandler, Action, IRoom
from src.utils import Print
from sys import exit


class QuitActionHandler(IActionHandler):
    AFFIRMATIVES = ["yes", "y"]

    def Handle(self, action: Action, room: IRoom):
        confirmation = Print.GetInput("Are you sure you want to quit?")
        if confirmation in QuitActionHandler.AFFIRMATIVES:
            exit(0)
        else:
            Print.NewLine()
