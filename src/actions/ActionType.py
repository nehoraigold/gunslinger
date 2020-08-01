import enum


class ActionType(enum.Enum):
    MOVE = "MOVE"
    LOOK = "LOOK"
    TRANSFER = "TRANSFER"
    SPEAK = "SPEAK"
    UNLOCK = "UNLOCK"
    INTERACT = "INTERACT"
    INVENTORY = "INVENTORY"
    HELP = "HELP"
    QUIT = "QUIT"
