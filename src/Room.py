class Room:
    def __init__(self, name: str, description: str = None):
        self.name = name
        self.description = description
        self.has_visited = False

    def Visit(self):
        visit_desc = self.get_name()
        if not self.has_visited:
            visit_desc += self.get_description()
            self.has_visited = True
        return visit_desc

    def Describe(self):
        return self.get_description()

    def SetDescription(self, description: str):
        self.description = description

    def get_name(self):
        return "{}\n".format(self.name)

    def get_description(self) -> str:
        return "{}\n".format(self.description)

    def __str__(self):
        return self.name
