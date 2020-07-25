import typing
from src import Utils


class ConfigsLoader:
    def __init__(self, file_path: str):
        self.configs = Utils.load_json(file_path)

    def Get(self, key: str):
        return self.configs[key]
