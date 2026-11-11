"""
Базовый Decorator и конкретные декораторы необходимо реализовать самостоятельно.

Подсказка: все декораторы должны удовлетворять интерфейсу BaseMessage и
работать с другим объектом BaseMessage через композицию.
"""

# TODO:
# - MessageDecorator
# - HeaderDecorator
# - SignatureDecorator
# - DateDecorator
# - Base64Decorator

import base64
from interfaces import BaseMessage


class MessageDecorator(BaseMessage):
    """Базовый декоратор"""
    def __init__(self, message: BaseMessage) -> None:
        self._message = message

    def render(self) -> str:
        return self._message.render()


class HeaderDecorator(MessageDecorator):
    """Конкретный декоратор: добавляет заголовок перед сообщением"""
    def __init__(self, message: BaseMessage, header: str) -> None:
        super().__init__(message)
        self.header = header

    def render(self) -> str:
        return self.header + self._message.render()


class SignatureDecorator(MessageDecorator):
    """Конкретный декоратор: добавляет подпись после сообщения"""
    def __init__(self, message: BaseMessage, signature: str) -> None:
        super().__init__(message)
        self.signature = signature

    def render(self) -> str:
        return self._message.render() + self.signature


class DateDecorator(MessageDecorator):
    """Конкретный декоратор: добавляет дату после сообщения"""
    def __init__(self, message: BaseMessage, date: str) -> None:
        super().__init__(message)
        self.date = date

    def render(self) -> str:
        return self._message.render() + self.date


class Base64Decorator(MessageDecorator):
    """Конкретный декоратор: возвращает всё сформированное сообщение в Base64"""
    def render(self) -> str:
        return base64.b64encode(self._message.render().encode("utf-8")).decode("utf-8")