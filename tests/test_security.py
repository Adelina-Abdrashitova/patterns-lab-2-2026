from security import AccessPolicy, UserContext


def test_access_policy() -> None:
    policy = AccessPolicy("reader")

    assert policy.is_allowed(UserContext.of("alice", "reader"))
    assert not policy.is_allowed(UserContext.of("bob", "guest"))
