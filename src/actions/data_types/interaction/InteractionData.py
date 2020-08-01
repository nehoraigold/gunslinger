import typing


class InteractionData:
    def __init__(self, verb: str, noun: str):
        self.verb = verb
        self.noun = noun

    def GetVerb(self) -> str:
        return self.verb

    def GetNoun(self) -> str:
        return self.noun
