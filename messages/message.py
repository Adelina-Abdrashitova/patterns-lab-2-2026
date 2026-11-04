from interfaces import BaseMessage


class Message(BaseMessage):
    def __init__(self, text: str) -> None:
        self._text = text

    def render(self) -> str:
        return self._text
