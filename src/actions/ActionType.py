import enum


class ActionType(enum.Enum):
    MOVE = "MOVE"
    LOOK = "LOOK"
    TAKE = "TAKE"
    DROP = "DROP"
    SPEAK = "SPEAK"
    INTERACTION = "INTERACTION"
    INVENTORY = "INVENTORY"
    HELP = "HELP"
    QUIT = "QUIT"
