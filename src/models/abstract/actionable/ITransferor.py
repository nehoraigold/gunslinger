from abc import ABCMeta, abstractmethod
from src.models.Item import Item


class ITransferor(metaclass=ABCMeta):
    @abstractmethod
    def Take(self, item: Item) -> None:
        raise NotImplementedError

    @abstractmethod
    def Drop(self, item: Item) -> None:
        raise NotImplementedError

    @abstractmethod
    def Has(self, item_name: any) -> Item:
        raise NotImplementedError
