import re
from .utils import print_error

# cas possible :
# a * x + b = c + x
# a * x^1 + (b * x) + c = d
# ax^2 + bx^1 + cx^0 + d = e + fx^2
# 2(ax^2 + b) = c + x
# (5 * X^0 + 4 * X^1 - 9.3 * X^2) = (1 * X^0)


def check_float(polylist):
    tmp = ""
    for i in polylist:
        if "." in i:
            tmp = tmp + i
    if tmp is None:
        return 0
    # floater = re.findall(r".[\.].", tmp)
    # print(floater)


def check_degree(polylist):
    tmp = ""
    print(polylist)
    for i in polylist:
        if "^" in i:
            tmp = tmp + i
    power = re.findall(r"[X]\^[\d]+", tmp)
    print(power)
    for i in power:
        degree = int(i[i.index("^") + 1:])
        print(degree)
        if degree > 2:
            print_error(0, 0, 5)


def check_power(polylist, side):
    for i in polylist:
        if "^" in i:
            power = 0
            for index in range(len(i)):
                if i[index] == "^":
                    power = power + 1
                    if index + 1 not in range(len(i)):
                        print_error("A power is not well formated", 0, 6)
                if power > 1:
                    print_error("You can't use more than one power on a polynom.", 0, 6)


def check_separator(poly, side):
    sign = 1
    if poly[0] == " ":
        poly = re.sub(r"(^ )", "", poly)
    if poly[0] == "*":
        print_error(poly[0], 0, side)
    if poly[0] == "+":
        poly = re.sub(r"^\+", "", poly)
    if side == 3:
        polylen = len(poly) - 2
    else:
        polylen = len(poly) - 1
    if poly[polylen] in "+-*":
        print_error(poly[polylen], polylen, side)
    polylist = re.split(r"[+*-][^X]", poly)
    separator = re.findall(r"[+*-][^X]", poly)
    if poly[0] == "-":
        polylist = re.split(r"[+*-][^X]", poly)[1:]
        sign = 0
    for i in polylist:
        if i == "":
            print_error("do not use more than 1 operator within arguments", 0, 1)
    if len(separator) + sign != len(polylist):
        print_error("do not use more than 1 operator within arguments", 0, 1)
    return polylist


def check_poly(poly, side):
    polylist = check_separator(poly, side)
    check_power(polylist, side)
    check_float(polylist)
    check_degree(polylist)
    return polylist


def parse_equation(expression):
    before, after = None, None
    expression = re.sub(r"(.)?([+-])(.)", r"\g<1> \g<2> \g<3>", expression)  # add space within +-
    expression = re.sub(
        r"(\d+)?([+*-])([^xX][\d+]?)", r"\g<1> \g<2> \g<3>", expression
    )  # add space within all operator except '*X'
    expression = re.sub(r"(.)?([\^])(.)", r"\g<1> \g<2> \g<3>", expression)  # add space within ^
    expression = re.sub(
        r"(\d+)?([\^])([\d+]?)", r"\g<1> \g<2> \g<3>", expression
    )  # add space within all power
    expression = re.sub(r"\s+", " ", expression)  # del all superfluous space
    expression = re.sub(r"(\s\^\s)", "^", expression)  # del space within ^ and all
    if expression[0] == " ":
        expression = re.sub(r"(^ )", "", expression)
    expression = expression.replace(r"x", r"X")
    print("expression modified = ", expression)
    split = expression.split("=")
    if len(split) != 2:
        print_error(0, 0, 0)
    before = split[0]
    after = split[1]
    for i, index in enumerate(expression):
        if index not in "0123456789.+-=* ^X":
            print_error(index, i, 2)
    polynomleft = check_poly(before, 3)
    polynomrigth = check_poly(after, 4)
    return polynomleft, polynomrigth
