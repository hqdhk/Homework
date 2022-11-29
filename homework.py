# 11 -> 22
# 188 -> 191
# 191 -> 202
# 2541 -> 2552

def ispalindrom(number: int) -> int:
    for el in range(number + 1, number + 50):
        reverse_num = int("".join(list(str(el)[::-1])))
        if el == reverse_num:
            return el









