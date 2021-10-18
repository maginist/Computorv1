
from utils.polynom import Polynom


def print_error(arg, index, error):
    error_message = {
        0: "Syntax error: Argument is not an equation",
        1: f"Syntax error: The equation is not well formated, {arg}.",
        2: f"Syntax error: bad caractere at index : {index}, you wrote '{arg}'.",
        3: f"Syntax error: forbidden operation on the left side at index: {index}, you wrote '{arg}'.",
        4: f"Syntax error: forbidden operation on the right side at index: {index}, you wrote '{arg}'.",
        5: "Degree of the equation is too high.",
        6: f"{arg}",
    }
    print(error_message.get(error))
    exit()


def abs(nb):
    if nb < 0:
        return (nb * (-1)) + 0
    else:
        return nb + 0


def sqrt(nb):
    x = 1
    y = 0.5 * (x + nb)
    while abs(y - x) > 0.00000001:
        x = y
        y = 0.5 * (x + nb / x)
    return y + 0

def create_polynom(before, after):
    polylist = []
    for i in before:
        polylist.append(Polynom(i[0]))
