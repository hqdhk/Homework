# 11 -> 22
# 188 -> 191
# 191 -> 202
# 2541 -> 2552

def ispalindrom(number: int) -> int:
    for el in range(number + 1, number + 50):
        reverse_num = int("".join(list(str(el)[::-1])))
        if el == reverse_num:
            return el


# 1. Написать функцию, которая будет конвертировать любую переданную ей строку в CamelCase.
# "the-stealth-warrior" -> "theStealthWarrior"
# "The_Stealth_Warrior" -> "TheStealthWarrior"

def convert_camelcase(text: str) -> str:
    if len(text.split("-")) > 1:
        elements = [text.split('-')[0].lower(), text.split('-')[1].capitalize(), text.split('-')[2].capitalize()]
        return "".join(elements)
    else:
        return "".join(text.split('_'))










