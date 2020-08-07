import typing
from src.models.npcs.NPCStateMachine import NPCState, Dialogue, Player


class KennerlyDefaultState(NPCState):
    ASK_ABOUT_TULL = "Ask about Tull"
    ASK_ABOUT_MAN_IN_BLACK = "Ask about the Man in Black"
    BOARD_YOUR_MULE = "Board your mule"
    NEVER_MIND = "Never mind"

    def __init__(self):
        self.has_met = False
        self.response_options = [self.ASK_ABOUT_TULL, self.ASK_ABOUT_MAN_IN_BLACK, self.NEVER_MIND]

    def GetDialogue(self, player: Player, selected_response: typing.Union[str, None]) -> Dialogue:
        player_has_mule = bool(player.Has("mule"))
        self.prepare_responses(player_has_mule)
        if selected_response is None:
            return self.get_conversation_starter()
        elif selected_response == self.ASK_ABOUT_MAN_IN_BLACK:
            return Dialogue('"Man in Black?" says Kennerly. "Ain\'t never heard of him."', self.response_options)
        elif selected_response == self.ASK_ABOUT_TULL:
            return Dialogue('"Not much to do \'round here, I\'m afraid. '
                            'Ya might get a burger at Sheb\'s, just west of North Main Street," Kennerly tells you.'
                            '{}'.format(' "But they won\'t let you in with a mule at yer hip."' if player_has_mule else ""),
                            self.response_options)
        else:
            return Dialogue('"Long days and pleasant nights," says Kennerly. '
                            '"If you should need me, you know where I be."')

    def get_conversation_starter(self) -> Dialogue:
        if self.has_met:
            return Dialogue('Kennerly greets you with a frown. "You\'re back," he says. '
                            '"How may I be of service?"', self.response_options)
        else:
            self.has_met = True
            return Dialogue("He eyes you up and down, his eyes full of derision. "
                            "\"G'day, sai. The name's Kennerly. What can I do ya for?\"", self.response_options)

    def prepare_responses(self, player_has_mule: bool) -> None:
        if player_has_mule and self.BOARD_YOUR_MULE not in self.response_options:
            self.response_options.insert(-1, self.BOARD_YOUR_MULE)
        elif not player_has_mule and self.BOARD_YOUR_MULE in self.response_options:
            self.response_options.remove(self.BOARD_YOUR_MULE)
