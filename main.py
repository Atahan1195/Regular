import re
# Напишите регулярное выражение, которое будет находить в тексте фрагменты, состоящие из одной буквы R,
# за которой следует одна или более букв b, за которой одна r. Учитывать верхний и нижний регистр.

text = "RbbbbbbRbRbrrrrbrbrbrrrrrRbRbRb"
pattern = re.compile(r"Rb+r")
matches = pattern.findall(text)


# Напишите функцию, выполняющую валидацию номера банковской карты (9999-9999-9999-9999-9999).

def validate_card(card):
    pattern = re.compile(r"\d{4}-\d{4}-\d{4}-\d{4}-\d{4}")
    matches = pattern.findall(card)
    if matches:
        return True
    else:
        return False


# Напишите функцию, которая принимает строковые данные и выполняет проверку на их соответствие мейлу.
# Требования:
# -Цифры (0-9).
# -только латинские буквы в большом (A-Z) и малом (a-z) регистрах.
# -в теле мейла допустимы только символы "_" и "-". Но они не могут быть первым символом мейла.
# -Символ "-" не может повторяться.

def validate_mail(gmail):
    pattern = re.compile(r'^[a-zA-Z]+([_-]?[a-zA-Z0-9]+)*@gmail\.(com)$')
    matches = pattern.findall(gmail)
    if matches:
        return True
    else:
        return False


# Напишите функцию, которая проверяет правильность логина. Правильный логин - строка от 2 до 10 символов,
# содержащая только буквы и цифры.

def validate_login(login):
    pattern = re.compile(r'^[a-zA-Z0-9]{2,10}$')
    matches = pattern.findall(login)
    if matches:
        return True
    else:
        return False











