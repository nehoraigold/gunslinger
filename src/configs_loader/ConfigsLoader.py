import typing
from src.utils import utils


class ConfigsLoader:
    def __init__(self, file_path: str):
        self.configs = utils.LoadJSON(file_path)

    def Get(self, key: str):
        return self.configs[key]
