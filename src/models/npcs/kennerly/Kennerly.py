from src.models.npcs.NonPlayableCharacter import NonPlayableCharacter, Player, Dialogue
from src.models.npcs.NPCStateMachine import NPCStateMachine
from src.models.npcs.kennerly.KennerlyDefaultState import KennerlyDefaultState
from src.models.npcs.kennerly.KennerlyBoardMuleState import KennerlyBoardMuleState


class Kennerly(NonPlayableCharacter):
    BOARD_MULE_PRICE = 2

    def __init__(self):
        super(Kennerly, self).__init__("Kennerly")
        self.state = NPCStateMachine([KennerlyDefaultState(), KennerlyBoardMuleState(self.BOARD_MULE_PRICE)], KennerlyDefaultState)
        self.state.AddTransition(KennerlyDefaultState.BOARD_YOUR_MULE, KennerlyDefaultState, KennerlyBoardMuleState)
        self.state.AddTransition("*", KennerlyBoardMuleState, KennerlyDefaultState)

    def TalkTo(self, player: Player, dialogue: Dialogue) -> Dialogue:
        response = None if dialogue.GetPlayerSelection() is not int else dialogue.GetResponseOptions()[dialogue.GetPlayerSelection()]
        return self.state.GetDialogue(player, response)
