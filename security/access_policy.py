from .user_context import UserContext


class AccessPolicy:
    def __init__(self, required_role: str) -> None:
        self._required_role = required_role

    def is_allowed(self, user: UserContext) -> bool:
        return self._required_role in user.roles
