"""
Реализуйте ProtectedMessageProxy.

Proxy должен предоставлять интерфейс BaseMessage, проверять AccessPolicy
и делегировать render() реальному объекту только при наличии доступа.
"""

# TODO: реализуйте ProtectedMessageProxy.
from datetime import datetime
from interfaces import BaseMessage
from security import AccessPolicy, UserContext


class ProtectedMessageProxy(BaseMessage):
    """Защищающий заместитель: писать могут только определенные роли"""
    def __init__(self, message: BaseMessage, policy: AccessPolicy, user: UserContext) -> None:
        self._message = message
        self._policy = policy
        self._user = user

    def render(self) -> str:
        if not self._policy.is_allowed(self._user):
            raise PermissionError(f"Недостаточно прав для просмотра сообщения")
        return self._message.render()


class LoggingMessageProxy(BaseMessage):
    """Заместитель-журнал: записывает каждое сообщение, затем передаёт его и дату"""
    def __init__(self, message: BaseMessage) -> None:
        self._message = message
        self.log: list[tuple[datetime, str]] = []

    def render(self) -> str:
        self.log.append((datetime.now(), self._message.render()))
        return self._message.render()