class ParseException(Exception):
    def __init__(self, description=None):
        super().__init__(description)
