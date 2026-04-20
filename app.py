def login(user, password):
    if not user or not password:
        print("Ошибка: пустые данные")
        return False

    if password == "1234":
        print("Успешный вход")
        return True
    else:
        print("Неверный пароль")
        return False
