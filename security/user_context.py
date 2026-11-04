from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class UserContext:
    username: str
    roles: frozenset[str]

    @classmethod
    def of(cls, username: str, *roles: str) -> "UserContext":
        return cls(username=username, roles=frozenset(roles))
