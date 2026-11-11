import base64
from messages import Message
from decorators.message_decorator import HeaderDecorator, SignatureDecorator, DateDecorator, Base64Decorator

msg = "мне не подобрать слов, чтобы описать ту боль и унижение, которые я испытал"


def test_1_header():
    """Конкретный декоратор: добавляет заголовок перед сообщением"""
    message = HeaderDecorator(Message(msg), "Дорогой дневник, ")
    assert message.render() == "Дорогой дневник, " + msg


def test_2_signature():
    """Конкретный декоратор: добавляет подпись после сообщения"""
    message = SignatureDecorator(Message(msg), " -- Кот Барсик")
    assert message.render() == msg + " -- Кот Барсик"


def test_3_date():
    """Конкретный декоратор: добавляет дату после сообщения"""
    message = DateDecorator(Message(msg), " 31.12.2026")
    assert message.render() == msg + " 31.12.2026"


def test_4_base64():
    """Конкретный декоратор: возвращает всё сформированное сообщение в Base64"""
    message = Base64Decorator(Message(msg))
    assert message.render() == base64.b64encode(msg.encode()).decode()


def test_5_combination():
    """Комбинация декораторов: заголовок, подпись и дата"""
    message = HeaderDecorator(Message(msg), "Дорогой дневник, ")
    message = SignatureDecorator(message, " -- Кот Барсик")
    message = DateDecorator(message, " 31.12.2026")
    assert message.render() == "Дорогой дневник, " + msg + " -- Кот Барсик 31.12.2026"


def test_6_base64_combination():
    """Комбинация декораторов: Base64 поверх всей цепочки декораторов"""
    message = HeaderDecorator(Message(msg), "Дорогой дневник, ")
    message = SignatureDecorator(message, " -- Кот Барсик")
    message = DateDecorator(message, " 31.12.2026")
    message = Base64Decorator(message)
    expected = base64.b64encode(("Дорогой дневник, " + msg + " -- Кот Барсик 31.12.2026").encode("utf-8")).decode("utf-8")
    assert message.render() == expected