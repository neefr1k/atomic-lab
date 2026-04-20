def login(user, password):
    # валидация
    if not user or not password:
        print("Ошибка: пустые данные")
        return False

    # бизнес-логика
    if password == "1234":
        print("Успешный вход")
        return True
    else:
        print("Неверный пароль")
        return False


def get_user_status(user):
    # новая функция
    if user == "admin":
        return "Администратор"
    elif user:
        return "Обычный пользователь"
    else:
        return "Гость"


# запуск программы
user = input("Введите имя: ")
password = input("Введите пароль: ")

if login(user, password):
    status = get_user_status(user)
    print("Статус:", status)
