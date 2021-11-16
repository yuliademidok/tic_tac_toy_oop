interface_string = {
    "welcome": "Добро пожаловать в Игру Крестики Нолики",
    "invalid_mode_value": "Недопустимый ввод, введите только число",
    "invalid_mode_key": "Недопустимое значение, повторите ввод",
    "enter_name": "Введите свое имя",
    "ask_step": "Введите координаты хода через пробел\n",
    "invalid_step": "Ячейка не существует или занята",
#     "help": """Игроки по очереди ставят на свободные клетки поля знаки.
# Введите режим ("-mode") и имена игроков ("-u1", "-u2")""",
}

template_variants = {
    "enter_name": lambda template, **kwargs: template.format(**kwargs),
    "ask_step": lambda template, **kwargs: template.format(**kwargs),
}


def user_interface(template_name, **template_vars):
    if template_name in template_variants:
        ask_str = template_variants[template_name](interface_string[template_name], **template_vars)
        user_input = input(ask_str.format(variants=template_variants[template_name]))
        return user_input
    else:
        print(interface_string[template_name])
