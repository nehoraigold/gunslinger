import typing
from src.utils import Utils


class ConfigsLoader:
    def __init__(self, file_path: str):
        self.configs = Utils.LoadJSON(file_path)

    def Get(self, key: str):
        return self.configs[key]
