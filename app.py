def login(username, password):
 if not isinstance(username, str) or not isinstance(password, str):
    print("Ошибка: неверный тип данных")
    return False
    # валидация
    if not username or not password:
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
    if username == "admin":
        return "Администратор"
    elif username:
        return "Обычный пользователь"
    else:
        return "Гость" 


# запуск программы
username = input("Введите имя: ")
password = input("Введите пароль: ")

if login(username, password):
    status = get_username_status(username)
    print("Статус:", status)
