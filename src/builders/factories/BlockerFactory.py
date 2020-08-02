from src.builders.abstract.IFactory import IFactory
from src.models.blockers.Blocker import Blocker, IBlocker
from src.models.blockers.Door import Door
from src.models.blockers.MuleCheckpoint import MuleCheckpoint


class BlockerFactory(IFactory):
    @staticmethod
    def Create(blocker_name: str, blocker_type: str) -> IBlocker:
        blocker_type = blocker_type.lower()
        if blocker_type == "door":
            return Door(blocker_name)
        elif blocker_type == "mule checkpoint":
            return MuleCheckpoint()
        return Blocker(blocker_name)
