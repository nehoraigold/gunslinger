from src.builders.abstract.IBuilder import IBuilder


class MockBuilder(IBuilder):
    def Build(self, name: str) -> any:
        pass
