import typing
from src.models.npcs.NPCStateMachine import NPCState, Player, Dialogue


class KennerlyBoardMuleState(NPCState):
    YES_RESPONSE = "Yes"
    NO_RESPONSE = "No"

    def __init__(self, board_mule_price: int):
        self.board_mule_price = board_mule_price

    def GetDialogue(self, player: Player, selected_response: typing.Union[str, None]) -> Dialogue:
        if selected_response is None:
            return Dialogue('"Stayin\' two nights, are ya?" Kennerly says. "That\'ll cost ya two gold pieces. '
                            'I reckon that shouldn\'t be a problem for you, Mr. Shoot-Up Money. Sound good?"',
                            [self.YES_RESPONSE, self.NO_RESPONSE])
        elif selected_response == self.YES_RESPONSE:
            return self.try_board_mule(player)
        elif selected_response == self.NO_RESPONSE:
            return Dialogue('"Keep the mule with ya, if ya wish," says Kennerly. '
                            '"But no place in town will let you in with a mule at yer hip."')

    def try_board_mule(self, player: Player) -> Dialogue:
        if player.Has("mule"):
            if player.gold >= self.board_mule_price:
                return Dialogue('You hand over two gold pieces and your mule. "Thanks kindly," says Kennerly.')
            return Dialogue('Kennerly sneers at you. "Don\'t have the gold, partner? Tough luck."')
        else:
            return Dialogue('"Ya tryin\' to pull one on me, bud?" asks Kennerly. "Where\'s the mule?"')


