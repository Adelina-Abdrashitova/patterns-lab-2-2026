from abc import ABC, abstractmethod


class BaseMessage(ABC):
    @abstractmethod
    def render(self) -> str:
        """Возвращает текстовое представление сообщения."""
        raise NotImplementedError
