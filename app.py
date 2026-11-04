from messages import Message


def main() -> None:
    message = Message("С наступающим Новым годом!")
    print(message.render())
    print()
    print("После выполнения задания здесь должна быть демонстрация Decorator и Proxy.")


if __name__ == "__main__":
    main()
