import enum


class ActionType(enum.Enum):
    MOVE = "MOVE"
    LOOK = "LOOK"
    TAKE = "TAKE"
    DROP = "DROP"
    INVENTORY = "INVENTORY"
    INTERACTION = "INTERACTION"
    HELP = "HELP"
    QUIT = "QUIT"
