import typing
from abc import ABCMeta, abstractmethod
from src.models.npcs.Dialogue import Dialogue
from src.models.Player import Player


class NPCState(metaclass=ABCMeta):
    @abstractmethod
    def GetDialogue(self, player: Player, selected_response: typing.Union[str, None]) -> Dialogue:
        raise NotImplementedError


class NPCStateMachine:
    def __init__(self, states: typing.List[NPCState], initial_state: NPCState):
        self.states = states
        self.state = initial_state
        self.triggers: typing.Dict[str, typing.Tuple[NPCState, NPCState]] = {}

    def AddTransition(self, trigger_response: str, from_state: typing.Type[NPCState], to_state: typing.Type[NPCState]) -> bool:
        if from_state == to_state:
            return False
        starting_state = None
        ending_state = None
        for state in self.states:
            if isinstance(state, from_state):
                starting_state = state
            if isinstance(state, to_state):
                ending_state = state
        if starting_state is None or ending_state is None:
            return False
        self.triggers[trigger_response] = (starting_state, ending_state)
        return True

    def GetDialogue(self, player: Player, selected_response: str) -> Dialogue:
        response = self.update_state(selected_response)
        return self.state.GetDialogue(player, response)

    def update_state(self, response: str) -> typing.Union[None, str]:
        for trigger, (before_state, after_state) in self.triggers.items():
            if self.state is before_state and (trigger == "*" or response == trigger):
                self.state = after_state
                return None
        return response
