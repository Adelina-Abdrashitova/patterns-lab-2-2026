from messages import Message
from decorators.message_decorator import HeaderDecorator, DateDecorator, SignatureDecorator, Base64Decorator
from proxies.protected_message_proxy import ProtectedMessageProxy
from security import AccessPolicy, UserContext


def main() -> None:

    message = Message("С наступающим Новым годом!")

    # Декоратор: сообщение
    decorated = HeaderDecorator(message, "Дорогой друг!")
    decorated = SignatureDecorator(decorated, " -- Дед Мороз")
    decorated = DateDecorator(decorated, " 31.12.2026")
    print(decorated.render())
    encoded = Base64Decorator(decorated)
    print(encoded.render())

    # Прокси: успешный доступ
    policy = AccessPolicy("reader")
    reader = UserContext.of("Father Frost", "reader")
    print(ProtectedMessageProxy(decorated, policy, reader).render())

    # Прокси: отказ в доступе
    guest = UserContext.of("bob", "guest")
    try:
        ProtectedMessageProxy(decorated, policy, guest).render()
    except PermissionError as e:
        print(f"{e}")


if __name__ == "__main__":
    main()
