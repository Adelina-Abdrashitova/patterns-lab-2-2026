from datetime import datetime

from messages import Message
from decorators.message_decorator import HeaderDecorator, SignatureDecorator
from proxies.protected_message_proxy import ProtectedMessageProxy, LoggingMessageProxy
from security import AccessPolicy, UserContext

msg = "я тебя могну"


def test_1_proxy_allowed():
    """Защищающий заместитель с нужной ролью: render() возвращает текст сообщения"""
    proxy = ProtectedMessageProxy(
        Message(msg),
        AccessPolicy("reader"),
        UserContext.of("Danil Kolbasenko", "reader"),
    )
    assert proxy.render() == msg


def test_2_proxy_denied():
    """Защищающий заместитель без нужной роли: render() возбуждает PermissionError"""
    proxy = ProtectedMessageProxy(
        Message(msg),
        AccessPolicy("reader"),
        UserContext.of("Ivan Zolo", "guest"),
    )
    try:
        proxy.render()
    except PermissionError:
        pass
    else:
        assert False, "ожидался PermissionError"


def test_3_proxy_does_not_change_message():
    """Защищающий заместитель не меняет содержание сообщения, обёрнутого в декораторы"""
    message = HeaderDecorator(Message(msg), "Ты слишком низкий, а я люблю высоких ")
    message = SignatureDecorator(message, " -- мо-могну")
    proxy = ProtectedMessageProxy(
        message,
        AccessPolicy("reader"),
        UserContext.of("alice", "reader"),
    )
    assert proxy.render() == "Ты слишком низкий, а я люблю высоких " + msg + " -- мо-могну"


def test_4_logging_writes_to_log():
    """Заместитель-журнал: render() добавляет запись (время и текст)"""
    proxy = LoggingMessageProxy(Message(msg))
    assert proxy.render() == msg
    assert len(proxy.log) == 1
    ts, text = proxy.log[0]
    assert isinstance(ts, datetime) and text == msg


def test_5_logging_does_not_change_message():
    """Заместитель-журнал: render() возвращает ровно текст обёрнутого сообщения"""
    proxy = LoggingMessageProxy(Message(msg))
    assert proxy.render() == Message(msg).render()


def test_6_two_proxies_together():
    """Два прокси вместе: Logging поверх Protected — доступ есть, запись в журнале есть"""
    protected = ProtectedMessageProxy(
        Message(msg),
        AccessPolicy("reader"),
        UserContext.of("Danil Kolbasenko", "reader"),
    )
    logging_proxy = LoggingMessageProxy(protected)

    assert logging_proxy.render() == msg
    assert len(logging_proxy.log) == 1
    assert logging_proxy.log[0][1] == msg