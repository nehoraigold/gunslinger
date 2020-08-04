import typing


class Dialogue:
    def __init__(self, message: str = "", response_options: typing.List[str] = None, player_selection: int = None):
        self.message = message
        self.response_options = response_options
        self.player_selection = player_selection

    def GetNPCResponse(self) -> str:
        return self.message

    def GetResponseOptions(self) -> typing.Union[typing.List[str]]:
        return self.response_options

    def GetPlayerSelection(self) -> typing.Union[None, int]:
        return self.player_selection

    def SetPlayerSelection(self, player_selection: int):
        self.player_selection = player_selection
