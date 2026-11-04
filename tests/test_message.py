from messages import Message


def test_message_returns_original_text() -> None:
    message = Message("hello")
    assert message.render() == "hello"
