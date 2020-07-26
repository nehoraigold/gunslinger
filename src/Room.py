from src.utils import utils


class Room:
    def __init__(self, name: str, description: str = None):
        self.name = name
        self.description = description
        self.has_visited = False

    def Visit(self) -> str:
        visit_description = self.get_name()
        if not self.has_visited:
            visit_description += self.get_description()
            self.has_visited = True
        return visit_description

    def Describe(self) -> str:
        return self.get_description()

    def SetDescription(self, description: str):
        self.description = description

    def get_name(self) -> str:
        return "{}\n".format(utils.FormatToHeader(self.name))

    def get_description(self) -> str:
        return "{}\n".format(self.description) if self.description is not None and len(self.description) > 0 else ""

    def __repr__(self) -> str:
        return self.name
