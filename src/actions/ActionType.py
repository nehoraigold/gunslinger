import enum


class ActionType(enum.Enum):
    MOVE = "MOVE"
    LOOK = "LOOK"
    TRANSFER = "TRANSFER"
    SPEAK = "SPEAK"
    INTERACT = "INTERACT"
    INVENTORY = "INVENTORY"
    HELP = "HELP"
    QUIT = "QUIT"
