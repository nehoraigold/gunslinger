from src.actions.handlers.abstract.IActionHandler import IActionHandler, Action, Room
from sys import exit


class QuitActionHandler(IActionHandler):
    AFFIRMATIVES = ["yes", "y"]

    def Handle(self, action: Action, room: Room):
        confirmation = input("Are you sure you want to quit? ")
        if confirmation.strip().lower() in QuitActionHandler.AFFIRMATIVES:
            exit(0)
        else:
            print()
