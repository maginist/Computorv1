from mpl_toolkits.axisartist.axislines import AxesZero
from utils.polynom import Polynom
import matplotlib.pyplot as plt

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

def get_pgcd(nb, denom):
   while nb%denom != 0 :
      nb, denom = denom, nb%denom
   return denom

def get_denominator(nb):
    str_nb = str(nb)
    count = -1
    mul = 1
    for i in str_nb:
        if count >= 0:
            count += 1
        if i == '.':
            count = 0
    while count > 0:
        mul = mul * 10
        count -= 1
    return mul

def get_irreductible_fraction(nb):
    denominator = get_denominator(nb)
    nb = nb * denominator
    nb = int(nb)
    pgcd = get_pgcd(nb, denominator)
    nb = nb / pgcd
    denominator = denominator / pgcd
    fraction = str(int(nb)) + '/' + str(int(denominator))
    if nb == 0 or nb < 0 :
        fraction = "None"
    return fraction

def get_degree(eq):
    degree = 0
    for i in eq:
        if degree < i.power:
            degree = i.power
    print("Polynomial degree :", degree)
    if degree > 2:
        print_error(0, 0, 5)
    return degree

def abs(nb):
    if nb < 0:
        return (nb * (-1)) + 0
    else:
        return nb + 0

def display_graph(eq):
    list_x = []
    list_y =[]
    for x in range(-50, 50):
        y = 0
        for i in eq:
            if i.sign == "+":
                sign = 1
            else:
                sign = -1
            if i.x is True:
                y += sign * i.factor * (x**i.power)
            else:
                y += sign * i.factor
        list_x.append(x)
        list_y.append(y)
    ax = plt.figure().add_subplot(axes_class=AxesZero)
    for direction in ["xzero", "yzero"]:
        #add orthonormal
        ax.axis[direction].set_axisline_style("-|>")
        ax.axis[direction].set_visible(True)
    for direction in ["left", "right", "bottom", "top"]:
    # hides borders
        ax.axis[direction].set_visible(False)
    ax.plot(list_x,list_y)
    ax.set_ylabel("y")
    ax.set_xlabel("x")
    ax.set_title("Computorv1")
    plt.show()